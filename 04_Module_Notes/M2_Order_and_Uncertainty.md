# Module 2: Order Effects and Uncertainty

## Changing the Sequence

Module 1 raised a practical question: can the procedure help produce the judgment being measured? An order experiment makes that question concrete. Define question A, question B, and a focal decision F. One condition asks A, then B, then F. Another asks B, then A, then F. Keep the wording, facts, and coding fixed. A change in F's yes rate then describes a difference between these two procedures.

**Slate order** concerns the arrangement of displayed alternatives. **Frame order** concerns the sequence in which considerations or questions are introduced. A study can vary these separately. Randomizing product positions addresses one source of variation; it does not automatically address the order of questions about convenience and privacy.

## Sequential Judgments

In the geometric model, answering the first question updates the state used for the next. Two judgments are **non-commuting** when reversing their mathematical operations changes the result. The term describes a property of the model. An observed order effect motivates investigation, but it does not establish that this particular model generated the answers.

The book's example starts with a state at 20 degrees, question A at 0 degrees, and question B at 50 degrees. B's yes probability is 0.75 when B is first and about 0.433 when B follows A. These are calculated probabilities under imposed angles. The notebook reproduces them and lets you change one input at a time.

## Reading the QQ Statistic

The **QQ statistic**, denoted q, compares the share giving matching answers in the two orders:

`q = P(yes, yes | AB) + P(no, no | AB) - P(yes, yes | BA) - P(no, no | BA)`

Each probability uses the interviews in its own order as the denominator. A pair is one person's or one model interview's two actual answers. Pooling separate yes rates does not recover the pair table. In the simple sequential projective model, the two agreement shares are equal, so q is zero. [Wang and colleagues (2014)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4084470/) examine this restriction in survey data.

The restriction leaves room for a substantial order effect. It also leaves room for classical alternatives. For example, the following imposed tables have q = 0 even though A's yes rate changes from 0.40 to 0.70. Both tables use A as rows and B as columns.

| Answer Pair | AB | BA, Relabeled by Question |
| --- | ---: | ---: |
| A yes, B yes | 0.30 | 0.45 |
| A yes, B no | 0.10 | 0.25 |
| A no, B yes | 0.20 | 0.05 |
| A no, B no | 0.40 | 0.25 |

Each agreement share is 0.70. A classical sequential process can generate these tables by using different conditional response rules after A and after B. The notebook supplies those rules. Agreement with q = 0 therefore supports compatibility with one restriction; it does not select a unique mechanism. The focal F difference is a separate statistic and requires F responses.

## Precision and Practical Importance

A sample estimate varies across repeated samples. A **confidence interval** is produced by a procedure designed to cover the target quantity at a stated frequency under its assumptions. A narrow interval is more informative about magnitude than a wide one. An interval containing zero does not by itself establish a negligible effect.

Suppose a manager specifies a practical tolerance of five percentage points before seeing the data. An interval from −2 to 3 percentage points lies entirely inside that range. An interval from −12 to 14 includes both small and important effects. Those two results support different decisions even if both contain zero. The course uses a transparent interval-versus-tolerance decision rule. It is distinct from a fully specified equivalence-testing procedure such as the one discussed by [Lakens (2017)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5502906/).

## Preserving the Sampling Structure

The project asks each persona to appear in six conditions. The starter notebook resamples complete persona blocks, keeping all six interviews together. This **block bootstrap** preserves dependence across conditions in the analysis. Treating every answer as an independent observation would discard that structure. The resulting intervals describe uncertainty under the sampled persona blocks and fixed collection procedure; they do not establish representativeness of people.

Run [M2_Order_and_QQ.ipynb](../06_Python/notebooks/M2_Order_and_QQ.ipynb). Verify the agreement sums, inspect the classical alternative, and explain why q and the focal order difference answer different questions. Before collecting project data, state the effect you want to estimate, the tolerance that matters, and a result that would change your interpretation.

**Book connections:** “Order and the QQ Equality,” “Evidence Order,” and the Python lab. [Reading guide](../05_Readings/README.md).
