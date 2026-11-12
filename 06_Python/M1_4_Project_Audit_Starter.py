# %% [markdown]
# # Project Audit Starter
# 
# **M2A2 and M4A1 · Modules 1–4**
# 
# Analyze the records from your two panels and the extra direct and assessed conditions. This notebook supports the six-condition matched design in the Project Templates and Collection Guide. It checks records and reports counts, the order effect, q, interference, and bracket contrasts with uncertainty.
# 
# The default run is a **Tier 1 simulation demonstration** so the notebook works without API access. It is not a completed Tier 2 project. No cell calls an AI provider or incurs usage charges. Collect model responses separately using the course-approved tool, then save the required records and raw messages.
# 
# **Your decision and frozen design:** [Name the company decision and link the dated Part 1 design.]

# %% [markdown]
# ## Team Project and Individual Oral Defense
# Work in your assigned team and submit one executed notebook with the team report and deck. Record each member’s contribution and who checked the work. Every member should understand the full audit and prepare to explain its design, calculations, uncertainty, and recommendation in an individual oral defense.
# 
# The team report and deck carry 30% of Part 1, equal to 15% of the full course. The individual oral defense carries 5% of Part 1, equal to 2.5% of the full course. Keep the team’s records in the approved private submission location.

# %% [markdown]
# ## Load the Analysis Functions
# 
# Run the next cell once. It rejects missing conditions, invalid binary coding, duplicate interviews, and incomplete persona blocks. It resamples all six records for each selected persona together. Arrange a different analysis with the instructor if your approved design differs.

# %%
"""Self-contained instructional audit functions embedded in the two notebooks."""
import json
import csv
from pathlib import Path
import numpy as np

CONDITIONS = ['isolated_AB', 'isolated_BA', 'constructed_AB',
              'constructed_BA', 'direct', 'assessed']
QUESTIONS = ['A', 'B', 'F']
ANGLES = {'A': 40.0, 'B': 62.5, 'F': 0.0}
STATE_ANGLE = 22.5
LABELS = {
    'isolated_main': 'Isolated F order difference',
    'isolated_q': 'Isolated stitched-pair q',
    'main': 'Constructed F order difference',
    'q': 'Constructed q',
    'direct': 'Direct F rate',
    'weight': 'Assessed A yes weight',
    'r_yes': 'F rate after A yes',
    'r_no': 'F rate after A no',
    'weighted': 'Weighted assessed rate',
    'interference': 'Direct minus weighted rate',
    'gap_yes': 'Direct minus A yes conditional rate',
    'gap_no': 'Direct minus A no conditional rate',
}

def probability_yes(state_angle, question_angle):
    return np.cos(np.deg2rad(state_angle-question_angle))**2

def geometric_sequence(rng, n, sequence):
    state = np.full(n, STATE_ANGLE)
    answers = {}
    for item in sequence:
        angle = ANGLES[item]
        yes = rng.random(n) < probability_yes(state, angle)
        answers[item] = yes.astype(int)
        state = np.where(yes, angle, angle+90)
    return answers

def geometric_population(sequence):
    paths = [({}, STATE_ANGLE, 1.0)]
    for item in sequence:
        expanded = []
        for answers, state, mass in paths:
            p = float(probability_yes(state, ANGLES[item]))
            for yes, prob in [(1,p),(0,1-p)]:
                expanded.append(({**answers,item:yes}, ANGLES[item]+90*(1-yes), mass*prob))
        paths = expanded
    assert abs(sum(x[2] for x in paths)-1) < 1e-12
    return [(a,p) for a,_,p in paths]

def population_values(regime):
    if regime == 'fixed_joint':
        direct, w, r1, r0, main, q = .58, .6, .7, .4, 0., 0.
    elif regime == 'geometric':
        ab,ba = geometric_population('ABF'),geometric_population('BAF')
        main = sum(p*a['F'] for a,p in ab)-sum(p*a['F'] for a,p in ba)
        q = sum(p*(a['A']==a['B']) for a,p in ab)-sum(p*(a['A']==a['B']) for a,p in ba)
        direct = float(probability_yes(STATE_ANGLE, ANGLES['F']))
        w = float(probability_yes(STATE_ANGLE, ANGLES['A']))
        r1 = float(probability_yes(ANGLES['A'], ANGLES['F']))
        r0 = float(probability_yes(ANGLES['A']+90, ANGLES['F']))
    else:
        raise ValueError('Use fixed_joint or geometric.')
    weighted = w*r1+(1-w)*r0
    return dict(isolated_main=0.,isolated_q=0.,main=main,q=q,direct=direct,
                weight=w,r_yes=r1,r_no=r0,weighted=weighted,
                interference=direct-weighted,gap_yes=direct-r1,gap_no=direct-r0)

