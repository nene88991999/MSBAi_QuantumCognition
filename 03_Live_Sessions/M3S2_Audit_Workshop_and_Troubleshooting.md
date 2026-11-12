# M3S2: Audit Workshop and Troubleshooting

**Preparation:** Complete M3A2 individually. Bring that executed notebook and your team’s frozen proposal, collection records, and Project Part 2 brief.

**Session Output:** A checked team collection, executed analysis or documented blocker, a draft evidence table, and assigned follow-up responsibilities.

This 90-minute meeting assumes the videos have been watched. Use the activities to develop your individual work and team project. Follow the assessment brief for submission requirements.

**Assessment Connections:** [M3A2_Audit_Practice](../02_Assessments/M3A2_Audit_Practice.md), [M4A1_Project_Part_2](../02_Assessments/M4A1_Project_Part_2.md)

## Meeting Plan

| Activity | Minutes |
| --- | ---: |
| The Practice Result | 5 |
| A Missing Condition in the Collection | 15 |
| Estimates Across Repeated Samples | 20 |
| The Rare Subgroup Limits Precision | 15 |
| Peer Critique of the Evidence | 15 |
| The Result Paragraph | 10 |
| Remaining Work | 10 |

## Slide 1: Audit Workshop and Troubleshooting

Quantum Cognition for Human-AI Decision Teaming

Nathan Yang

M3S2

### Discussion and Work

This meeting assumes that students have watched the module videos. Use the session for application and assessment progress.

## Slide 2: The Practice Result

Did the calculation recover the simulator’s pattern?

How did the smaller sample change the intervals?

Which warning needs attention?

### Discussion and Work

Students compare estimates with known population values in their own run. A small sample can leave a decision unresolved even when the code is correct. Do not alter seeds until a preferred finding appears.

## Slide 3: A Missing Condition in the Collection

What must be resolved before calculating the paired comparison?

Toy excerpt: two of the six conditions; one repetition per persona.

| Persona | Constructed ABF | Constructed BAF |
| --- | --- | --- |
| P01 | F = Yes | F = No |
| P02 | F = No | Missing |
| P03 | F = Yes | F = Yes |

### Discussion and Work

This small record excerpt is a debugging exercise, not a dataset to analyze. Missing is not No. Inspect the full six-condition collection, distinguish failed calls from refusals and parser errors, and follow the frozen inclusion rule. Do not silently drop or impute a record. Preserve raw responses and count denominators explicitly. Students verify their own collection with the supplied audit code.

## Slide 4: Estimates Across Repeated Samples

Where does your reported uncertainty come from?

5,000 simulations: 100 independent responses per arm; true rates 0.60 and 0.50.

| Difference in percentage points (5-point bin midpoints) | Simulated samples |
| --- | ---: |
| -17.5 | 0 |
| -12.5 | 11 |
| -7.5 | 57 |
| -2.5 | 258 |
| 2.5 | 755 |
| 7.5 | 1193 |
| 12.5 | 1398 |
| 17.5 | 859 |
| 22.5 | 366 |
| 27.5 | 92 |
| 32.5 | 9 |
| 37.5 | 2 |

**Units:** Simulated samples. Values for percentage-formatted rate charts are stored as proportions (0.64 means 64%).

### Discussion and Work

This is a sampling simulation, not a bootstrap of collected data. In each of 5,000 repetitions, independently draw two binomial counts with n=100 and probabilities 0.60 and 0.50, then subtract the rates. NumPy default_rng seed 20261111. Five-point bins are left-closed, right-open except the last. The true difference is 10 percentage points. The audit instead resamples complete observed persona blocks to preserve dependence. Students run their notebook and verify counts, q, the focal difference, and bracket diagnostics against raw records. Simulation source and counts are provided in source/sessions.json.

## Slide 5: The Rare Subgroup Limits Precision

Which conditional rate will be less precise?

Imposed counts: 100 assessed records divided by the first answer.

| Category | Assessed records |
| --- | ---: |
| A = Yes | 90 |
| A = No | 10 |

**Units:** Records in the assessed arm. Values for percentage-formatted rate charts are stored as proportions (0.64 means 64%).

### Discussion and Work

A conditional rate computed from ten records generally has less information than one computed from ninety, holding the response variance and dependence structure comparable. Here both subgroup counts are imposed. Empty groups can make a conditional rate or bracket unavailable. More bootstrap draws do not create additional observations. Students inspect subgroup sizes, invalid records, and the inclusion rules before interpreting an uncertain result.

## Slide 6: Peer Critique of the Evidence

Does each estimate have a clear denominator?

Does the interval preserve the sampling structure?

Does the interpretation stay within Tier 2?

### Discussion and Work

Exchange a summary table without sharing private or unnecessary raw records. Use the Part 2 rubric to identify one claim to narrow or one check to strengthen.

## Slide 7: The Result Paragraph

State the tested model, procedure, and outcome.

Report magnitude and uncertainty together.

Connect the finding to a proposed action.

### Discussion and Work

Draft the report using actual results or explicitly mark a workflow draft if collection is incomplete. Explain the strongest alternative near the interpretation it limits.

## Slide 8: Remaining Work

Save the team notebook, records, and evidence table.

Assign the next task and a member to check it.

Each member prepares to explain the full audit.

### Discussion and Work

The report and deck are shared team work. Preserve the original design and document revisions and contributions. Each student’s oral defense is graded separately. Consult Canvas and M4A1 for the required submissions and schedule.
