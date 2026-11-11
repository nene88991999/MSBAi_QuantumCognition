# M2S1: Interpreting Order Effects



**Preparation:** Watch the Module 2 videos, including intervals and tolerances. Run the order-and-QQ notebook and bring a preliminary A/B/F battery.



**Session output:** A correct QQ interpretation, a defined focal order comparison, and draft thresholds and rival tests for the proposal.



This 90-minute meeting assumes the videos have been watched. The activities support the assessments listed below; follow each assessment brief for individual submission requirements.



**Assessment connections:** [M2A1_Discussion_2](../02_Assessments/M2A1_Discussion_2.md), [M2A2_Project_Part_1](../02_Assessments/M2A2_Project_Part_1.md)



## Meeting Plan



| Activity | Minutes |

| --- | ---: |

| Order Differences and QQ | 5 |

| An Imposed Answer-Pair Table | 10 |

| Agreement Shares and Order Rates | 15 |

| A Classical Sequential Explanation | 15 |

| Intervals Against a Practical Range | 10 |

| The Resampling Unit | 10 |

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



## Slide 4: Agreement Shares and Order Rates



Calculate each order’s agreement share.

Compare A’s yes rate across orders.

State what is missing for an F comparison.



### Discussion and Work

Students compute in pairs and compare with the M2 notebook. Each agreement share is 70/100; A yes rates are 40/100 and 70/100. F has not been observed in this table. These are class exercises rather than a project answer key.



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



## Slide 7: The Resampling Unit



The project links six interviews to each persona.

Keep the complete block together.

Explain what independent sampling is assumed.



### Discussion and Work

Use the collection guide to identify one block. Resampling individual answers would sever the design’s links. A persona bootstrap represents variation over the sampled blocks under a fixed collection process; it does not turn model personas into sampled people.



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
