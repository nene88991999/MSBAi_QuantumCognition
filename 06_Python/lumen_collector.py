"""Six-condition Lumen collector. Importing this module makes no network calls.

Use M1_4_Lumen_Collection.ipynb. Only the explicit pilot/main modes call Lumen.
The HTTP transport uses Python's standard library and has no hidden retries.
"""
from __future__ import annotations

import copy
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import random
import re
import time
from urllib import error, parse, request

BASE_URL = "https://lumen.ncsa.illinois.edu/v1"
DESIGN = {
    "isolated_AB": ("ABF", False),
    "isolated_BA": ("BAF", False),
    "constructed_AB": ("ABF", True),
    "constructed_BA": ("BAF", True),
    "direct": ("F", False),
    "assessed": ("AF", True),
}
METADATA_FIELDS = ("id", "parent", "created", "owned_by", "input_cost_per_million",
                   "output_cost_per_million", "cached_input_cost_per_million",
                   "cache_write_cost_per_million")


class CollectionStopped(RuntimeError):
    """The saved record explains why collection stopped. Do not delete it."""


class CallError(Exception):
    def __init__(self, status, code, body=None, retry_after=None):
        super().__init__(f"Lumen request stopped: status={status}, code={code}")
        self.status, self.code = status, code
        self.body, self.retry_after = body, retry_after


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def digest(value):
    return hashlib.sha256(canonical(value).encode()).hexdigest()


