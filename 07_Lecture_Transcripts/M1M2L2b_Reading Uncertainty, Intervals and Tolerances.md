# M1M2L2b_Reading Uncertainty, Intervals and Tolerances

Before we run the QQ test, I want to take a few minutes for a tool we'll use again and again for the rest of the course: how to judge whether a number from data is trustworthy. You don't need any statistics background for this.

The ideas are simple, and once you have them, the next lectures will be much easier to follow.

Imagine you survey 100 customers and 52 percent say they'd sign up for a new service. If you surveyed a different 100 customers from the same market, you might get 47 percent.

Another hundred might give you 55. Nothing changed about the market.

You just happened to ask different people. That natural change from one sample to the next is called sampling variation, and it's in every number we calculate from data, including q.

So a single number on its own can't tell us much. We need a sense of how far it might move if we'd happened to ask different people.

Usually, we can't go out and survey new groups again and again. A method called the bootstrap helps us estimate this variation using the data we already have.

You take the people you already have and draw a new sample from them at random, the same size as the original. For our two-order comparison, do this separately within each order group.

After you draw each person, you put them back, so the same person can be picked more than once. Then you recalculate your number, say q, for that new sample.

Repeat that a thousand times or so. Each repeat gives a slightly different answer, and the spread estimates how much your number could vary from sample to sample.

This works when the sampling and resampling procedures fit the design. It won't repair a biased survey.

One rule for our tests: when you draw a person, keep both of their answers together, because q depends on the pairs.

From those repeats, one approach takes the middle 95 percent of the calculated results. That gives an approximate confidence interval, which we'll call an uncertainty interval.

It shows which values remain plausible given the sample and the method's assumptions. The 95 percent describes the method: over many new samples, about 95 percent of intervals made this way should contain the true value when those assumptions hold.

Say our estimate of q is 0.02, and the interval runs from minus 0.03 to plus 0.07. That tells us the true value could be a little below zero or a fair bit above it.

A narrow interval means our estimate is precise. A wide one means we're still quite unsure.

The last piece is a tolerance. Before collecting any data, you decide how big a difference from zero you'd still call practically small, say anything between minus 0.05 and plus 0.05.

Deciding this in advance matters, because it stops anyone from moving the goalposts after seeing the results. Then you compare the interval with the tolerance.

If the whole interval sits inside the tolerance, the departure is small enough for the practical standard you chose. This supports a small difference; it doesn't establish an exact zero.

If the interval is very wide, or it crosses one of the edges, the question is still open, and you may need more data. And if the whole interval sits outside the tolerance, the data challenge the prediction.

Our example interval, from minus 0.03 to plus 0.07, crosses the upper edge, so it would be unresolved.

Let's recap, because we'll use these ideas in almost every lecture from here on. Every estimate can vary across samples.

The bootstrap helps estimate how much. The uncertainty interval gives a range of plausible values under the method's assumptions.

And a tolerance, set in advance, tells you which departures would be small enough for your decision. In the next lecture, we'll put all four ideas to work and run the QQ test for real.