def simulate_records(regime, n=2000, seed=20261110):
    """One independent simulated block per persona ID; six interviews per block."""
    rng = np.random.default_rng(seed)
    blocks = {}
    for condition in CONDITIONS:
        sequence = ('ABF' if condition.endswith('AB') else 'BAF')
        if condition == 'direct': sequence='F'
        if condition == 'assessed': sequence='AF'
        if regime == 'fixed_joint':
            a = (rng.random(n)<.6).astype(int)
            b = (rng.random(n)<np.where(a==1,.8,.3)).astype(int)
            f = (rng.random(n)<np.where(a==1,.7,.4)).astype(int)
            full = {'A':a,'B':b,'F':f}
            if condition.startswith('isolated'):
                full = {k:(rng.random(n)<p).astype(int) for k,p in [('A',.6),('B',.6),('F',.58)]}
            answers = {q:full[q] for q in sequence}
        elif regime == 'geometric':
            if condition.startswith('isolated'):
                answers = {q:(rng.random(n)<probability_yes(STATE_ANGLE,ANGLES[q])).astype(int) for q in sequence}
            else:
                answers = geometric_sequence(rng,n,sequence)
        else:
            raise ValueError('Unknown simulator.')
        blocks[condition]=answers
    records=[]
    for i in range(n):
        for condition in CONDITIONS:
            records.append(dict(interview_id=f'sim_{regime}_{i:05d}_{condition}',
                persona_id=f'sim_{i:05d}', condition=condition,
                **{q:int(blocks[condition][q][i]) if q in blocks[condition] else None for q in QUESTIONS},
                raw_file=None))
    return records

def validate_records(records, require_raw=False, base_dir='.'):
    """Reject incomplete blocks, duplicates, bad coding, and unrecorded responses."""
    if not isinstance(records,list) or not records:
        raise ValueError('Input must be a nonempty JSON list of interview records.')
    blocks={}; interviews=set()
    for row in records:
        for key in ['interview_id','persona_id','condition','A','B','F','raw_file']:
            if key not in row: raise ValueError(f'Missing field {key}.')
        iid, pid, condition = row['interview_id'],row['persona_id'],row['condition']
        if not isinstance(iid,str) or not iid or iid in interviews:
            raise ValueError(f'Invalid or duplicate interview ID: {iid}')
        if not isinstance(pid,str) or not pid: raise ValueError('Persona ID must be nonempty text.')
        if condition not in CONDITIONS: raise ValueError(f'Unknown condition: {condition}')
        interviews.add(iid)
        if condition in blocks.setdefault(pid,{}): raise ValueError(f'Duplicate {pid}, {condition}.')
        expected = set('F') if condition=='direct' else set('AF') if condition=='assessed' else set('ABF')
        for question in QUESTIONS:
            value=row[question]
            if question in expected:
                if type(value) is not int or value not in [0,1]:
                    raise ValueError(f'{iid}: {question} must be integer 0 or 1, not a missing value.')
            elif value is not None: raise ValueError(f'{iid}: unasked {question} must be null.')
        if require_raw:
            if not row['raw_file']: raise ValueError(f'{iid}: raw_file is required for model data.')
            raw_path=(Path(base_dir)/row['raw_file']).resolve()
            if not raw_path.is_file(): raise ValueError(f'Raw record missing: {raw_path}')
            raw=json.loads(raw_path.read_text())
            for key in ['model','model_version','settings','timestamp','messages','retry_history']:
                if key not in raw: raise ValueError(f'{raw_path.name} is missing {key}.')
            if not isinstance(raw['messages'],list) or not raw['messages']:
                raise ValueError(f'{raw_path.name}: complete messages are required.')
        blocks[pid][condition]=row
    ids=sorted(blocks)
    if len(ids)<2: raise ValueError('At least two complete persona blocks are required.')
    for pid in ids:
        if set(blocks[pid])!=set(CONDITIONS):
            raise ValueError(f'{pid} is missing a condition. Document and resolve attrition before analysis.')
    data=np.array([[[blocks[pid][c][q] if blocks[pid][c][q] is not None else np.nan
                     for q in QUESTIONS] for c in CONDITIONS] for pid in ids],dtype=float)
    return data,ids

