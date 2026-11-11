# M1M2L4_Designing the Order-Effects Audit

Over the preceding lessons, we've learned how to spot an order effect, what the arrow picture predicts, and how to test the QQ equality. Now it's time to put it all together and design a complete order-effects audit.

The place to start isn't the statistics. It's the business decision.

A company might be deciding whether to change its onboarding flow, standardize how a committee reviews proposals, or change how an AI tool presents evidence. Before anything else, say which outcome matters and why the order of questions might affect it.

Here's the example we'll use throughout this lesson. A firm wants to know whether asking customers about convenience before privacy changes how willing they are to sign up for a new service.

The answer will help the signup team decide which question to ask first.

Once the decision is clear, it tells you which questions are worth asking. The next step is to choose two meaningful frames.

A frame is simply a way of looking at the decision. An investment might be seen in terms of opportunity or in terms of risk.

A digital service might be seen in terms of convenience or in terms of privacy. Be ready to explain why answering one question might change how people think about the other.

Then add a main outcome question that's tied directly to the client's decision, such as: would you sign up for this service? So the audit ends up with three questions: the two framing questions, followed by the outcome question.

Next, think ahead about what else could cause a change in sign-ups. Before collecting any data, write down the strongest classical explanation you can think of.

Name the cause, which direction you expect it to push answers, and one extra piece of evidence it predicts. For example, query theory, the memory explanation from the last lesson, might predict which thoughts people list first.

A contrast account might predict that answers depend on the previous item. And a demand account, where people respond to clues about what the study wants, might predict that answers shift when those clues are obvious.

Measuring these predictions makes the study much stronger, because in the end you can compare the explanations on the same evidence. It also stops you from putting a quantum label on a surprising result after you've seen it.

Now for the data collection itself. Reverse the order of the frames across comparable groups of respondents.

One group gets A then B, followed by the main decision question. The other gets B then A, followed by the same decision question.

Keep everything else aligned: the wording, the surrounding information, and the makeup of the groups. If you're using a synthetic panel, which means a language model answering as a set of fictional respondents, keep the model version the same too.

Use the same table of respondent descriptions in both orders, and keep each respondent's earlier answers in the conversation. And save everything: every prompt, every response, the assigned order, and the model settings.

Without that record, changes in how the AI generated its answers could easily be mistaken for an order effect.

Each part of the interview feeds a different comparison, so it's important to keep the complete record. From the two framing questions, you build the four-box answer table for each order.

From the final decision question, you compare the share of people saying yes in each order. That difference is what matters to the client, because it tells you how much the order changes sign-ups.

Meanwhile, the paired framing answers give you q, the difference in agreement rates. These are two separate calculations, using different parts of the same interview.

When you report them, include the group sizes, the counts in each box, and how you coded the answers, so another analyst could reproduce your work. And include uncertainty ranges for both.

So how do you get those uncertainty ranges? You can use the bootstrap from the last lesson.

Draw respondents at random, with replacement, within each order group, and recalculate both the main order effect and q each time. The spread of results tells you whether your estimates are precise enough to guide a decision.

Before you look at any results, set two benchmarks. One is a business threshold for the main effect: how big a change in sign-ups would actually matter to the client?

The other is an acceptable range around zero for q. Keep in mind that a small, precise change might not be worth acting on, while a large but uncertain change might justify collecting more data before any redesign.

With those benchmarks in place, you can write your decision rules in advance. If the effect on the main outcome is small and precise, take whatever action you planned for a small result.

If the effect is meaningful and the q interval sits completely inside its tolerance, compare the geometric explanation with the strongest rivals. If the q interval is completely outside the tolerance, rethink that explanation and look into the competing ones.

And if the intervals are too wide, gather more data. A result can pass one check and fail another.

Writing these branches down ahead of time keeps your recommendation tied to the evidence, and makes it obvious if anyone changes the interpretation later.

Once you know which explanation the evidence supports, you can choose the right fix. If the audit supports incompatible frames, the organization could test one standard question order, show people both frames before they commit to an answer, or develop one shared way of evaluating the decision.

If the evidence points instead to contrast, fatigue, or clues about the study's purpose, the fix should target that cause. For example, you might shuffle the agenda, set fixed standards, allow breaks, or remove the clues.

Either way, predict how responses should change before you test the new procedure. The follow-up comparison then shows whether the fix really addresses the process the audit found.

There's one more situation where an audit can help: when an interim poll changes the process. First, a quick definition.

Bayesian updating is a standard way of revising your beliefs as new evidence comes in. If you start with the same beliefs and use a correct model of the same evidence, then reading two memos in either order should leave you with the same final beliefs.

People, though, can behave differently once they've publicly committed to an answer. So compare two procedures.

In silent review, people read memo one and then memo two, and then give their final view. The second procedure adds a poll between the two memos.

Reverse the memo order within both procedures. Compare the size of the order effect directly between the silent and polled procedures.

A difference between those effects is evidence that the poll changed the process. Finding a clear effect in one group and an uncertain effect in the other is not enough on its own.

Then test a polling procedure designed to address the change you found.

Let's recap the full sequence of an order-effects audit. Start with the business decision.

Choose two competing frames. Reverse their order across comparable groups.

Keep the complete pattern of answers. Calculate both the decision effect and q, with uncertainty ranges.

And use decision rules that you wrote down in advance. The same discipline applies when an AI system asks the questions, or when it plays the role of a synthetic respondent.

In those cases, the AI is part of the questioning process, so it has to be evaluated as part of the audit too. That's exactly where we'll pick up in the next module, which looks at how AI fits into human judgment.
