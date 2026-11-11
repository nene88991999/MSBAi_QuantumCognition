# Audit Notebook Practice

M3A2  |  Individual  |  Ungraded  |  Before Project Studio 3

Check the audit calculations on simulated responses whose generating process is known. This is Tier 1 validation: it checks the analysis before you use it on a language model. No API key, paid model call, or physics background is needed.

## Start the Notebook

Open M3A2_Audit_Practice.ipynb from the Notebooks folder in Colab, Jupyter, or VS Code. In Colab, upload the notebook and choose Run all. The notebook needs Python and NumPy, already available in Colab. Work on your own copy and save the outputs with it.

The first simulator draws from one fixed joint distribution of A, B, and F, so changing the question order leaves the population rates unchanged. The second uses a specified geometric model in which asking a question changes the simulated state. Both are mathematical examples. Neither contains human or language-model responses.

1. Before running, write a short prediction about the order effect, q, interference, and the bracket for each simulator. Use the notebook’s population benchmark table to check what the generating assumptions imply.

2. Run the default sample and bootstrap settings. Confirm the counts and answer coding. For each simulator, report the constructed-panel order effect, q, interference, and bracket result with the intervals the notebook produces.

3. Compare each estimate with its known population value. An individual confidence interval can miss the population value. Investigate systematic discrepancies rather than requiring every interval to contain the truth.

4. Repeat with 100 interviews per condition, using the supplied sensitivity cell. Explain how the interval widths and decision branches change. Do not change the prespecified five-percentage-point thresholds to improve the result.

5. Complete the hand calculation on the next page. Then explain why model-generated results would support a Tier 2 claim, and identify the additional evidence needed for a claim about people.

## Submit

Submit the executed .ipynb file through Canvas and include its repository link. Fill in the notebook’s short response sections, about 250–400 words in total. Bring one calculation or design question to Project Studio 3. Allow about 60–90 minutes.

## Hand Calculation

These invented summary counts are a separate arithmetic exercise. Each order has 100 complete interviews. The cells below always name A first and B second, even when B was asked first.

| Order | A Yes B Yes | A Yes B No | A No B Yes | A No B No | F Yes |
| --- | --- | --- | --- | --- | --- |
| A Then B | 36 | 24 | 16 | 24 | 68 |
| B Then A | 26 | 14 | 26 | 34 | 52 |

A separate direct condition has 45 F yes responses among 100 interviews. In the assessed condition, A is asked before F. Of 60 A yes responses, 36 are followed by F yes. Of 40 A no responses, 32 are followed by F yes.

1. Calculate the F order effect as the A-first yes rate minus the B-first yes rate. Report percentage points.

2. Compute the agreement rate in each order by adding the yes-yes and no-no counts and dividing by that order’s total. Subtract the B-first rate from the A-first rate to obtain q.

3. Compute the A yes weight, the F yes rate after A yes, and the F yes rate after A no. Multiply each conditional rate by its weight and add them to obtain the weighted prediction.

4. Subtract the weighted prediction from the direct F rate to obtain interference. Identify the smaller and larger conditional rates, which form the bracket. Locate the direct rate relative to that bracket.

5. State what the point estimates suggest and what remains unresolved without uncertainty calculations. Explain why a nonzero interference estimate alone does not establish a bracket violation.

## Practice Feedback and Checks

This checkpoint carries zero points. Use the feedback to fix your analysis before the project. The instructor will mark each item as demonstrated or revise and resubmit.

| Check | Evidence to Look For |
| --- | --- |
| Runnable Notebook | All cells run in order from a fresh session; outputs and the random seed are retained. |
| Correct Records | Both framing answers remain paired; A and B keep their names across order; direct and assessed records use their own denominators. |
| Accurate Calculations | Hand calculations match the definitions, and simulated estimates approach their known population values. |
| Uncertainty | The bootstrap preserves the complete sampling unit; the smaller run is interpreted using its actual precision. |
| Interpretation | The response distinguishes q tolerance, interference, the bracket, and evidence tiers without treating one passing test as proof of a mechanism. |

## Common Problems

If a cell fails, restart the session and run from the top. If NumPy is missing in a local environment, use the course-supported environment or Colab. An empty conditional group means its rate is unavailable; a missing answer is never coded as no. At small sample sizes, some bootstrap draws may have empty groups, and the notebook reports when an interval is unavailable.

The notebook uses 95% pointwise intervals for the main statistics. For the two direct-minus-conditional contrasts, it uses wider 97.5% intervals as an approximate Bonferroni adjustment for checking both endpoints. Wide intervals should lead to an unresolved conclusion.

## Use of AI

AI may help you understand errors in this ungraded practice. Record the help you used and explain the calculations yourself. Learning objectives: M3LO4 and M3LO5, with practice of M2LO3.