def save_json(path, value):
    """Replace a JSON file atomically; flush it before replacing the old copy."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    with tmp.open("w", encoding="utf-8") as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2, allow_nan=False)
        stream.write("\n")
        stream.flush()
        os.fsync(stream.fileno())
    tmp.replace(path)


class _NoRedirect(request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


class LumenHTTP:
    """A single-attempt HTTPS transport. Never serializes the credential."""
    def __init__(self, api_key, timeout=60):
        if not isinstance(api_key, str) or not api_key.strip():
            raise ValueError("Enter your own Lumen key in the hidden prompt.")
        self._key, self.timeout = api_key.strip(), timeout
        self._opener = request.build_opener(_NoRedirect())

    def _request(self, method, path, payload=None):
        body = None if payload is None else canonical(payload).encode()
        if body and self._key.encode() in body:
            raise ValueError("A credential appeared in the request content. Remove it.")
        req = request.Request(BASE_URL + path, data=body, method=method,
                              headers={"Authorization": "Bearer " + self._key,
                                       "Content-Type": "application/json"})
        try:
            with self._opener.open(req, timeout=self.timeout) as response:
                text = response.read().decode("utf-8").replace(self._key, "[REDACTED]")
                try:
                    return json.loads(text)
                except json.JSONDecodeError:
                    raise CallError(200, "invalid_json", {"raw_response": text}) from None
        except error.HTTPError as exc:
            text = exc.read().decode("utf-8", errors="replace").replace(self._key, "[REDACTED]")
            try:
                details = json.loads(text)
            except json.JSONDecodeError:
                details = {"raw_response": text}
            err = details.get("error", {}) if isinstance(details, dict) else {}
            code = err.get("code", "http_error") if isinstance(err, dict) else "http_error"
            wait = exc.headers.get("Retry-After")
            try:
                wait = float(wait) if wait is not None else None
            except ValueError:
                wait = None
            raise CallError(exc.code, code, details, wait) from None
        except (error.URLError, TimeoutError, ConnectionError, OSError):
            # The provider might have received a timed-out request. Count the attempt.
            raise CallError(None, "network_error", {"delivery_status": "unknown"}) from None

    def get_model(self, model):
        return self._request("GET", "/models/" + parse.quote(model, safe=""))

    def usage(self):
        return self._request("GET", "/usage")

    def complete(self, payload):
        return self._request("POST", "/chat/completions", payload)


def validate_config(config):
    c = copy.deepcopy(config)
    for key in ("model", "system_instruction", "background", "questions", "personas",
                "settings", "schedule_seed", "max_attempts_per_question",
                "max_total_attempts", "max_coins_per_run", "example_only"):
        if key not in c:
            raise ValueError(f"Missing configuration field: {key}")
    if set(c["questions"]) != set("ABF") or any(not isinstance(v, str) or not v.strip()
                                               for v in c["questions"].values()):
        raise ValueError("Supply one nonempty question each for A, B, and F.")
    if not isinstance(c["model"], str) or not c["model"].strip():
        raise ValueError("Supply the exact approved Lumen model ID.")
    if any(not isinstance(c[k], str) or not c[k].strip() for k in ("system_instruction", "background")):
        raise ValueError("Supply the instruction and common background.")
    if not isinstance(c["personas"], list) or len(c["personas"]) < 2:
        raise ValueError("Use at least two persona blocks, including for a pilot.")
    ids = []
    for persona in c["personas"]:
        pid = persona.get("persona_id", "")
        if not re.fullmatch(r"[A-Za-z0-9_-]{1,64}", pid):
            raise ValueError("Persona IDs must be simple letters, numbers, underscores, or hyphens.")
        if not isinstance(persona.get("description"), str) or not persona["description"].strip():
            raise ValueError("Every persona needs a fictional description.")
        ids.append(pid)
    if len(set(ids)) != len(ids):
        raise ValueError("Persona IDs must be unique.")
    settings = c["settings"]
    if set(settings) != {"temperature", "top_p", "max_tokens", "chat_template_kwargs"}:
        raise ValueError("Use the documented four settings; review protocol changes with the instructor.")
    if not 0 <= settings["temperature"] <= 2 or not 0 < settings["top_p"] <= 1:
        raise ValueError("Invalid sampling settings.")
    if type(settings["max_tokens"]) is not int or settings["max_tokens"] < 1:
        raise ValueError("max_tokens must be a positive integer.")
    if settings["chat_template_kwargs"] != {"enable_thinking": False}:
        raise ValueError("This template requests reasoning off. A different model needs a reviewed protocol.")
    for key in ("max_attempts_per_question", "max_total_attempts"):
        if type(c[key]) is not int or c[key] < 1:
            raise ValueError(f"{key} must be a positive integer.")
    if type(c["schedule_seed"]) is not int or type(c["example_only"]) is not bool:
        raise ValueError("Check schedule_seed and example_only types.")
    if not isinstance(c["max_coins_per_run"], (int, float)) or c["max_coins_per_run"] <= 0:
        raise ValueError("Choose a positive spending stop level before the run.")
    return c


def make_schedule(config):
    c = validate_config(config)
    rows = [{"persona_id": p["persona_id"], "condition": condition,
             "interview_id": p["persona_id"] + "_" + condition}
            for p in c["personas"] for condition in DESIGN]
    random.Random(c["schedule_seed"]).shuffle(rows)
    return rows


def plan_summary(config):
    c = validate_config(config)
    n = len(c["personas"])
    return {"personas": n, "interviews": 6 * n, "nominal_calls": 15 * n,
            "maximum_attempts": min(15 * n * c["max_attempts_per_question"], c["max_total_attempts"]),
            "model_requested": c["model"], "example_only": c["example_only"]}


def metadata_identity(metadata):
    return {key: metadata.get(key) for key in METADATA_FIELDS}


def preflight(transport, model):
    """Read metadata and usage only. No model-generation request is made."""
    metadata = transport.get_model(model)
    if not isinstance(metadata, dict) or not metadata.get("id"):
        raise CollectionStopped("Model metadata is missing its ID. Check the service.")
    if metadata.get("tags"):
        raise CollectionStopped("Review the model notice in your own Lumen dashboard before continuing.")
    usage = transport.usage()
    return {"timestamp": utc_now(), "base_url": BASE_URL, "model_metadata": metadata, "usage": usage}


def _messages(config, persona, history, question):
    intro = (config["system_instruction"] + "\n\nFictional persona:\n" + persona["description"]
             + "\n\nCommon background:\n" + config["background"])
    return ([{"role": "system", "content": intro}] + copy.deepcopy(history)
            + [{"role": "user", "content": config["questions"][question]}])


def _answer(response):
    try:
        choice = response["choices"][0]
        message = choice["message"]
        if choice.get("finish_reason") != "stop":
            return None, "finish_reason_requires_review"
        if message.get("reasoning_content") or message.get("reasoning"):
            return None, "reasoning_requires_review"
        text = message["content"]
        if not isinstance(text, str):
            return None, "invalid_format"
        value = text.strip().upper()
        if value not in ("YES", "NO"):
            return None, "invalid_format"
        return int(value == "YES"), None
    except (KeyError, IndexError, TypeError):
        return None, "invalid_format"


def _retryable(exc):
    return (exc.code == "network_error" or exc.status in (408, 500, 502, 503, 504)
            or (exc.status == 429 and exc.code == "rate_limit_exceeded"))


class _DryRun:
    """Constructed test responses. These are never Lumen data."""
    def complete(self, payload):
        bit = int(digest(payload)[0], 16) % 2
        return {"model": "offline-demonstration", "id": "demo-" + digest(payload)[:12],
                "choices": [{"finish_reason": "stop", "message": {
                    "role": "assistant", "content": "YES" if bit else "NO"}}],
                "usage": {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}}


def collect(config, output_dir, *, mode="dry_run", transport=None,
            model_and_settings_approved=False, sleep=time.sleep):
    """Collect or resume exactly one frozen run. A completed run makes no new calls.

    Dry-run responses are constructed. Pilot/main require an explicit approval
    flag. Main also requires example_only=False. Keep pilot and main directories
    separate. This function never chooses a fallback model or removes records.
    """
    c = validate_config(config)
    if mode not in ("dry_run", "pilot", "main"):
        raise ValueError("Use dry_run, pilot, or main.")
    live = mode != "dry_run"
    if live and (transport is None or not model_and_settings_approved):
        raise CollectionStopped("Confirm the instructor's model and settings before live collection.")
    if mode == "main" and c["example_only"]:
        raise CollectionStopped("Replace the example with your approved project design first.")
    if live and isinstance(transport, LumenHTTP) and transport._key in canonical(c):
        raise CollectionStopped("A credential appeared in the configuration. Remove it before saving a run.")
    if mode == "dry_run":
        transport = _DryRun()
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    lock = out / ".collection.lock"
    try:
        lock_fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError:
        raise CollectionStopped("A run lock exists. Confirm no collector is running before investigating it.") from None
    try:
        os.write(lock_fd, str(os.getpid()).encode())
        os.close(lock_fd)
        return _collect_locked(c, out, mode, transport, live, sleep)
    finally:
        lock.unlink(missing_ok=True)


def _collect_locked(c, out, mode, transport, live, sleep):
    frozen = {"schema_version": 1, "collector_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "mode": mode, "config": c, "schedule": make_schedule(c)}
    plan_path = out / "frozen_plan.json"
    if plan_path.exists():
        if json.loads(plan_path.read_text()) != frozen:
            raise CollectionStopped("The frozen configuration or collector changed. Preserve this run and review the revision.")
    else:
        if any(out.glob("attempts/*.json")) or (out / "interviews.json").exists():
            raise CollectionStopped("Records exist without their frozen plan. Restore the plan before continuing.")
        save_json(plan_path, frozen)
    attempts = [json.loads(p.read_text()) for p in sorted((out / "attempts").glob("*.json"))]
    if any(a["status"] == "started" for a in attempts):
        raise CollectionStopped("An interrupted attempt has an unknown outcome. Preserve it and ask the instructor before resuming.")
    if (out / "summary.json").exists():
        summary = json.loads((out / "summary.json").read_text())
        if summary.get("complete"):
            for rel, expected in summary["file_hashes"].items():
                p = out / rel
                if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest() != expected:
                    raise CollectionStopped("A completed output changed or is missing. Restore it before using the data.")
            return summary
    current = preflight(transport, c["model"]) if live else {
        "timestamp": utc_now(), "model_metadata": {"id": "offline-demonstration"}, "usage": {"cost": 0}}
    pre_path = out / "preflight.json"
    if pre_path.exists():
        initial = json.loads(pre_path.read_text())
        if metadata_identity(initial["model_metadata"]) != metadata_identity(current["model_metadata"]):
            raise CollectionStopped("Model identity or pricing changed. Ask the instructor before continuing.")
    else:
        initial = current
        save_json(pre_path, initial)
    personas = {p["persona_id"]: p for p in c["personas"]}
    records = []
    returned = {(a["response"].get("model"), a["response"].get("system_fingerprint"))
                for a in attempts if a.get("accepted")}
    start_cost = initial["usage"].get("cost")
    if live and not isinstance(start_cost, (int, float)):
        raise CollectionStopped("Usage cost is unavailable. Confirm the budget before collecting.")
    for interview in frozen["schedule"]:
        sequence, retain = DESIGN[interview["condition"]]
        history, values, selected = [], {q: None for q in "ABF"}, []
        for question in sequence:
            messages = _messages(c, personas[interview["persona_id"]], history if retain else [], question)
            payload = {"model": c["model"], "messages": messages, **c["settings"]}
            previous = [a for a in attempts if a["interview_id"] == interview["interview_id"] and a["question"] == question]
            if any(a["request"] != payload for a in previous):
                raise CollectionStopped("Saved messages differ from the reconstructed interview. Review the records.")
            accepted = next((a for a in previous if a.get("accepted")), None)
            if not accepted and any(a.get("fatal") for a in previous):
                raise CollectionStopped("A saved attempt needs review. The collector will not silently retry it.")
            while accepted is None:
                if len(previous) >= c["max_attempts_per_question"] or len(attempts) >= c["max_total_attempts"]:
                    raise CollectionStopped("The frozen attempt limit was reached. Preserve the partial run for review.")
                if previous:
                    wait = max(0.0, previous[-1].get("retry_not_before", 0.0) - time.time())
                    if wait > 30:
                        raise CollectionStopped("The service requested a longer wait. Resume this same run later.")
                    sleep(wait)
                if live:
                    status = transport.usage()
                    balance, cost = status.get("coins_available"), status.get("cost")
                    if not isinstance(cost, (int, float)) or cost < start_cost:
                        raise CollectionStopped("Usage accounting changed or is unavailable. Review before continuing.")
                    if cost - start_cost >= c["max_coins_per_run"] or balance is None or (balance != -2 and balance <= 0):
                        raise CollectionStopped("The spending stop level or available balance was reached.")
                    model_now = transport.get_model(c["model"])
                    if model_now.get("tags") or metadata_identity(model_now) != metadata_identity(initial["model_metadata"]):
                        raise CollectionStopped("The model's access, identity, or price changed. Review before continuing.")
                index = len(attempts) + 1
                path = out / "attempts" / f"{index:06d}.json"
                attempt = {"attempt_id": index, "interview_id": interview["interview_id"],
                           "persona_id": interview["persona_id"], "condition": interview["condition"],
                           "question": question, "question_attempt": len(previous) + 1,
                           "timestamp": utc_now(), "status": "started", "request": payload,
                           "accepted": False, "data_origin": mode, "base_url": BASE_URL if live else None}
                save_json(path, attempt)  # Save before dispatch, including a possibly uncertain outcome.
                try:
                    response = transport.complete(payload)
                    value, issue = _answer(response)
                    identity = (response.get("model"), response.get("system_fingerprint")) if isinstance(response, dict) else (None, None)
                    if returned and identity not in returned:
                        issue = "returned_model_or_fingerprint_changed"
                    attempt.update(status="response", response=response, validation_issue=issue,
                                   accepted=issue is None, answer=value if issue is None else None,
                                   fatal=issue not in (None, "invalid_format"))
                    if issue is None:
                        returned.add(identity)
                        accepted = attempt
                except CallError as exc:
                    attempt.update(status="error", error={"http_status": exc.status, "code": exc.code,
                                   "response_body": exc.body, "retry_after": exc.retry_after},
                                   fatal=not _retryable(exc))
                attempt["completed_at"] = utc_now()
                delay = attempt.get("error", {}).get("retry_after")
                delay = max(2 ** len(previous), float(delay or 0))
                attempt["retry_not_before"] = time.time() + delay if accepted is None else 0
                save_json(path, attempt)
                attempts.append(attempt)
                previous.append(attempt)
                if attempt["fatal"]:
                    raise CollectionStopped(f"Attempt {index} needs review. See its saved record; no model was substituted.")
                if live:
                    sleep(0.5)
            values[question] = accepted["answer"]
            selected.append(accepted)
            history += [{"role": "user", "content": c["questions"][question]},
                        {"role": "assistant", "content": accepted["response"]["choices"][0]["message"]["content"]}]
        raw_path = "raw/" + interview["interview_id"] + ".json"
        relevant = [a for a in attempts if a["interview_id"] == interview["interview_id"]]
        raw = {**interview, "data_origin": mode, "model": c["model"] if live else "offline-demonstration",
               "model_version": initial["model_metadata"].get("parent") or initial["model_metadata"]["id"],
               "model_version_scope": "Gateway metadata; an immutable weight revision may be unavailable.",
               "settings": c["settings"], "timestamp": relevant[0]["timestamp"],
               "messages": [{"question": a["question"], "request_messages": a["request"]["messages"],
                             "response_message": a["response"]["choices"][0]["message"],
                             "attempt_id": a["attempt_id"]} for a in selected],
               "retry_history": relevant, "answers": values}
        save_json(out / raw_path, raw)
        records.append({**interview, **values, "raw_file": raw_path, "data_origin": mode})
        save_json(out / "partial_interviews.json", records)
    filename = "interviews.json" if mode == "main" else mode + "_interviews.json"
    save_json(out / filename, records)
    ending = transport.usage() if live else {"cost": 0}
    save_json(out / "usage_after.json", ending)
    files = [plan_path, pre_path, out / filename, out / "usage_after.json"] + list((out / "attempts").glob("*.json")) + list((out / "raw").glob("*.json"))
    summary = {"complete": True, "mode": mode, "data_origin": mode, "timestamp": utc_now(),
               "personas": len(c["personas"]), "interviews": len(records), "attempts": len(attempts),
               "accepted_calls": sum(a["accepted"] for a in attempts),
               "other_attempts": sum(not a["accepted"] for a in attempts), "records_file": filename,
               "observed_key_cost_difference": ending.get("cost", 0) - (start_cost or 0),
               "file_hashes": {p.relative_to(out).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in files}}
    save_json(out / "summary.json", summary)
    return summary


def check_export(output_dir):
    """Check coding and completeness; dry-run and pilot files retain their labels."""
    out = Path(output_dir)
    summary = json.loads((out / "summary.json").read_text())
    records = json.loads((out / summary["records_file"]).read_text())
    blocks = {}
    for row in records:
        sequence, _ = DESIGN[row["condition"]]
        for q in "ABF":
            if q in sequence:
                if type(row[q]) is not int or row[q] not in (0, 1):
                    raise ValueError("An asked question lacks a binary answer.")
            elif row[q] is not None:
                raise ValueError("An unasked question must be null.")
        if row["condition"] in blocks.setdefault(row["persona_id"], set()):
            raise ValueError("Duplicate condition.")
        blocks[row["persona_id"]].add(row["condition"])
        if not (out / row["raw_file"]).is_file():
            raise ValueError("Missing raw record.")
    if len(blocks) < 2 or any(conditions != set(DESIGN) for conditions in blocks.values()):
        raise ValueError("Incomplete persona blocks.")
    return {"mode": summary["mode"], "personas": len(blocks), "interviews": len(records),
            "records_file": str(out / summary["records_file"])}


def budget_estimate(config, pilot_dir):
    """Planning estimate from saved pilot usage, without network calls.

    Uses full input/output rates, ignores cache discounts, and scales the pilot
    by persona count. Failed-call costs and prompt variation can change cost.
    """
    c = validate_config(config)
    out = Path(pilot_dir)
    summary = json.loads((out / "summary.json").read_text())
    before = json.loads((out / "preflight.json").read_text())
    metadata = before["model_metadata"]
    attempts = [json.loads(p.read_text()) for p in (out / "attempts").glob("*.json")]
    usages = [a.get("response", {}).get("usage", {}) for a in attempts]
    complete = all(isinstance(u.get("prompt_tokens"), (int, float)) and
                   isinstance(u.get("completion_tokens"), (int, float)) for u in usages)
    tin = sum(u.get("prompt_tokens", 0) or 0 for u in usages)
    tout = sum(u.get("completion_tokens", 0) or 0 for u in usages)
    pin, pout = metadata.get("input_cost_per_million"), metadata.get("output_cost_per_million")
    factor = len(c["personas"]) / summary["personas"]
    price_known = isinstance(pin, (int, float)) and isinstance(pout, (int, float))
    estimate = (tin * pin + tout * pout) / 1_000_000 * factor if price_known and complete else None
    return {"pilot_mode": summary["mode"], "pilot_attempts": len(attempts),
            "pilot_input_tokens_reported": tin, "pilot_output_tokens_reported": tout,
            "all_attempts_have_token_counts": complete, "main_nominal_calls": 15 * len(c["personas"]),
            "projected_coins_from_tokens": estimate,
            "projected_coins_with_50_percent_planning_allowance": estimate * 1.5 if estimate is not None else None,
            "pilot_observed_key_cost_difference": summary["observed_key_cost_difference"],
            "note": "Planning estimate only. Review prices, failed calls, prompt lengths, and current account balance."}
