# Module 1: Judgment and Models

## A Decision About a Survey

A company is considering a new service. Its survey asks customers whether they support the launch. The manager wants to know whether that answer gives a reliable basis for proceeding. Before interpreting the percentage, she needs to know how the question was asked. A prompt about convenience may direct attention toward benefits; a prompt about personal data may direct attention toward costs. The response procedure is part of the evidence.

Consider two explanations. Under a **detection explanation**, the customer already has a relevant judgment and the survey records it. Under a **construction explanation**, answering the survey helps the customer form that judgment. The word *explanation* is used here in the same sense as *account* in some readings. Both explanations can be useful, and the appropriate one depends on the decision and evidence. Constructed preference has a substantial history in behavioral research. [Bettman, Luce, and Payne (1998)](https://academic.oup.com/jcr/article-abstract/25/3/187/1795625) provide an entry point.

## What a Model Assumes

A **model** is a simplified description that produces predictions. A **classical probability model** assigns probabilities to defined events, such as a yes answer to a survey question. One version gives each person a fixed answer to every question and assumes that asking a question leaves those answers unchanged. In that version, changing the order of questions cannot change their underlying joint distribution, meaning the probabilities of each possible answer pair.

Classical probability also permits models in which memory, attention, or beliefs change during the interview. These models can produce order effects. The comparison therefore concerns specified assumptions, rather than whether a result defeats classical probability as a whole. [Dzhafarov and Kon](https://arxiv.org/abs/1710.07847) explain why labeling outcomes by their contexts matters.

The practical question is which assumptions are adequate for the decision. If a fixed-preference model predicts a new survey well, it may be sufficient. If it repeatedly misses changes caused by the procedure, the analyst should compare models that represent those changes.

## A First Picture of Quantum Probability

A quantum probability model represents a judgment using a **state**, a mathematical description of the person's current disposition to answer. A question selects a direction or subspace. The model obtains an answer probability from the squared length of a projection onto that subspace. The **Born rule** names that calculation. Recording an answer can update the state, so a later question can have a different probability.

The introductory Python example places a state 37 degrees from the yes direction. The probability is the square of the cosine of 37 degrees, about 0.638. The angle is an imposed model input. It is not a physical measurement of a person's mind. A useful application would estimate or justify its inputs and evaluate predictions against data. No claim about a physically quantum brain is required. [Yearsley and Busemeyer (2016)](https://openaccess.city.ac.uk/id/eprint/18714/) develop the mathematics for readers who want it.

## Three Comparisons

An **order effect** occurs when a defined answer rate differs across question sequences. A **conjunction judgment** compares a combined statement with its parts. An **interference comparison** in this course compares a direct decision with the weighted rate after an intermediate assessment. Each comparison needs its own data and assumptions. A single survey percentage does not establish all three.

For the interference comparison, suppose the action rates after an intermediate yes and no judgment are 0.70 and 0.30. Every weighted average of these two fixed rates lies between 0.30 and 0.70. A direct rate above 0.70 would contradict carrying those same conditional rates into the direct procedure. A process-dependent classical explanation could still change the rates across procedures. Module 3 examines that possibility.

## A Pattern Register at Northwind

Northwind is a fictional company whose analysts keep a register of recurring judgment patterns. The register helps them recognize familiar problems and assign responsibility. When a new procedure creates a new pattern, however, a list alone may offer little guidance about what will happen next.

A model adds value when it predicts an outcome that was not used to fit it. The team could fit competing explanations using one set of interviews, then test both on a new sequence or held-out sample. **Held-out** means deliberately kept separate during model selection. The comparison should state the prediction, the measurement, and the result that would count against each explanation.

## Work Through the Example

Run [M1_Probability_Onramp.ipynb](../06_Python/notebooks/M1_Probability_Onramp.ipynb). Change the state angle while keeping the question fixed. Then hold the state fixed and change the question. Explain which object you changed and how it changed the predicted probability. Finally, describe a business setting in which the act of answering might itself matter.

The main lesson is to connect a managerial decision to a specific comparison. A model earns consideration through clear assumptions and useful predictions. A familiar label or a good fit to past observations is insufficient by itself.

**Book connections:** “The Decision Default,” “A Unified View,” “Case: Northwind,” and “A Python Lab for Quantum Probabilities” in Nathan Yang's manuscript. This course companion adapts the explanations to the four-module sequence. [Reading guide](../05_Readings/README.md).
