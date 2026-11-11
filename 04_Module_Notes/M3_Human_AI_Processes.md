# Module 3: Human-AI Decision Processes

## The Intermediate Judgment

The sequence examined in Module 2 becomes a design choice when software determines what a person sees next. A fraud-review console might ask for a block-or-allow decision immediately. Another might first require a fraud-or-legitimate judgment. The manager needs to know how that extra step affects decisions, accuracy, and the cost of errors.

Meridian is a fictional payment company used in the book. In an illustrative comparison, the assess-first procedure has block rates of 0.63 after a fraud judgment and 0.41 after a legitimate judgment. With a fraud-judgment share of 9/11, its weighted block rate is 0.59. The direct procedure has a block rate of 0.69, above both assessed conditional rates. These numbers illustrate a possible pattern; they are not field estimates from a real company.

## What the Weighted Rate Means

Write w for the share answering yes to intermediate question A. Let r_yes and r_no be F's yes rates within A's two answer groups. The assessed average is:

`weighted = w × r_yes + (1 − w) × r_no`

When all three inputs come from the same complete assess-first records, this calculation equals the overall assessed F rate. That equality is an accounting identity. Predicting a different, direct procedure with it requires an additional assumption that the relevant conditional rates remain applicable across procedures.

The course's **interference estimate** is `direct − weighted`. The **bracket** runs from the smaller conditional rate to the larger one. A direct rate outside that bracket challenges every mixture of those fixed rates. It does not rule out a classical process that changes the conditional responses when the procedure changes. Retain that distinction when proposing a mechanism.

## The Manager's Outcome

A higher block rate does not establish better fraud detection. The manager also needs outcomes such as fraud losses, legitimate payments blocked, review time, and appropriately calibrated reliance on advice. Trust is a separate measured outcome. The published [Humr and Canan (2024)](https://www.mdpi.com/1099-4300/26/6/500) study motivates examining intermediate judgments in AI-supported decisions, while a production decision requires evidence relevant to the actual console and users.

The course's two-dimensional geometric demonstration uses a different set of imposed inputs: conditional rates 0.70 and 0.30, equal weights, and a direct rate about 0.958. It is a simple computational example, rather than a fitted model of the Meridian case. Keeping those examples separate prevents a convenient illustration from becoming an empirical claim.

## Recommendation Systems and Goals

Juno is another fictional case. A shopping feed can introduce popularity or a customer's stated goal first. The team should measure whether that choice changes purchases and whether purchases advance the customer's goal. A conversion rate alone cannot answer both questions.

A useful experiment holds the available items and factual information fixed while varying the framing procedure. User control over the goal or presentation may be another design option to evaluate. Changes in behavior could reflect attention, learning, incentives, or other processes. Research on [induced preference shifts in recommenders](https://proceedings.mlr.press/v162/carroll22a.html) provides a complementary modeling approach.

## Synthetic Respondents and Evidence Tiers

A **synthetic respondent** is a model answering under a specified persona and prompt. Matching a demographic description does not make it a sampled human. A useful validation distinguishes three evidence levels. **Tier 1** uses a simulator with known rules to check the calculation. **Tier 2** studies an actual model under documented prompts and settings. **Tier 3** adds evidence from the relevant people and setting.

The project operates at Tier 2 after the Tier 1 practice run. Model versions, prompts, persona construction, settings, missing answers, and retries are part of the result. [Bisbee and colleagues (2024)](https://doi.org/10.1017/pan.2024.5) show why aggregate agreement can coexist with deficiencies in synthetic survey data. Treat human validation as a separate empirical task.

## Collecting the Six Conditions

The project uses isolated AB and BA interviews; constructed AB and BA interviews that retain actual answers; direct F-only interviews; and assessed A-then-F interviews. Use the same persona grid in all six. Fresh conversations implement isolation. Retaining the prior question and actual answer implements the constructed sequence. The direct and assessed arms supply the data for the interference comparison.

The [collection guide](../02_Assessments/M1_4_Project_Templates_and_Collection_Guide.md) gives the complete procedure. Run the [interference notebook](../06_Python/notebooks/M3_Interference_and_Brackets.ipynb), then complete [M3A2](../02_Assessments/M3A2_Audit_Practice.md). The project starter analyzes saved interviews; it makes no paid model calls. Confirm the approved tool and collection budget before gathering model responses.

**Book connections:** “The Missing Layer,” “Case: The Intermediate Step,” “Case: Which Self Are You Optimizing?,” and the Python lab. [Reading guide](../05_Readings/README.md).
