# M1M2L3_The QQ Equality and Its Classical Rivals

We now have two tools: the arrow picture for predicting order effects, and uncertainty intervals for deciding how precise a result is. But order effects can also come from learning, memory, or a change in perspective, so seeing one doesn't tell us which explanation is right.

In this lesson, we'll look at a test that can help: the QQ equality. As a reminder, QQ stands for quantum question.

The standard quantum model of question order makes a very specific prediction. Take the share of people whose two answers match, meaning they said yes to both questions or no to both.

That share should be the same whichever order the questions were asked in. We work out the difference between those two shares, call it q, and the model predicts q equals zero.

If the data match, that supports this one restriction of the model. It doesn't prove the quantum model is the cause, though, because some classical models predict the same thing.

Let's walk through how to run the test. Start with two yes-or-no questions, A and B.

Randomly assign similar people to answer either A then B, or B then A. Keep everything else the same: the wording, the timing, and any information around the questions.

Everyone answers both questions. Then, for each group, count how many people gave each of the four possible answer pairs, and divide by the size of the group.

That turns the counts into shares, and the four shares in each table add up to one. One detail really matters here.

In both tables, use rows for A's answers and columns for B's answers, even for the group that saw B first. Keeping the same layout lets us compare the same answer pair across the two orders.

Now let's calculate the agreement rate. Start with the A-first table and add two boxes: yes-yes and no-no.

Those are the people whose two answers matched, so that sum is the agreement rate. Do the same for the B-first table.

One thing to be careful about: agreement here means agreement between one person's own two answers. It doesn't mean everyone agrees with each other.

Next, subtract the B-first agreement rate from the A-first agreement rate. That difference is q.

The other two boxes, yes-no and no-yes, are the two ways a person's answers can disagree. And since each table adds up to one, if agreement is equal across the orders, disagreement must be equal too.

So what does the quantum model actually allow? Under the standard model, the question lines and the starting arrow can be set any way you like, provided the same starting state and question definitions apply to both orders.

The prediction for q is still zero. That's what makes this test so useful: it doesn't depend on any settings we fit.

It does assume we use the same yes-or-no questions in both orders, and that the state updates by the arrow-and-shadow rule after each answer. Importantly, the individual boxes are still allowed to change.

For example, yes-yes might go down while no-no goes up by exactly the same amount. Then the agreement totals stay equal.

That's how you can see an order effect and still have the QQ equality hold. The model allows change, but it restricts how those changes balance out.

Let's try it with some example numbers. Read each table across the A-yes row first, then the A-no row.

For A then B, the shares are 0.36, 0.14, 0.16, and 0.34. The agreement rate is the yes-yes box plus the no-no box: 0.36 plus 0.34, which is 0.70.

For B then A, using the same layout, the shares are 0.31, 0.11, 0.19, and 0.39. Agreement is 0.31 plus 0.39, which is also 0.70.

Now subtract: 0.70 minus 0.70 equals zero. So even though every single box changed between the two orders, the agreement rate didn't, and q is zero.

In real data, you'll almost never get exactly zero, because every sample has some randomness. So we need a sense of how much q could bounce around.

One common method is called the bootstrap. You build a new sample by drawing people at random within each order group, putting each one back after drawing, so the same person can be picked more than once.

You recalculate q, and you repeat this many times. The spread of results gives you an uncertainty interval, a range of plausible values under the sampling and resampling assumptions.

Keep each person's two answers together when you do this. Before collecting any data, you also decide on a tolerance, which is the biggest difference from zero you'd still consider practically small.

Here, the tolerance runs from minus 0.05 to plus 0.05. Now compare the interval with the tolerance.

If the interval sits completely inside it, that supports a small departure. If the interval is very wide, or crosses the edge of the tolerance, the question is still open.

And if it lies completely above or below the tolerance, that challenges the model's prediction. The single number alone can't tell you which of these situations you're in.

Even if q passes, we still need to check the competition, so let's look at the classical rivals. One of the best known is query theory, which explains order effects through memory.

The idea is that a question makes people search their memory for reasons. The reasons that come to mind first are easier to use, and competing reasons become harder to recall afterward.

So reversing the questions can change the answer. This explanation is especially convincing when other evidence follows the same pattern, such as the thoughts people list, how long they take to respond, or memory tests.

A good audit writes down those predictions before collecting data. A detailed rival like this gives us something concrete to compare with the geometric model.

This is where it gets subtle. A memory explanation in general doesn't require equal agreement rates, but a particular version of it might still predict q near zero.

So we can't assume every classical explanation fails the QQ test. We need to spell out the rival and check what it predicts for the same tables.

If the equality fails and the memory evidence matches what the rival predicted, that favors the rival over the geometric model. If the equality holds, both might still be plausible.

In that case, we can compare their predictions on another task, or try a change to the procedure that the two explanations expect to have different effects.

Before you interpret any of this, there's one more thing to check: whether your measurement itself is biased. Systematic measurement bias means a part of your procedure that consistently pushes answers one way.

A leading question, scale labels that aren't balanced, or more people dropping out of one order than the other can distort one order more than the other and break the equality. If that happens, survey design becomes a competing explanation for the failed check.

So before you interpret q, check that the groups are balanced, that completion rates are similar, that the wording is fair, and that the answers look reasonable. If something differs between the groups, fix the comparison first, and only then use it to judge the explanation.

Let's put it all together into four possible outcomes. First, if the order effect itself is small and precisely measured, you can keep using the simpler process for this task.

Second, if the effect is meaningful and the q interval sits completely inside your tolerance, the geometric explanation stays in the running alongside its rivals. Third, if the effect is meaningful but the q interval sits completely outside your tolerance, that challenges the model's prediction.

And fourth, if the interval is too wide, you can't reach a verdict yet. Whichever branch you land in, check your measurement first.

Most important of all, write these rules down before you collect the data, and connect each one to a specific decision your client will make. In the next lesson, we'll use all of this to design a complete audit.