def statistics(data):
    def rate(c,q): return float(data[:,c,q].mean())
    def agreement(c): return float((data[:,c,0]==data[:,c,1]).mean())
    assessed=data[:,5,:]
    yes=assessed[:,0]==1; no=~yes
    r1=float(assessed[yes,2].mean()) if yes.any() else np.nan
    r0=float(assessed[no,2].mean()) if no.any() else np.nan
    direct=rate(4,2); weighted=rate(5,2)
    # The weighted decomposition equals the pooled assessed F rate.
    if yes.any() and no.any():
        assert abs(weighted-(yes.mean()*r1+no.mean()*r0))<1e-10
    return dict(isolated_main=rate(0,2)-rate(1,2), isolated_q=agreement(0)-agreement(1),
        main=rate(2,2)-rate(3,2),q=agreement(2)-agreement(3),direct=direct,
        weight=float(yes.mean()),r_yes=r1,r_no=r0,weighted=weighted,
        interference=direct-weighted,gap_yes=direct-r1,gap_no=direct-r0)

def analyze(data, reps=1200, seed=4711):
    if reps<200: raise ValueError('Use at least 200 bootstrap draws; 1200 is the teaching default.')
    point=statistics(data); keys=list(point)
    draws=np.empty((reps,len(keys)))
    rng=np.random.default_rng(seed)
    for b in range(reps):
        # Select whole persona blocks. Every question and all six conditions stay linked.
        sampled=data[rng.integers(0,len(data),size=len(data))]
        values=statistics(sampled)
        draws[b]=[values[k] for k in keys]
    result={}
    for j,k in enumerate(keys):
        valid=np.isfinite(draws[:,j]); level=.975 if k in ['gap_yes','gap_no'] else .95
        # Do not silently discard bootstrap draws with empty conditional groups.
        if valid.all() and np.isfinite(point[k]):
            alpha=(1-level)/2
            lo,hi=np.quantile(draws[:,j],[alpha,1-alpha])
            interval=[float(lo),float(hi)]
        else: interval=None
        result[k]={'estimate':float(point[k]) if np.isfinite(point[k]) else None,
                   'interval':interval,'level':level,'valid_draws':int(valid.sum()),'draws':reps}
    return result

def interval_branch(result, threshold):
    ci=result['interval']
    if ci is None: return 'unresolved; interval unavailable'
    lo,hi=ci
    if lo>=-threshold and hi<=threshold: return 'within the prespecified range'
    if lo>threshold: return 'above the prespecified range'
    if hi<-threshold: return 'below the prespecified range'
    return 'unresolved relative to the prespecified range'

def bracket_branch(result):
    cis=[result[k]['interval'] for k in ['gap_yes','gap_no']]
    if any(x is None for x in cis): return 'unresolved; a conditional interval is unavailable'
    if all(x[0]>0 for x in cis): return 'direct rate above both conditional rates'
    if all(x[1]<0 for x in cis): return 'direct rate below both conditional rates'
    if (cis[0][0]>0 and cis[1][1]<0) or (cis[0][1]<0 and cis[1][0]>0):
        return 'direct rate between the two conditional rates'
    return 'unresolved relative to at least one endpoint'

def quality_notes(data):
    notes=[]
    n1=int(data[:,5,0].sum());n0=len(data)-n1
    if min(n1,n0)<10:
        notes.append('A conditional assessed group has fewer than 10 records. Treat percentile intervals with care and discuss additional data.')
    for c,name in enumerate(CONDITIONS):
        if data[:,c,2].mean() in [0.,1.]:
            notes.append(f'{name}: all F answers are identical. A degenerate bootstrap interval does not establish certainty.')
    for label,value in [('A yes',data[data[:,5,0]==1,5,2]),('A no',data[data[:,5,0]==0,5,2])]:
        if len(value) and value.mean() in [0.,1.]:
            notes.append(f'Conditional {label}: no observed F variation; the percentile interval may be unreliable.')
    return notes

