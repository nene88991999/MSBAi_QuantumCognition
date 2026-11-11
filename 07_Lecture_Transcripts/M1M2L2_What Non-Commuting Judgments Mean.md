# M1M2L2_What Non-Commuting Judgments Mean

In the last lesson, we said that some questions are non-commutative, meaning the order you ask them in can change the result. In this lesson, I want to show you exactly what that looks like, using the arrow picture from Module 1.

Let's go back to a manager evaluating a proposal for its opportunity and its risk. If she thinks about opportunity first, her attention goes to growth.

If she thinks about risk first, her attention goes to possible losses. Both questions are about the same proposal, but her first answer can change how she approaches the second.

A model where the order of these steps matters is called non-commutative. In plain terms, doing A and then B can give a different result from doing B and then A.

The arrow and its shadows let us see this happen, and even calculate it.

In Module 1, the arrow was just a picture. Now we'll use it to calculate.

Let's represent the decision maker's current state of mind as an arrow of length one. Then, for question A, we draw two lines at a right angle to each other.

The horizontal line stands for yes, and the vertical line stands for no. The arrow casts a shadow on each line.

Here's the rule: to get the probability of answering yes, take the length of the shadow on the yes line and square it, which just means multiplying it by itself. In our example, the yes shadow is one half.

One half times one half is one quarter, so there's a 25 percent chance she says yes. If you're wondering where the one half comes from, it's because the arrow points sixty degrees away from the yes line.

You won't need to calculate angles yourself in this course. The key idea is that the arrow's direction sets the shadows, and the shadows set the probabilities.

Now let's bring in question B, which has its own yes and no lines. In the simplest case, B's lines point the same way as A's.

That's the compatible case. More generally, compatibility means the two question operations can be swapped without changing the model's result.

One table of answer pairs then describes both orders. Reversing the order leaves the whole pattern of probabilities unchanged.

Think back to the bank checking an account balance and a fixed age rule. Asking about one doesn't change the other.

Compatibility is the situation where the quantum model behaves exactly like the classical one. One caution, though.

If you see only a small order effect in real data, that fits with compatibility, but it doesn't prove it.

Let's go back to question A and follow what happens step by step. Suppose the answer is yes.

In the model, we keep just the part of the arrow that lies along the yes line, which is its shadow. That shadow is shorter than one, so we stretch it back to length one.

This stretching step is called normalization. All it means is that we're now describing her new state of mind, after she said yes.

Next, we evaluate question B, using this updated arrow and B's lines. If B's lines are tilted compared with A's, the shadows on B are now different from what they would have been from the original arrow.

And if we'd asked B first instead, the arrow would have snapped somewhere else to begin with. Either way, the second question starts from a different place, depending on which question came first.

There's a short way of writing these two paths. A followed by B is written AB, and B followed by A is written BA.

When the two steps commute, swapping them gives the same result. When they don't commute, the two orders can give different answer pairs.

The key is the update after the first answer: the second question always works on the updated state. I should add a caution here.

Classical models can also describe a state that changes over time, so the fact that order matters doesn't, by itself, prove the quantum model is right. To tell them apart, we need the quantum model's extra predictions about the pattern across both orders, and we'll get to the most important one shortly.

This graph shows what the model predicts in one particular situation. The height of each curve is the probability of saying yes to both questions, with one curve for each order.

Across the bottom, we change the angle between the two questions' lines, from perfectly lined up on the left to ninety degrees apart on the right. Throughout, the starting arrow stays fixed at sixty degrees from A-yes.

Wherever the curves pull apart, the two orders predict different probabilities. Notice that where the questions line up, the curves meet, so there's no order effect.

Also notice that the gap doesn't simply grow as the angle grows. It depends on both the angle and where the arrow starts.

With a different starting arrow, the curves would separate differently.

The same idea applies to people. Compatibility isn't a fixed trait of a person.

It's a property of a particular pair of questions in a particular task. The same evaluator might answer one pair of questions with no order effect at all, and another pair with a clear one.

These three small diagrams show that: lines perfectly lined up, lines tilted by twenty degrees, and lines tilted by forty degrees. It's the same model each time, just with different settings.

For a manager, this raises a practical design question. Should your process set strategic goals before assessing risk, or set risk limits first?

There isn't one right answer for every situation. Choose the order that serves the decision, test it, and write down why you chose it.

Keep in mind that these curves show what the model predicts. Real order effects can come from lots of everyday causes.

Memory plays a role. So does anchoring, which means leaning on an earlier answer.

New information, fatigue, and clues about what a study is looking for can all create order effects too. What makes the geometric model distinctive is that it makes one extra, very specific prediction: the agreement rate should be the same in both orders.

That's the QQ equality we met in Module 1. If the difference is close to zero and the uncertainty range is narrow enough, that supports a small departure from this restriction.

Some classical processes can meet it too, so we still compare their predictions. And if the check clearly fails in a well-designed study with good measurement, that counts against the model.

Let's look at the graph once more, at the point where the lines are aligned. This shows how the classical case fits inside the quantum picture.

When the two steps commute, the order effect disappears, and one ordinary probability table works for both orders. But be careful: a small gap in real data can also come from random noise, or from a particular starting point, even when the questions aren't fully compatible.

That's why we always look at uncertainty and test more than one prediction. If the simpler model describes the decision well enough, use it, and keep your conclusion specific to the questions and setting you actually tested.

Before we calculate the QQ test, the next short lesson will explain how we judge uncertainty in a number. After that, we'll work through QQ step by step.

Here's a preview of the calculation. First, build a four-box answer table for each question order.

In each table, add the yes-yes box and the no-no box. Those are the people whose two answers agreed.

Then subtract the agreement rate for the B-first order from the agreement rate for the A-first order. We call that difference q, and the model predicts it's zero.

We'll work through an example, see how much uncertainty surrounds the result, and compare the quantum explanation with classical alternatives.
