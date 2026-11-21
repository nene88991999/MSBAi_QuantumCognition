"""Offline tests of the collection protocol. No API key or network is used."""
import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import sys

P = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(P))
import lumen_collector as lc
import audit


class FakeLumen:
    def __init__(self, actions=None):
        self.calls = []
        self.actions = list(actions or [])
        self.metadata = {'id': 'nemotron-3-super-120b-a12b', 'parent': None, 'tags': [],
                         'input_cost_per_million': 1., 'output_cost_per_million': 2.}
        self.interrupt_metadata_once = False

    def get_model(self, model):
        if self.interrupt_metadata_once and len(self.calls) == 7:
            self.interrupt_metadata_once = False
            raise lc.CallError(503, 'temporary_metadata_failure')
        return copy.deepcopy(self.metadata)

    def usage(self):
        return {'cost': len(self.calls) * .00001, 'coins_available': 10.}

    def complete(self, payload):
        self.calls.append(copy.deepcopy(payload))
        action = self.actions.pop(0) if self.actions else ('YES' if len(self.calls) % 2 else 'NO')
        if isinstance(action, BaseException):
            raise action
        if isinstance(action, dict):
            return copy.deepcopy(action)
        return {'id': f'fake-{len(self.calls)}', 'model': 'fake-fixed-model',
                'choices': [{'finish_reason': 'stop', 'message': {'role': 'assistant', 'content': action}}],
                'usage': {'prompt_tokens': 100, 'completion_tokens': 1, 'total_tokens': 101}}


class CollectorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.out = Path(self.temp.name) / 'run'
        self.config = json.loads((P/'lumen_example_config.json').read_text())
        self.config['example_only'] = False
        self.client = FakeLumen()

    def tearDown(self):
        self.temp.cleanup()

    def run_main(self):
        return lc.collect(self.config, self.out, mode='main', transport=self.client,
                          model_and_settings_approved=True, sleep=lambda _: None)

    def short(self):
        self.config['personas'] = self.config['personas'][:2]

    def attempts(self):
        return [json.loads(p.read_text()) for p in sorted((self.out/'attempts').glob('*.json'))]

    def test_360_calls_correct_context_and_audit_export(self):
        summary = self.run_main()
        self.assertEqual((summary['personas'], summary['interviews'], summary['attempts']), (24, 144, 360))
        self.assertEqual(lc.check_export(self.out)['interviews'], 144)
        records = json.loads((self.out/'interviews.json').read_text())
        data, ids = audit.validate_records(records, require_raw=True, base_dir=self.out)
        self.assertEqual(data.shape, (24, 6, 3))
        self.assertEqual(len(ids), 24)
        for row in records:
            raw = json.loads((self.out/row['raw_file']).read_text())
            sequence, retain = lc.DESIGN[row['condition']]
            self.assertEqual([m['question'] for m in raw['messages']], list(sequence))
            history = []
            for i, record in enumerate(raw['messages']):
                messages = record['request_messages']
                self.assertEqual(len(messages), 2+2*i if retain else 2)
                self.assertEqual(messages[-1]['content'], self.config['questions'][sequence[i]])
                if retain:
                    self.assertEqual(messages[1:-1], history)
                history += [messages[-1], record['response_message']]
            for a in raw['retry_history']:
                self.assertEqual(a['request']['chat_template_kwargs'], {'enable_thinking': False})
        # Rerunning a completed batch returns its checked summary without more calls.
        self.run_main()
        self.assertEqual(len(self.client.calls), 360)

    def test_retries_preserve_requests_and_first_valid_answer(self):
        self.short()
        self.client = FakeLumen(['YES, probably', lc.CallError(None, 'network_error'), ' no '])
        summary = self.run_main()
        attempts = self.attempts()
        self.assertEqual(summary['attempts'], 32)
        self.assertEqual([a['accepted'] for a in attempts[:3]], [False, False, True])
        self.assertEqual(attempts[2]['answer'], 0)
        self.assertEqual(attempts[0]['request'], attempts[1]['request'])
        self.assertEqual(attempts[1]['request'], attempts[2]['request'])

    def test_known_interruption_resumes_without_duplicate_calls(self):
        self.short()
        self.client.interrupt_metadata_once = True
        with self.assertRaises(lc.CallError):
            self.run_main()
        self.assertEqual(len(self.client.calls), 7)
        self.assertEqual(self.run_main()['attempts'], 30)
        self.assertEqual(len(self.client.calls), 30)

    def test_unknown_interruption_blocks_automatic_retry(self):
        self.short()
        self.client = FakeLumen([KeyboardInterrupt()])
        with self.assertRaises(KeyboardInterrupt):
            self.run_main()
        self.assertEqual(self.attempts()[0]['status'], 'started')
        with self.assertRaisesRegex(lc.CollectionStopped, 'unknown outcome'):
            self.run_main()
        self.assertEqual(len(self.client.calls), 1)

    def test_quota_does_not_retry_or_switch_models(self):
        self.short()
        self.client = FakeLumen([lc.CallError(429, 'insufficient_quota')])
        with self.assertRaises(lc.CollectionStopped):
            self.run_main()
        with self.assertRaises(lc.CollectionStopped):
            self.run_main()
        self.assertEqual(len(self.client.calls), 1)
        self.assertTrue(self.attempts()[0]['fatal'])

    def test_rate_limit_retries_with_same_payload(self):
        self.short()
        self.client = FakeLumen([lc.CallError(429, 'rate_limit_exceeded', retry_after=1)])
        summary = self.run_main()
        self.assertEqual(summary['attempts'], 31)
        self.assertEqual(self.client.calls[0], self.client.calls[1])

    def test_truncation_or_reasoning_requires_review(self):
        self.short()
        for kind in ['length', 'reasoning']:
            self.out = Path(self.temp.name)/kind
            response = {'model': 'fake-fixed-model', 'choices': [{'finish_reason': 'stop',
                         'message': {'role': 'assistant', 'content': 'YES'}}]}
            if kind == 'length':response['choices'][0]['finish_reason']='length'
            else:response['choices'][0]['message']['reasoning_content']='unfinished reasoning'
            self.client = FakeLumen([response])
            with self.assertRaises(lc.CollectionStopped):self.run_main()
            self.assertEqual(len(self.client.calls), 1)

    def test_frozen_configuration_and_metadata_are_enforced(self):
        self.short()
        self.client.interrupt_metadata_once=True
        with self.assertRaises(lc.CallError):self.run_main()
        self.config['questions']['A'] += ' Changed.'
        with self.assertRaisesRegex(lc.CollectionStopped, 'frozen configuration'):self.run_main()
        self.config['questions']['A'] = self.config['questions']['A'].removesuffix(' Changed.')
        self.client.metadata['parent'] = 'changed-deployment'
        with self.assertRaisesRegex(lc.CollectionStopped, 'identity or pricing'):self.run_main()
        self.assertEqual(len(self.client.calls), 7)

    def test_attempt_cap_and_invalid_format_limit(self):
        self.short()
        self.config['max_total_attempts']=2
        with self.assertRaisesRegex(lc.CollectionStopped, 'attempt limit'):self.run_main()
        self.assertEqual(len(self.client.calls),2)
        self.out=Path(self.temp.name)/'invalid'
        self.config['max_total_attempts']=450
        self.client=FakeLumen(['maybe','YES.','NO.'])
        with self.assertRaisesRegex(lc.CollectionStopped, 'attempt limit'):self.run_main()
        self.assertEqual(len(self.client.calls),3)
        self.assertFalse(any(a['accepted'] for a in self.attempts()))

    def test_dry_run_is_offline_and_cannot_be_main_data(self):
        self.short()
        with patch.object(lc.LumenHTTP, '_request', side_effect=AssertionError('Network forbidden')):
            summary=lc.collect(self.config,self.out,transport=self.client)
        self.assertEqual(len(self.client.calls),0)
        self.assertEqual(summary['records_file'],'dry_run_interviews.json')
        records=json.loads((self.out/summary['records_file']).read_text())
        with self.assertRaisesRegex(ValueError, 'main project data'):
            audit.validate_records(records,require_raw=True,base_dir=self.out)
        # The raw record retains the label even if a row's label is lost.
        for row in records:row.pop('data_origin')
        with self.assertRaisesRegex(ValueError, 'practice data'):
            audit.validate_records(records,require_raw=True,base_dir=self.out)

    def test_pilot_is_labelled_and_example_cannot_be_main(self):
        self.short()
        summary=lc.collect(self.config,self.out,mode='pilot',transport=self.client,
                           model_and_settings_approved=True,sleep=lambda _:None)
        records=json.loads((self.out/summary['records_file']).read_text())
        with self.assertRaises(ValueError):audit.validate_records(records,True,self.out)
        self.out=Path(self.temp.name)/'main'
        self.config['example_only']=True
        with self.assertRaisesRegex(lc.CollectionStopped,'example'):self.run_main()

    def test_changed_completed_file_detected(self):
        self.short(); self.run_main()
        (self.out/'interviews.json').write_text('[]')
        with self.assertRaisesRegex(lc.CollectionStopped,'completed output'):self.run_main()
        self.assertEqual(len(self.client.calls),30)

    def test_budget_estimate_and_spending_stop(self):
        self.short(); self.run_main()
        estimate=lc.budget_estimate(self.config,self.out)
        self.assertAlmostEqual(estimate['projected_coins_from_tokens'],.00306)
        self.out=Path(self.temp.name)/'budget'
        self.client=FakeLumen()
        self.config['max_coins_per_run']=.00002
        with self.assertRaisesRegex(lc.CollectionStopped,'spending stop'):self.run_main()
        self.assertEqual(len(self.client.calls),2)

    def test_live_approval_and_exclusive_run_lock(self):
        with self.assertRaises(lc.CollectionStopped):
            lc.collect(self.config,self.out,mode='main',transport=self.client)
        self.out.mkdir(parents=True)
        (self.out/'.collection.lock').write_text('someone else')
        with self.assertRaisesRegex(lc.CollectionStopped,'run lock'):self.run_main()
        self.assertEqual(len(self.client.calls),0)

    def test_credentials_rejected_before_saving_configuration(self):
        self.config['background'] += ' secret-test-key'
        self.client=lc.LumenHTTP('secret-test-key')
        with self.assertRaisesRegex(lc.CollectionStopped,'credential'):self.run_main()
        self.assertFalse(self.out.exists())


if __name__ == '__main__':
    unittest.main()
