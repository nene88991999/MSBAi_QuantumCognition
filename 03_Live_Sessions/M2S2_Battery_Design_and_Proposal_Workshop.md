# M2S2: Battery Design and Proposal Workshop

**Preparation:** Bring the draft proposal, question battery, evidence ledger, and collection guide. Review the Part 1 rubric.

**Session Output:** A revised proposal with fixed wording, six conditions, a persona plan, thresholds, and explicit actions for different findings.

This 90-minute meeting assumes the videos have been watched. Use the activities to develop your individual assessments. Follow the assessment brief for submission requirements.

**Assessment Connections:** [M2A2_Project_Part_1](../02_Assessments/M2A2_Project_Part_1.md)

## Meeting Plan

| Activity | Minutes |
| --- | ---: |
| A Battery for the Service Decision | 10 |
| Six Conditions, One Persona Grid | 15 |
| The Final Question Has a Fixed Position | 10 |
| The Record of What Each Person Saw | 10 |
| Precision and the Collection Plan | 15 |
| Peer Review Against the Rubric | 15 |
| Revisions and Their Reasons | 10 |
| Proposal Submission Check | 5 |

## Slide 1: Battery Design and Proposal Workshop

Quantum Cognition for Human-AI Decision Teaming

Nathan Yang

M2S2

### Discussion and Work

This meeting assumes that students have watched the module videos. Use the session for application and assessment progress.

## Slide 2: A Battery for the Service Decision

How would you revise these questions for your company?

Fictional planning example. Supply the same service facts in every arm.

| Question | Consideration | Response |
| --- | --- | --- |
| A | Is the convenience valuable? | Yes / No |
| B | Is the privacy protection adequate? | Yes / No |
| F | Would you support the launch? | Yes / No |

### Discussion and Work

A battery is a set of questions used together. These shortened prompts illustrate structure; students must specify the service, features, privacy practices, and neutral wording. In the constructed ABF and BAF arms, keep F last and retain actual prior answers. Follow the collection guide for all six conditions. Define any specialized terms in the survey itself.

## Slide 3: Six Conditions, One Persona Grid



| Condition | Question sequence | Context retained |
| --- | --- | --- |
| Isolated AB / BA | A, B, F / B, A, F | Fresh for each question |
| Constructed AB / BA | A → B → F / B → A → F | Prior questions and answers |
| Direct | F only | No prior assessment |
| Assessed | A → F | Prior question and answer |

### Discussion and Work

The isolated conditions ask every question in a fresh conversation. Constructed conditions retain actual prior answers. Direct and assessed arms supply the separate procedural comparison. An ordinary all-at-once panel is optional and does not replace a required arm.

## Slide 4: The Final Question Has a Fixed Position

Randomizing questions and selecting a subset change different things.

Which items vary, and which position stays fixed?

Qualtrics documentation: advanced randomization.

[Official source image](assets/qualtrics_advanced.png)

**Image Description:** The upper portion of the official advanced-randomization dialog contrasts fixed display order with randomize questions. The displayed example text belongs to Qualtrics, not the course battery.

### Discussion and Work

Use this product example to inspect a design choice before collecting data. The screenshot shows a general control, not a configured ABF/BAF study. Students identify how their implementation preserves F last while varying A and B. Hold the fact sheet, coding, and intended context fixed. Pilot both orders and save the exact prompts, actual answers, and conversation history.

**Sources:** [Source 1](https://www.qualtrics.com/support/survey-platform/survey-module/block-options/question-randomization/). Accessed November 11, 2026.

## Slide 5: The Record of What Each Person Saw

The assigned order and the observed order should agree.

Can your records reconstruct the question sequence?

Qualtrics documentation: viewing-order export.

[Official source image](assets/qualtrics_export.png)

**Image Description:** An official Qualtrics export dialog has the option Export viewing order data for randomized surveys checked and outlined.

### Discussion and Work

Qualtrics documents an option to export viewing order. The course model-panel workflow needs the analogous evidence: condition, persona, repetition, actual prompt order, response, and conversation history. Set the collection volume, model version, settings, and stopping rule before collection. Students save a pilot record and verify it can reproduce a response path. This slide does not require students to use Qualtrics.

**Sources:** [Source 1](https://www.qualtrics.com/support/survey-platform/survey-module/block-options/question-randomization/). Accessed November 11, 2026.

## Slide 6: Precision and the Collection Plan

How does this uncertainty compare with your practical threshold?

Planning illustration: two independent arms, each with yes probability 0.50.

| Observations per arm (each step doubles n) | Approximate half-width |
| --- | ---: |
| 50 | 19.6 |
| 100 | 13.86 |
| 200 | 9.8 |
| 400 | 6.93 |
| 800 | 4.9 |

**Units:** 95% interval half-width (percentage points). Values for percentage-formatted rate charts are stored as proportions (0.64 means 64%).

### Discussion and Work

The displayed normal-approximation half-width for a difference is 1.96 × sqrt(0.25/n+0.25/n) ×100 percentage points, where n is observations per independent arm. Values are about 19.6, 13.9, 9.8, 6.9, and 4.9 points. This conservative planning illustration is not the audit’s paired-persona bootstrap interval or a sample-size prescription. Dependence, rare subgroups, and invalid answers affect precision. Students freeze their substantive thresholds and appropriate analysis before observing the project results.

## Slide 7: Peer Review Against the Rubric

Find one claim without enough evidence.

Find one design choice that could change the result.

Propose a concrete revision.

### Discussion and Work

Partners use the M2A2 rubric and collection checklist. Keep feedback specific. Each student owns the final proposal and discloses permitted AI assistance.

## Slide 8: Revisions and Their Reasons

Resolve the highest-impact issue first.

Record what changed and why.

Preserve the original prediction for comparison later.

### Discussion and Work

Allow quiet revision time. A useful revision log separates planned design changes from changes made after results are observed. The log later supports Project Part 2 and the reflection.

## Slide 9: Proposal Submission Check

Attach the proposal, battery, sources, and AI log.

Check the exact Canvas deadline.

Retain a fixed copy before collecting project data.

### Discussion and Work

Use M2A2 for the complete requirements. This workshop does not add a separate submission.