def show_tables(data):
    print('Counts by condition; each row is one complete interview')
    print(f'Personas: {len(data)}; interviews: {len(data)*6}')
    for c,name in enumerate(CONDITIONS):
        print(f'{name:17s} n={len(data):5d} F yes={int(data[:,c,2].sum()):5d}')
    print(f'Assessed A yes n={int(data[:,5,0].sum())}; A no n={int((data[:,5,0]==0).sum())}')
    for c in range(4):
        counts=[[int(((data[:,c,0]==a)&(data[:,c,1]==b)).sum()) for b in [1,0]] for a in [1,0]]
        print(f'\n{CONDITIONS[c]}: A rows [yes,no], B columns [yes,no]')
        print(np.array(counts))

def show_results(result, main_threshold=.05, q_tolerance=.05, truth=None):
    print('Rates and differences are on the 0–1 scale; multiply differences by 100 for percentage points.')
    for k,r in result.items():
        v='unavailable' if r['estimate'] is None else f"{r['estimate']:.4f}"
        ci='unavailable' if r['interval'] is None else f"[{r['interval'][0]:.4f}, {r['interval'][1]:.4f}]"
        population='' if truth is None else f' | population {truth[k]:.4f}'
        print(f'{LABELS[k]}: {v} | {100*r["level"]:g}% {ci}{population}')
    print('\nConstructed main effect:',interval_branch(result['main'],main_threshold))
    print('Constructed q:',interval_branch(result['q'],q_tolerance))
    print('Bracket comparison:',bracket_branch(result))
    print('These branches describe the tested process. They do not identify a mechanism or validate human representativeness.')

