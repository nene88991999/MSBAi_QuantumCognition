# M1M3L4_Running the Audit and the Tier 2 Boundary

In the last lecture, we compared three kinds of synthetic panel. Now imagine a manager receives support estimates from all three.

Before comparing them, the analyst has to check the process that produced each one. Start with the table of individual answers.

Check the counts for each panel and order, make sure every answer is a valid yes or no, and look for missing items, duplicate records, and incomplete model details. Fix any errors using the rules you set in advance, and then freeze the dataset so it can't quietly change.

After that, you'll calculate three statistics. For their uncertainty, use the bootstrap, resampling the right unit for your design, which is usually a whole respondent interview within each panel and order.

Keep each person's answer pairs together. If repeated interviews with a persona share a common source of variation, resample those interviews together.

That's a cluster bootstrap: it keeps related observations together. The resampling unit should follow how the responses were generated.

And include the extra comparison groups when you bootstrap interference.

With the records checked, start with the number that matters most to the client's decision. The first statistic is the main order effect.

In the constructed panel, take the share answering yes after A then B, and subtract the share answering yes after B then A. Check whether the direction matches what you predicted before collecting responses.

In our data-center survey, for example, asking about the economy first might raise support compared with asking about the environment first. Report the difference in percentage points, along with a bootstrap interval.

This statistic tells you whether question order changes the outcome the client cares about. It can't tell you why, though.

Clues about the desired answer, attention drawn to an earlier idea, carryover from a previous answer, and quirks of a particular model can all create the same overall shift.

To look at the pattern behind that shift, go back to the two framing answers. The second statistic is q.

Build the answer-pair table for each order using the same layout, with A's answers in the rows and B's in the columns. In each table, add yes-yes and no-no to get the agreement rate.

Then subtract the B-first agreement rate from the A-first agreement rate. The geometric model predicts zero.

Compare the bootstrap interval with the tolerance you set in advance. If the interval sits within the tolerance, the departure is small enough for that practical standard.

It doesn't establish exact equality. A clear departure challenges the model, as long as your measurement checks pass.

Coding mistakes, or running the two orders differently, can also create a departure, so rule those out before choosing an explanation.

Reversing question order is one kind of comparison. Leaving out an assessment is another, and that's what the third statistic is about.

It compares a direct action with a weighted prediction based on assessed judgments, just like the Meridian example earlier in this module. The design needs a direct condition, the response rate after each possible assessment, and the weights to combine those rates.

Interference is the direct rate minus the weighted average. Separately, check whether the direct rate falls outside the range between the two assessed rates, which is the bracket.

A nonzero difference doesn't automatically mean the bracket is broken, so report uncertainty for both. Define these conditions when you design the study, because simply reversing two questions won't give you the observations this test needs.

Let's read some illustrative results. The isolated-item panel changes by just half a percentage point between its order labels, which is what we'd expect, since it never sees a sequence.

The constructed panel changes by fifteen points. Its q is close to zero, with an interval from minus 0.05 to plus 0.05.

Its interference estimate is minus 0.085, with an interval from minus 0.13 to minus 0.04. The ordinary panel changes by fourteen points, and its q is 0.085.

So the two large effects look similar, but the other statistics are quite different. Compare the q intervals with the tolerance you set in advance, and check the bracket separately, before interpreting either panel.

This shows that the same headline effect can lead to different decisions, so read the results together. A small, precise main effect can support keeping the simpler process for this task.

A meaningful effect, with a q interval inside the tolerance and a confirmed bracket violation, is a stronger challenge to the fixed-rate benchmark, although some classical explanations where the process changes are still possible. A q interval clearly outside the tolerance challenges the geometric model.

If you don't have the direct comparison, your claim has to be narrower. And wide intervals leave the question open.

As always, set these branches before you see the results. Also note that the illustrative numbers on this slide don't settle every branch on their own, because some intervals and bracket endpoints aren't shown.

Even a convincing pattern needs a clear answer to one question: a pattern in whom? Suppose the model shows a meaningful order effect, meets the QQ tolerance, and breaks the bracket.

That's evidence about how this model, with this setup, generates answers. It doesn't directly measure residents, customers, or employees.

Real people face circumstances, incentives, and consequences that a prompted model never experiences. To keep our conclusions honest, we use three evidence tiers: a check on simulated data, an audit of model behavior, and a study of real people.

Each one answers a different question.

Let's go through them. Tier 1 checks our tools before we trust them with a new result.

It runs the audit on simulated processes where we already know the right answer, and checks whether the audit reaches the correct verdict at the sample size we plan to use. Tier 2 applies the questions and coding rules, fixed before the run, to language models.

It can reveal unclear wording, unstable prompts, model drift, and answers that look human but have the wrong underlying pattern. Its conclusions apply only to the named model, version, prompt setup, and persona grid.

Tier 3 uses the same design with the real people relevant to the decision. Only Tier 3 can tell you whether those people show the pattern in that setting.

So each tier supports a different kind of claim. Tier 1 checks the estimator, which is just the calculation we use to get a number from data, along with our decision rules, against simulated processes.

Its conclusion is about how well our tools perform in those simulations. Tier 2 shows how a named model, version, prompt setup, and persona grid behave.

Tier 3 supports a statement about the real people sampled, answering the questions as they were actually asked. Every conclusion should name its tier, the group or model tested, and its scope.

A Tier 2 order effect belongs to the language model. A Tier 3 order effect belongs to the people sampled and the survey they took.

And similar percentages from a model and from people don't make the model a verified stand-in for human respondents.

Let's wrap up Module 3. The audit treats the interaction between people and AI as part of the measurement process itself.

It brings the order effect, q, and interference together in one analysis, and then limits each claim to the evidence actually collected. A Tier 2 result describes the responses of a specific model, and it can help you prepare a human study.

But a recommendation about people needs Tier 3 evidence from the right population. In Module 4, we'll take the next step: figuring out which action an observed pattern supports, and what further evidence the decision still needs.
