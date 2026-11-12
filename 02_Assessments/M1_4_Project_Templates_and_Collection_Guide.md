# Project Templates and Collection Guide

Companion to M2A2 and M4A1  |  Editable Working Templates

Use these shared team templates to turn a company decision into a reproducible audit. Replace the response prompts with your own work. The six-condition design below matches the supplied Project Audit Starter notebook and keeps the additional interference comparison explicit.

## Team and Individual Responsibilities

Use the team assigned in Canvas. Submit one proposal, report, deck, executed project notebook, and set of supporting records per team. Each student completes the three discussions, Module 3 practice, oral defense, and reflection individually. The proposal and report receive shared team scores; oral-defense and reflection scores reflect each student’s work.

## Proposal Template

### Company Decision

State the company, the decision owner, the choice to be made, and the measurable outcome. Explain what public evidence establishes the setting. Response: [write here].

### Research Question and Population

State what you want to learn about the questioning process. Identify the people relevant to the eventual business decision and why model responses could help prepare a human study. Response: [write here].

### Frames and Questions

Explain why frame A and frame B matter in this setting. Give the exact background facts and the exact wording of A, B, and F. Each question must have a clear yes-or-no answer. Define yes as 1 and no as 0, or document a different fixed coding. Response: [write here].

### Prediction and Rival

State the direction you predict for F when A and B are reversed. Name the strongest rival, what else it predicts, and the comparison or observation you will use to examine it. Response: [write here].

### Decision Rules

Record the meaningful F difference and the q tolerance in percentage points. State the planned action for a small precise result, a meaningful result, a failed model prediction, and an unresolved result. Response: [write here].

## Six Conditions for the Audit

A and B are the two framing questions; F is the final decision question. Every condition receives the same background information and uses the same coding. Each persona has a fresh interview in every condition. Randomize the run schedule so condition is not confounded with time or model changes.

| Condition Code | Procedure | Role |
| --- | --- | --- |
| isolated_AB | A, B, and F in three fresh conversations | Baseline with an A-first label |
| isolated_BA | B, A, and F in three fresh conversations | Baseline with a B-first label |
| constructed_AB | A then B then F, retaining earlier answers | A-first sequential interview |
| constructed_BA | B then A then F, retaining earlier answers | B-first sequential interview |
| direct | F alone in a fresh conversation | Direct decision rate |
| assessed | A then F, retaining the A answer | Weights and conditional decision rates |

The baseline’s A and B pair is assembled from isolated calls, so its q is a procedural check rather than a sequential-interview test. Interference belongs to the separate direct-versus-assessed comparison. Do not construct it from the A-B-F and B-A-F groups alone.

## Persona Grid and Sample Plan

List fictional persona descriptions relevant to the market. Use the same list in every condition, with one complete interview per persona per condition for this starter design. The notebook resamples each persona and its six records together. If you use repeated interviews, unequal weights, or a different allocation, agree on the analysis with the instructor before collecting the main data.

A planning example uses 24 persona descriptions, giving 144 condition records and 360 one-question model calls. This is a workflow pilot, not a power guarantee. Start with a small technical pilot, estimate cost, and freeze the main sample within the approved budget. Small or empty conditional groups can make the bracket unresolved. More calls from the same narrow grid do not establish representativeness of people.

## Collect and Preserve the Responses

## Prompt Template

Use the following neutral instruction with your own background facts and persona description: “For this fictional respondent exercise, answer as the person described. Use the supplied background facts. Answer the question with YES or NO only.” Do not name the expected effect, desired company outcome, QQ value, or simulator regime.

1. Freeze the exact persona descriptions, facts, questions, instructions, model version, settings, and retry rule. Save a dated copy before the main run. A model-generated persona description should be reviewed and recorded like any other AI contribution.

2. Shuffle the persona-condition run schedule. In isolated conditions, start a new conversation for each item and include only the common facts, persona, and current question. In constructed and assessed conditions, retain the actual prior questions and answers. The direct condition contains only F.

3. Save the raw output from every call before coding it. Use one fixed rule for valid YES and NO responses. Set a maximum number of retries in advance, retain failed attempts, and identify which valid response is included. Never replace an inconvenient valid answer.

4. Record one analysis row per complete condition interview. Include a unique interview ID, persona ID, condition code, A, B, and F answers where asked, and a path to the raw interview record. Use null for questions not asked. Keep model settings and timestamps in the raw record.

5. Check counts before analysis. The starter requires all six conditions for every retained persona, with no duplicates. If a record remains missing, document the cause and any exclusion of the whole persona from the matched analysis. Report all attrition and discuss how it could affect the result.

The raw interview file should contain every system and user message, every model reply, model and provider identifiers, settings, timestamps, and retry history. Do not put API keys or confidential company material in the repository. No human recruitment is required for this assignment.