def export_results(folder,result,metadata):
    folder=Path(folder);folder.mkdir(parents=True,exist_ok=True)
    (folder/'audit_results.json').write_text(json.dumps({'metadata':metadata,'statistics':result},indent=2,allow_nan=False))
    with (folder/'audit_results.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['quantity','estimate','interval_low','interval_high','level','valid_draws','draws'])
        for k,r in result.items():
            bounds=r['interval'] if r['interval'] is not None else [None,None]
            w.writerow([k,r['estimate'],*bounds,r['level'],r['valid_draws'],r['draws']])
    print('Saved result files to',folder)


# %% [markdown]
# ## Set the Analysis Mode and Prespecified Rules
# 
# For your project, change `MODE` to `model_data`, provide your JSON filename and metadata, and enter the thresholds from your frozen proposal. The data file is a list of records containing `interview_id`, `persona_id`, `condition`, `A`, `B`, `F`, and `raw_file`. Use 0 or 1 for asked questions and null for unasked ones. All six exact condition codes are listed in `CONDITIONS` above.
# 
# Every raw interview JSON file must include `model`, `model_version`, `settings`, `timestamp`, `messages`, and `retry_history`. The messages list should preserve roles and content for every prompt and reply. The notebook verifies that those files and fields exist; you remain responsible for checking that coding matches the raw answers.
# 
# One complete interview per persona per condition is the starter design. Keep a log of any excluded persona blocks. Report the original and retained counts in your report.

# %%
MODE = 'demonstration'  # Use 'model_data' for your collected Tier 2 records.
DATA_FILE = 'my_model_interviews.json'
MAIN_THRESHOLD = 0.05  # Replace with the frozen proposal's meaningful difference.
QQ_TOLERANCE = 0.05   # Replace with the frozen proposal's tolerance for q.
BOOTSTRAP_DRAWS = 1200
BOOTSTRAP_SEED = 4711
MODEL_METADATA = {
    'provider': '', 'model': '', 'model_version': '', 'settings': {},
    'collection_window': '', 'prompt_version': '', 'persona_grid_file': '',
    'frozen_proposal_file': '', 'exclusion_log_file': ''
}
assert 0 < MAIN_THRESHOLD < 1 and 0 < QQ_TOLERANCE < 1

if MODE == 'demonstration':
    records = simulate_records('geometric',2000,20261110)
    data, persona_ids = validate_records(records)
    evidence_tier = 1
    output_folder = Path('audit_outputs/project_demonstration')
    output_folder.mkdir(parents=True,exist_ok=True)
    example = simulate_records('geometric',8,20261110)
    (output_folder/'SIMULATED_data_format_example.json').write_text(json.dumps(example,indent=2))
    print('TIER 1 SIMULATED DEMONSTRATION. Replace these records before a Tier 2 submission.')
elif MODE == 'model_data':
    if any(value in ['',{},None] for value in MODEL_METADATA.values()):
        raise ValueError('Complete all MODEL_METADATA entries, including paths to the frozen proposal and exclusion log.')
    for key in ['persona_grid_file','frozen_proposal_file','exclusion_log_file']:
        if not Path(MODEL_METADATA[key]).is_file(): raise ValueError(f'Missing {key}.')
    input_path = Path(DATA_FILE)
    records = json.loads(input_path.read_text())
    data, persona_ids = validate_records(records,require_raw=True,base_dir=input_path.parent)
    evidence_tier = 2
    output_folder = Path('audit_outputs/project_model_data')
    print('TIER 2 MODEL RESPONSES. Interpretation is limited to the recorded model setup.')
else:
    raise ValueError('MODE must be demonstration or model_data.')


# %% [markdown]
# ## Inspect the Records and Counts
# 
# Check one record against its saved raw interview. Verify that A and B retain their names in both orders. In a constructed interview, the actual earlier questions and answers must remain in context. In an isolated condition, each question starts fresh.

# %%
print(json.dumps(records[0],indent=2))
show_tables(data)
notes = quality_notes(data)
print('\nData quality notes:')
for note in notes or ['No listed warning. Inspect the raw records and collection log as well.']:
    print('-',note)


# %% [markdown]
# ## Calculate the Audit
# 
# The F difference compares A-first with B-first. The q calculation compares their agreement rates. Interference compares F alone with the weighted assessed rate; with these same assessed records, that weighted rate equals the overall assessed F rate.
# 
# The bracket calculation compares the direct rate with both conditional rates. The 97.5% intervals for these two contrasts implement an approximate Bonferroni adjustment. Other intervals are 95% pointwise intervals. The full set does not have a single joint 95% interpretation.

# %%
results = analyze(data,BOOTSTRAP_DRAWS,BOOTSTRAP_SEED)
show_results(results,MAIN_THRESHOLD,QQ_TOLERANCE)
metadata = {
    'evidence_tier':evidence_tier, 'mode':MODE, 'personas_retained':len(persona_ids),
    'interviews_retained':len(records), 'main_threshold':MAIN_THRESHOLD,
    'q_tolerance':QQ_TOLERANCE,'bootstrap_draws':BOOTSTRAP_DRAWS,
    'bootstrap_seed':BOOTSTRAP_SEED,'resampling_unit':'complete six-condition persona block',
    'model_metadata':MODEL_METADATA if evidence_tier==2 else None,'quality_notes':notes
}
export_results(output_folder,results,metadata)


# %% [markdown]
# ## Interpret the Joint Pattern
# 
# **Your results:** [State the main effect, q, interference, and bracket result. Report rates, intervals, and counts with the correct denominators. Use the frozen thresholds. Explain any unavailable or unreliable interval.]
# 
# **Your strongest rival:** [State its prediction, the observation or comparison you used, the result, and what remains unresolved. Identify checks added after seeing the results as exploratory.]
# 
# **Your evidence tier:** [Name the tested model, version, settings, prompts, and persona grid. Describe the human study needed to evaluate whether the pattern occurs in the people relevant to the decision.]
# 
# A q interval within tolerance checks one restriction. It does not identify a unique mechanism. A bracket violation challenges fixed conditional rates carried across procedures. Process-dependent classical explanations can remain plausible. Isolated-panel answer pairs combine separate calls and have a different interpretation from sequential pairs.

# %% [markdown]
# ## Recommendation and Revision
# 
# **Recommendation:** [State the company action, responsible owner, supporting evidence, and condition for reconsidering the action. A small or unresolved effect can support further testing or retention of the current process.]
# 
# **Revision from Part 1:** [Identify a changed or retained claim, the evidence prompting the decision, and whether any design changes preceded or followed the relevant results.]
# 
# **Reproducibility:** [Link the raw records, persona grid, frozen proposal, exclusion log, AI Attribution Log, and revision record. Add a README with rerun steps and record the submitted repository commit.]
# 
# Before submission, confirm that the notebook is in the intended evidence tier and that the output reflects your actual records. Save the executed notebook with the report and 6–10 slide deck. The oral defense is completed without live AI assistance.
