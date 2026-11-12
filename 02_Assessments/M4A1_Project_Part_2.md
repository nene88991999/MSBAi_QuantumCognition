# Project Part 2 Audit Report and Client Presentation

M4A1 team report 30 points  |  M4A3 individual defense 5 points  |  Week 4

Run the design you proposed, report what the model produced, and recommend the next action the evidence supports. Explain how your judgment changed from Part 1. A carefully documented small, contradictory, or inconclusive result can earn full credit.

The team report and deck count for 30% of Part 1 and 15% of the full course. Each student’s oral defense counts separately for 5% of Part 1 and 2.5% of the full course. Part 1 covers Modules 1–4 and contributes 50% of the course grade.

## Required Deliverables

1. One team audit report of about 1,500–2,000 words, excluding tables, sources, and logs. Start with the company decision and recommendation, then explain the design, results, rival, evidence tier, and limits that affect the action.

2. An executed notebook with its data and raw-response records, organized in the team’s approved private submission repository. Include a short README explaining how to reproduce the results, the software requirements, and the location of the frozen Part 1 design.

3. One team deck of 6–10 readable slides and a ten-minute team presentation. Each member then completes a separate five-minute oral defense. Include the decision, frames and design, results with uncertainty, rival checks, recommendation, and revision from Part 1.

4. Shared AI Attribution and contribution logs, plus a revision record comparing the final design and interpretation with Part 1. Retain invalid responses, retries, exclusions, and raw outputs so the analysis can be reconstructed.

## Submission and Presentation

One member submits the team report, deck, logs, and executed .ipynb notebook in Canvas by the end of Week 4, listing all team members. Include the repository URL and commit identifier containing the supporting data and raw records. Present at the team’s assigned time in Canvas. Use the approved private repository and give the instructor access. Each student receives a separate oral-defense score.

Use the two required panels from Part 1: the isolated-item baseline and the constructed sequential panel. Add the direct and assessed conditions for interference. Run the Tier 1 practice before analyzing model outputs. If access or data collection fails, document the problem and contact the instructor for an alternative; simulated records must remain labeled Tier 1.

## Analysis and Recommendation

1. Report the model, version, settings, prompts, collection window, persona grid, and valid and excluded counts by condition. Show the two A-by-B answer tables with A in rows and B in columns for each panel. Explain that baseline pairs combine separate calls.

2. Report the difference in F yes rates between A-first and B-first interviews in each panel. For the constructed panel, compute q as the A-first agreement rate minus the B-first agreement rate. Agreement means yes to both frames or no to both frames.

3. Report the direct F rate, the A yes share in the assessed condition, both conditional F rates after A, their weighted average, and interference. Report the bracket endpoints separately. Use the guide’s denominators; F remains the same question in all conditions.

4. Give bootstrap intervals for the main differences, q, interference, and the two direct-minus-conditional contrasts. Keep each interview intact and resample repeated persona records together. State the resampling unit, number of draws, and interval levels. Explain missing or unstable intervals.

5. Compare the main effect and q intervals with the thresholds you set before the run. Distinguish a nonzero interference estimate from a supported bracket violation. State which predictions survive and which remain unresolved. The supplied intervals do not provide a single joint confidence level for the entire verdict.

6. Evaluate the strongest rival using your planned observation or a clearly labeled exploratory check. A small q does not identify a quantum mechanism. A bracket violation challenges fixed response rates carried across procedures; a classical process that changes those rates can remain plausible.

7. Name the evidence tier beside the conclusion. Tier 2 findings describe this model, version, prompts, settings, and persona grid. Recommend an action with an owner and review condition, and describe the human evidence needed before treating the panel as a substitute for customers or employees.

If a conditional group is empty or the sample is too small for a stable interval, report that limitation and narrow the conclusion. Do not invent the missing statistic or change thresholds after seeing the results.

## Team Report and Deck Rubric

| Criterion | Points | Evidence for Full Credit |
| --- | --- | --- |
| Execution and Records | 6 | Follows the frozen design, documents departures, preserves the two panel procedures and extra conditions, and supplies reproducible records. |
| Calculations and Uncertainty | 10 | Uses correct counts and denominators, computes all three statistics and the bracket contrasts, and uses a defensible bootstrap with transparent missing-data treatment. |
| Interpretation and Rival | 7 | Reads the results jointly, applies precommitted thresholds, tests the rival, and keeps model evidence separate from claims about people. |
| Recommendation and Deck | 4 | Connects the evidence to an action, owner, review condition, and next human validation step; presents a clear 6–10 slide deck within ten minutes. |
| Revision and Attribution | 3 | Documents changes from Part 1 and their evidence, with complete AI Attribution and member contribution records. |

Total: 30 points. Score each criterion using the anchors below; half points may be used. The direction of your finding does not affect the score.

Full credit: accurate, complete, and supported. About three quarters: sound reasoning with a minor omission. About half: a substantial omission or error weakens the argument. About one quarter: a relevant attempt with little support. Zero: absent or unrelated. Apply these anchors within each criterion, rather than counting words mechanically.

This 30-point rubric determines the shared team score, worth 15% of the full course.

## Individual Oral Defense Rubric

Each member answers questions about the entire audit, including the design, calculations, uncertainty, and recommendation. Prepare beyond your assigned task. Respond without live AI assistance or answers supplied by teammates. The instructor directs comparable core questions to each student and may follow up on the team’s actual evidence. The team submission score and each student’s defense score are recorded separately.

Allow ten minutes per team plus five minutes per member. For example, three teams with four members each require 90 minutes. Larger cohorts or teams need additional scheduled blocks. Canvas specifies the presentation and individual-defense slots.

| Criterion | Points | Evidence for Full Credit |
| --- | --- | --- |
| Design and Records | 2 | Explains the team’s questions, six conditions, controls, and response records accurately. |
| Calculations and Uncertainty | 2 | Reconstructs a calculation and explains its denominator, resampling unit, and uncertainty. |
| Interpretation and Action | 1 | Defends the recommendation with the evidence, identifies a credible rival, and states the scope of the claim. |

Total: 5 points. Score each criterion using the anchors below; half points may be used. The direction of your finding does not affect the score.

Full credit: accurate, complete, and supported. About three quarters: sound reasoning with a minor omission. About half: a substantial omission or error weakens the argument. About one quarter: a relevant attempt with little support. Zero: absent or unrelated. Apply these anchors within each criterion, rather than counting words mechanically.

Score each student’s own answers separately under M4A3. This five-point rubric is worth 2.5% of the full course. It is additional to the shared 30-point M4A1 team score. Both sets of instructions are kept in this Project Part 2 brief.

## Use of AI

AI Assessment Scale level 4. The model is the subject of the audit. Disclose AI assistance with analysis or writing and verify the final work. The oral defense is level 0: answer the questions yourself without live AI assistance.

Learning objectives: M3LO3, M3LO4, M4LO1, M4LO2, M4LO3, and M4LO4.