## Calculate and Interpret the Results

Use rates between 0 and 1 for calculation. Multiply a difference by 100 to report percentage points. Keep A in rows and B in columns in both answer tables.

| Quantity | Calculation and Denominator |
| --- | --- |
| Main Order Effect | F yes count divided by complete interviews in A-first, minus the corresponding rate in B-first. |
| QQ Statistic q | Within each order, add A yes B yes and A no B no counts and divide by that order’s complete interviews. Subtract B-first agreement from A-first agreement. |
| Assessed Weight | A yes count divided by all complete assessed interviews. The A no weight is the remainder. |
| Conditional Rates | F yes among A yes divided by the A yes assessed count; F yes among A no divided by the A no assessed count. |
| Weighted Prediction | Multiply each conditional rate by its assessed weight and add. With these same records, this equals the overall F yes rate in the assessed condition. |
| Interference | Direct F yes rate minus the weighted prediction. This is a cross-procedure comparison. |
| Bracket | The smaller and larger conditional rates are the endpoints. Compare the direct rate with both using direct-minus-conditional differences. |

The fixed-rate benchmark assumes the assessed response rates carry over to direct decisions. A direct rate outside both endpoints challenges that assumption. Interference can be nonzero while the direct rate stays inside the bracket. Report both comparisons and their uncertainty.

For the provided matched design, resample persona IDs with replacement and retain all six records for each selected ID. This preserves answer pairs and cross-condition links. A 95% interval is a property of a repeated-sampling procedure under its assumptions. For model outputs, the interval describes the chosen resampling scheme and tested grid; it does not quantify uncertainty about human customers.

## Report and Log Templates

## Report Outline

1. Decision and recommendation: name the company action, owner, and condition for review.

2. Design: identify the model setup, persona grid, questions, conditions, sample sizes, coding, and departures from Part 1.

3. Results: provide counts, answer tables, main effects, q, direct and assessed rates, interference, bracket contrasts, and intervals. Interpret them against the frozen rules.

4. Rival and scope: report the rival check, state the evidence tier, and identify what a human validation study would need to establish.

5. Revision: explain one retained or changed judgment and the evidence supporting it. Link the detailed logs and reproducible notebook.

## AI Attribution Log Entry

Copy this entry for each substantive use. Link the full prompts and outputs when they are lengthy. Model calls used as audit data may be grouped by a recorded batch, provided every call remains traceable.

Date and task: [response]
Tool provider and model version: [response]
Settings and prompt or raw-file reference: [response]
Output used and location in submission: [response]
Member who used the tool and member who checked the result: [response]
Verification and sources checked: [response]
What you changed or rejected and why: [response]

## Contribution Record Entry

Task and date: [response]
Member responsible: [response]
Work produced and file or commit: [response]
Member who checked the work and result of the check: [response]
Decisions agreed by the team: [response]

Record substantive contributions as the work proceeds. All members review the final submission and prepare to explain the full audit. The contribution record supports transparency; it does not introduce a separate graded activity or an automatic peer-score adjustment.

## Revision Record Entry

Date and stage before or after relevant results: [response]
Original claim or design choice and version: [response]
Evidence or feedback prompting review: [response]
Revised or retained judgment and reason: [response]
Consequence for the client recommendation: [response]

## Notebook and File Setup

Open M1_4_Project_Audit_Starter.ipynb. Its default mode uses labeled simulated demonstration data so you can check the workflow without an API key. For your project, switch to the model-data mode and supply your collected JSON file. The notebook stops if required conditions or records are missing. A successful demonstration run is still Tier 1.

## Analysis Record Template

The input file is a JSON list of interview records. Use the following fields for each record. The notebook creates a clearly labeled example file that you can inspect; the example is simulated and cannot serve as your Tier 2 submission.

| Field | Value |
| --- | --- |
| interview_id | Unique text identifier for this condition interview |
| persona_id | Same identifier for the same fictional persona across all six conditions |
| condition | One of the six exact condition codes on page 2 |
| A and B | 0 or 1 when asked; null when not asked |
| F | 0 or 1 in every condition |
| raw_file | Relative path to the saved raw interview JSON file |

## Suggested Repository Contents

Keep the team’s frozen proposal and questions, persona grid, model-data JSON, raw interview records, executed notebook, result tables, report, slides, attribution log, contribution record, and revision log in clearly named folders in the approved private submission repository. Add a README that identifies the evidence tier, software, input file, and steps for rerunning the analysis. Use a commit identifier to identify the submitted version.

In Colab, upload the notebook and model-data file, plus the raw-record folder in a ZIP if needed; extract the folder beside the notebook input. In a local notebook environment, keep the same relative paths. The analysis needs only Python and NumPy. It does not call an AI provider or incur usage charges. Collect model responses separately with the course-approved tool and preserve the full records specified in this guide.
