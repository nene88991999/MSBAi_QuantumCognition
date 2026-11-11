# %% [markdown]
# # Audit Notebook Practice
# 
# **M3A2 · Individual · Ungraded · Before Project Studio 3**
# 
# Check an audit on two simulated processes before using it on model-generated responses. Both datasets below are **Tier 1 simulations**. They contain no human or language-model data. The notebook runs offline with Python and NumPy and makes no paid API calls.
# 
# Open this notebook in Colab, Jupyter, or VS Code. Run the cells in order. Complete the response sections, retain the outputs, and submit your executed `.ipynb` file. The companion Word brief provides the full instructions and hand-calculation exercise.
# 
# Every simulated persona ID identifies an independent block of six interviews. The bootstrap resamples these complete blocks, retaining all answers and conditions. In a project, repeated persona descriptions can create dependence, so the sampling unit must follow the collection design.

# %% [markdown]
# ## Predictions Before Running
# 
# The fixed-joint simulator gives A, B, and F one common probability distribution that does not change with order. The geometric simulator applies the model introduced in the lectures: each question changes the simulated state before the next response is drawn. The geometric model has the QQ restriction built into its probabilities. A sequential interview with an actual language model need not follow that model.
# 
# **Your prediction:** [Write two or three sentences about the main effect, q, interference, and bracket.]

# %% [markdown]
# ## Analysis Functions
# 
# Run the next cell once. You may collapse it afterward. The functions keep the names A and B fixed when the order changes, check complete records, and preserve the six-condition block in every bootstrap draw. You do not need to rewrite the functions.

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
# ## Settings Fixed Before the Run
# 
# The meaningful main-effect threshold and the QQ tolerance are separate choices. Both are set to five percentage points here for practice. A value of 0.05 on the calculation scale means five percentage points. The large sample is computationally cheap because it is simulated; it does not prescribe a paid model-collection budget.

# %%
N = 2000
BOOTSTRAP_DRAWS = 1200
SIMULATION_SEED = 20261110
BOOTSTRAP_SEED = 4711
MAIN_THRESHOLD = 0.05
QQ_TOLERANCE = 0.05
for regime in ['fixed_joint', 'geometric']:
    print('\nPopulation benchmarks:', regime)
    for key in ['main','q','direct','weight','r_yes','r_no','weighted','interference']:
        print(f'{key:15s} {population_values(regime)[key]: .6f}')


# %% [markdown]
# ## Run the Fixed Joint Simulator
# 
# Check the group sizes and paired answer tables first. The isolated panel asks each question separately. Its A-B pairs are stitched together from separate calls. The constructed panel retains all answers in sequence, although this simulator's fixed joint distribution makes order irrelevant in the population.

# %%
fixed_records = simulate_records('fixed_joint', N, SIMULATION_SEED)
fixed_data, fixed_ids = validate_records(fixed_records)
show_tables(fixed_data)
fixed_result = analyze(fixed_data, BOOTSTRAP_DRAWS, BOOTSTRAP_SEED)
show_results(fixed_result, MAIN_THRESHOLD, QQ_TOLERANCE, population_values('fixed_joint'))
print('Data quality notes:', quality_notes(fixed_data) or ['No listed warning in this run.'])
export_results('audit_outputs/practice_fixed_joint', fixed_result,
               {'evidence_tier':1,'generator':'fixed_joint','N_per_condition':N,
                'simulation_seed':SIMULATION_SEED,'bootstrap_seed':BOOTSTRAP_SEED,
                'resampling_unit':'complete six-condition persona block'})


# %% [markdown]
# ## Run the Geometric Simulator
# 
# This simulator uses state angle 22.5 degrees and question angles A = 40, B = 62.5, and F = 0 degrees. You do not need to calculate angles by hand. They define a known process against which to check the estimator. The direct condition asks F alone; the assessed condition asks A and then F.

# %%
geometric_records = simulate_records('geometric', N, SIMULATION_SEED)
geometric_data, geometric_ids = validate_records(geometric_records)
show_tables(geometric_data)
geometric_result = analyze(geometric_data, BOOTSTRAP_DRAWS, BOOTSTRAP_SEED)
show_results(geometric_result, MAIN_THRESHOLD, QQ_TOLERANCE, population_values('geometric'))
print('Data quality notes:', quality_notes(geometric_data) or ['No listed warning in this run.'])
export_results('audit_outputs/practice_geometric', geometric_result,
               {'evidence_tier':1,'generator':'geometric','N_per_condition':N,
                'simulation_seed':SIMULATION_SEED,'bootstrap_seed':BOOTSTRAP_SEED,
                'resampling_unit':'complete six-condition persona block'})


# %% [markdown]
# ## Read the Intervals
# 
# The main statistics use 95% pointwise percentile intervals. The two direct-minus-conditional contrasts use 97.5% intervals, an approximate Bonferroni adjustment for checking both bracket endpoints. Both intervals must lie above zero to support a direct rate above the bracket, or both below zero to support a rate below it. A missing interval means that a conditional group was empty in at least one bootstrap draw; it is not replaced with a zero.
# 
# An interval entirely within the q tolerance supports a practically small departure from that restriction. An interval that merely contains zero may still be too wide. These intervals do not form a single joint 95% test for the full verdict. Check warnings about sparse groups or identical responses before relying on the interval.
# 
# **Your interpretation:** [Report the main effect, q, interference, and bracket for both simulators. Compare estimates with the population benchmarks. If a branch is unresolved, explain why.]

# %% [markdown]
# ## Repeat With a Smaller Sample
# 
# Keep the thresholds fixed. This comparison uses a new simulated sample of 100 interviews in each condition. Explain what the interval widths permit you to conclude.

# %%
small_results = {}
for regime in ['fixed_joint','geometric']:
    small_data, _ = validate_records(simulate_records(regime,100,SIMULATION_SEED))
    small_results[regime] = analyze(small_data,BOOTSTRAP_DRAWS,BOOTSTRAP_SEED)
    print('\nSMALL SAMPLE:',regime)
    show_results(small_results[regime],MAIN_THRESHOLD,QQ_TOLERANCE)
    print('Data quality notes:', quality_notes(small_data) or ['No listed warning in this run.'])


# %% [markdown]
# ## Responses and Hand Calculation
# 
# Complete about 250–400 words across the response sections, excluding arithmetic.
# 
# 1. **Smaller sample:** [Which conclusions changed, and why? Explain why an interval containing zero is different from an interval entirely within tolerance.]
# 2. **Hand calculation from the Word brief:** [Show the F order effect, both agreement rates, q, assessed weights and conditional rates, weighted prediction, interference, and bracket. Keep the denominators visible.]
# 3. **Evidence tier:** [What would this analysis establish if the records came from a named language model? What would a study with people need to establish before the company could rely on the model as a substitute?]
# 4. **Question for Project Studio 3:** [Write one calculation or design question.]
# 5. **AI disclosure:** [Identify any help with understanding or debugging, or state that you did not use AI.]
# 
# Save the notebook with outputs and your responses. The JSON and CSV result files are optional supporting files; the executed notebook is the required practice submission.

# %% [markdown]
# ## References
# 
# The QQ restriction is discussed in [Wang, Solloway, Shiffrin, and Busemeyer (2014)](https://doi.org/10.1073/pnas.1407756111). This notebook follows the course's agreement-rate sign convention. [NIST's bootstrap documentation](https://www.itl.nist.gov/div898/software/dataplot/refman1/auxillar/bootplot.htm) describes resampling with replacement and preserving paired observations. The simulators and decision thresholds here are instructional choices.
