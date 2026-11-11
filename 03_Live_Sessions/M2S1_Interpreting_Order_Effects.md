# M2S1: Interpreting Order Effects

**Preparation:** Watch the Module 2 videos, including intervals and tolerances. Run the order-and-QQ notebook and bring a preliminary A/B/F battery.

**Session Output:** A correct QQ interpretation, a defined focal order comparison, and draft thresholds and rival tests for the proposal.

This 90-minute meeting assumes the videos have been watched. Use the activities to develop your individual assessments. Follow the assessment brief for submission requirements.

**Assessment Connections:** [M2A1_Discussion_2](../02_Assessments/M2A1_Discussion_2.md), [M2A2_Project_Part_1](../02_Assessments/M2A2_Project_Part_1.md)

## Meeting Plan

| Activity | Minutes |
| --- | ---: |
| Order Differences and QQ | 5 |
| An Imposed Answer-Pair Table | 10 |
| Agreement and the A-Yes Rate | 15 |
| A Classical Sequential Explanation | 15 |
| Intervals Against a Practical Range | 10 |
| Resampling Complete Personas | 10 |
| Design Revisions | 15 |
| The Interpretation Paragraph | 10 |

## Slide 1: Interpreting Order Effects

Quantum Cognition for Human-AI Decision Teaming

Nathan Yang

M2S1

### Discussion and Work

This meeting assumes that students have watched the module videos. Use the session for application and assessment progress.

## Slide 2: Order Differences and QQ

Which statistic compares F across orders?

Which statistic compares A/B agreement?

What records does each require?

### Discussion and Work

Give students two minutes to write their answers. The focal difference uses F yes rates; q uses actual paired A/B responses within each order. Clarify only the distinctions that remain uncertain.

## Slide 3: An Imposed Answer-Pair Table

Both columns contain 100 illustrative interviews.

| Answer pair | AB | BA |
| --- | --- | --- |
| A yes, B yes | 30 | 45 |
| A yes, B no | 10 | 25 |
| A no, B yes | 20 | 5 |
| A no, B no | 40 | 25 |

### Discussion and Work

The table consistently uses A rows and B columns, including for BA. These are imposed counts and not human observations. Students should verify totals before computing rates.

## Slide 4: Agreement and the A-Yes Rate

Why can agreement stay fixed while an answer rate changes?

Calculated from the imposed answer-pair table on the previous slide.

| Category | AB order | BA order |
| --- | ---: | ---: |
| A yes | 0.4 | 0.7 |
| A/B agreement | 0.7 | 0.7 |

**Units:** Share of 100 interviews in each order. Values for percentage-formatted rate charts are stored as proportions (0.64 means 64%).

### Discussion and Work

A-yes is (30+10)/100=.40 in AB and (45+25)/100=.70 in BA. Agreement is (30+40)/100=.70 in AB and (45+25)/100=.70 in BA, so q=.00 for the agreement-difference definition. A-yes is a marginal answer rate, not F. This table contains no F responses; it cannot establish a focal decision effect. Ask students which records their proposal needs for each statistic.

## Slide 5: A Classical Sequential Explanation

Inspect the transition rules in the notebook.

The rules vary with which question comes first.

Which extra prediction would test this explanation?

### Discussion and Work

Run classical_order_example. In AB, A yes is .4 and B yes conditional on A is .75 or 1/3. In BA, B yes is .5 and A yes conditional on B is .9 or .5. Ordinary probabilities generate the table with q=0. Source: the course’s constructed example; Dzhafarov and Kon, https://arxiv.org/abs/1710.07847.

## Slide 6: Intervals Against a Practical Range

Use a prespecified tolerance of ±5 percentage points.

| Case | Illustrative 95% interval | Decision relative to ±5 pp |
| --- | --- | --- |
| A | −2 to +3 pp | Within the range |
| B | −12 to +14 pp | Unresolved |
| C | +1 to +4 pp | Within the range |

### Discussion and Work

The intervals are illustrative inputs, not estimates from a dataset. Ask students to classify each and justify the action. A and C lie inside the practical range; B is unresolved. Revise the table if the class chooses a different managerial tolerance.

## Slide 7: Resampling Complete Personas

Which six records travel together when a persona is drawn?

Toy example: draw personas 02, 02, 03 from three complete blocks.

| Category | Original sample | One resample |
| --- | ---: | ---: |
| Persona 01 | 6 | 0 |
| Persona 02 | 6 | 12 |
| Persona 03 | 6 | 6 |

**Units:** Condition records. Values for percentage-formatted rate charts are stored as proportions (0.64 means 64%).

### Discussion and Work

Each of three personas has one record in each of six conditions. One bootstrap draw selects persona 02 twice, persona 03 once, and persona 01 zero times. Copy all six records each time a persona is selected. This example explains the resampling unit; three personas are not an adequate sample-size recommendation. For the course audit, retain the complete persona blocks and all repetitions in each selected block. For independently assigned human respondents, the resampling design would follow the actual human sampling structure.

## Slide 8: Design Revisions

Freeze A, B, F, coding, and collection conditions.

Choose a practical threshold and q tolerance.

Write a fair test of the strongest alternative.

### Discussion and Work

Students revise their own proposal. Thresholds should follow the managerial decision and feasible precision. The teaching value of .05 is not a universal threshold. Save the rationale in the proposal and log any later changes.

## Slide 9: The Interpretation Paragraph

Explain why order and QQ answer different questions.

Describe what an uncertain interval leaves unresolved.

Use that reasoning in Discussion 2.

### Discussion and Work

Write a short outline for M2A1 and identify one remaining proposal weakness. Submit individual work under the brief. Next session is the battery-design workshop.
