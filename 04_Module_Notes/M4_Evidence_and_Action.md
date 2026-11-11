# Module 4: Evidence and Managerial Action

## The Decision After the Audit

A manager receives an audit showing that question order affects a recommendation. She must decide whether to change the process, collect more evidence, or continue with the current procedure. The size of the observed difference matters, but so do its uncertainty, the alternative explanations, and the population to which it applies.

Begin the recommendation with that decision. State the tested model or population, the exact procedures compared, the outcome, and the evidence that changes the action. A reader should be able to trace a recommendation back to the counts and collection rules that support it.

## Three Statistics, Three Questions

| Quantity | Question Answered | Interpretation Needed |
| --- | --- | --- |
| Focal order difference | How much did F's yes rate change between ABF and BAF? | Wording, population, order assignment, and practical threshold. |
| QQ statistic | How much did A/B agreement differ between the two orders? | Actual paired answers, interval precision, tolerance, and alternative mechanisms. |
| Direct-minus-assessed difference | How much did F's rate change when A was elicited first? | Separate direct and assessed conditions; a fixed-rate comparison requires transport assumptions. |

A large focal order difference can matter operationally even when the model comparison remains unresolved. A q interval inside a prespecified tolerance supports a narrow statement about one restriction. A direct rate outside the assessed bracket challenges carrying those assessed conditional rates into the direct procedure. None of these statements alone establishes human representativeness of an AI panel.

## Match the Action to the Evidence

Consider three illustrative outcomes. First, a precise order difference exceeds the manager's practical threshold. The evidence supports considering a process change or a human validation experiment, depending on the setting. Second, the interval lies within the practical range. The team may retain the procedure for that outcome and setting, with a stated review condition. Third, the interval spans both small and important effects. The appropriate next step may be more informative data rather than a categorical verdict.

The decision rule should be specified before examining the result. A rule chosen after seeing the interval can turn interpretation into a search for a preferred answer. Where choices were revised, document the revision and distinguish exploratory findings from the original comparison.

## Evaluate the Strongest Alternative

A fair comparison gives the alternative explanation a chance to succeed. A context-dependent classical model may explain an order effect. Differences in wording or retained information may explain differences between model panels. A model release may change behavior between batches. Identify the relevant alternative, what evidence would favor it, and what additional comparison would be informative.

The [classical sequential example](../06_Python/qc_models.py) provides a concrete reminder: an order effect can coexist with q = 0 in a classical process. The contribution of a quantum model may lie in its parsimonious restrictions or predictive performance. Compare those properties directly instead of inferring a mechanism from a label.

## A Recommendation With an Owner

A complete recommendation names the action, the owner, the evidence supporting it, and a condition for review. For example: “The survey team should randomize frame order in the next model-panel collection and report both order-specific rates. The current result is sensitive to order. The team should revisit the design after collecting matched human responses using the same wording.” The final sentence states the evidence needed for a broader decision.

An audit of model responses supports conclusions about those model responses. Human deployment additionally depends on relevant human outcomes and costs. An operationally sensible change can be worth testing even while the mechanism remains uncertain.

## The Client Presentation

The ten-minute project presentation has 6–10 slides. Introduce the decision and the measured comparison, explain the design, show the three-statistic pattern with uncertainty, evaluate the strongest alternative, and recommend an action. Select the evidence that affects the decision. Keep complete counts, code, and collection records available for questions.

Practice answering three questions without AI assistance: What result would change your recommendation? Which assumption carries the broadest claim? What did you revise after examining the evidence? The oral defense is an opportunity to show ownership of the analysis. Follow the [Part 2 instructions](../02_Assessments/M4A1_Project_Part_2.md) and the [reflection instructions](../02_Assessments/M4A2_Reflection.md) for the separate submission requirements.

**Book connections:** “Real Versus Decorative Quantum,” “What It Is and Is Not,” and the worked-audit appendix. The course focuses on the claims needed for a four-week managerial audit. [Reading guide](../05_Readings/README.md).
