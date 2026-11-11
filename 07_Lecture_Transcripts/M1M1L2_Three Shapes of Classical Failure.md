# M1M1L2_Three Shapes of Classical Failure

Welcome back. In the last two videos we met a simple classical model, where questions just read answers that are already there, and we got a picture of how a quantum model works.

Now I want to show you three situations where the classical model runs into trouble. First, a quick point about how models go wrong, because there are really two kinds of mistakes.

Say your model forecasts 60 and the real number is 63. That's a miss, but you can probably fix it by improving your estimate.

Now say your model insists the answer has to be somewhere between 40 and 60, and the real number is 63. That's a different kind of problem, because the model said 63 couldn't happen, which means something is off in its basic assumptions.

Each of the three patterns in this lecture is that second kind. Each also has ordinary explanations we'll need to rule out, so think of them as warning signs rather than final verdicts.

Let's start with the first pattern, which I'll call an out-of-bracket result. A bracket is just a range with two ends.

Let's go back to our fraud reviewers. Suppose one group is asked to label each transaction first, as fraud or legitimate, and then decide whether to block it.

In our example, when they've labeled a transaction fraud, they block it 63 percent of the time. When they've labeled it legitimate, they block it 41 percent of the time.

Now take a second, similar group who skip the labeling step and just decide. To predict the second group, suppose each person has a settled fraud-or-legitimate judgment, even though we don't ask for it.

Also suppose the two block rates carry over unchanged when we remove the labeling step. Under those assumptions, the overall block rate should be a mix of 63 and 41, a weighted average that depends on how many lean each way.

If most lean fraud, it'll be close to 63, and if most lean legitimate, close to 41. Either way, it has to land somewhere between 41 and 63.

That range is what the classical model allows, and it's our benchmark.

Now suppose the direct group actually blocks 69 percent. That's six points above the top of the range, and no mix of 41 and 63 can ever get you to 69, no matter how you weight them.

So the classical model, with its fixed rates, fails here. Why might that happen?

One possibility is that the labeling step itself changes how people decide. Think back to the arrow picture from the last video.

Labeling a case snaps the judgment into place. Skipping that step leaves the arrow unsnapped, and that can lead somewhere neither route leads.

A quantum model describes this gap with something called an interference term, which we'll calculate later in the course. Other models can also let an assessment change the decision, though.

The math tells us which model failed. Figuring out why takes more evidence.

That's the first pattern. The second one is about the order of questions.

Picture a committee deciding whether to approve a new store. Question A asks whether the location has a strong market.

Question B asks whether it fits the brand. We randomly split the committee members into two groups.

We ask one group to answer A then B, and another to answer B then A, and we keep both answers from every person. Each person ends up in one of four boxes: yes to both, yes to A only, yes to B only, or no to both.

A table that shows how many people land in each box is called a joint response table. If the questions just read fixed opinions, the two orders should give us matching tables, apart from chance.

If they don't match, the order made a difference, and that's worth a closer look.

Of course, lots of ordinary things can make the tables differ. People learn as they go, they get tired, or they try to stay consistent with their first answer.

So how could we tell whether a quantum model fits better? It makes one very specific prediction, called the QQ equality, where QQ stands for quantum question.

In each table, add the share who said yes to both and the share who said no to both. Those are the people whose two answers agreed, so that total is called the agreement rate.

The QQ equality says the agreement rate should be the same in both orders, even if the individual boxes shift around. If the data match, the quantum model stays in the running, although some classical models can match it too.

If the data clearly don't match, that counts against this quantum model. We'll work through the numbers in Module 2.

Now for the third pattern, which is about a whole and its parts. The technical term is non-separability, but the idea is easier than the name.

Think about a guppy. Most people wouldn't call it a typical pet, because they picture a dog or a cat.

They wouldn't call it a typical fish either, because they picture something like a trout. Yet most people agree it's a very typical pet fish.

Putting the two words together changed the idea being judged. Businesses run into the same thing with product bundles.

Caldera, a software company we'll use as an example, sells a team chat tool and an audit-log feature. Customers rate each one as only so-so on its own.

Sold together, though, buyers see them as a compliance-ready workspace, which feels like a completely different product.

Those examples raise a real question: can a model that gives each part its own fixed value explain how people judge the whole? Before we say no, let's give the classical side a fair chance.

We can let its model include each feature's own value, plus what are called interactions, where one feature is worth more or less depending on whether the other is there. Then we test its predictions on new data it hasn't seen.

There's also a stronger test, borrowed from physics, called the CHSH inequality, after the four physicists who came up with it. You ask about each part in two different ways, which gives you four pairings, and for each pairing you measure how strongly the answers move together.

For this test, code each answer as plus one or minus one. The benchmark says one common table of possible answers describes all four pairings, with the same question meaning in each pairing.

Under those conditions, a particular combination of the four relationships can be at most 2 in absolute value. A reliable result above 2 challenges that common-table model.

Changing what a question means across pairings would break the comparison, so the design matters. It takes careful design to run this test, and a bundle that just feels greater than its parts doesn't break the ceiling by itself.

So we've now seen all three patterns. If you step back, you'll notice they have something in common: each one compares answers we got in different ways.

For the bracket, we compare people who acted directly with the range set by people who labeled first. For order, we compare complete answer pairs from the two sequences.

For wholes and parts, we compare judgments of the combination with what a model of the parts allows. In every case, the underlying question is the same: does the way we ask change the judgment?

When a prediction fails, it narrows down the list of models that could still be right, and tells us what a better model needs to explain.

So how do you run one of these tests well? I'd suggest four steps.

First, state the model's limit before you look at the results, so you can't move the goalposts later. Second, design a comparison that would actually show a break if there is one.

Third, estimate how much the number could move just by chance, since every sample has some random variation. And fourth, test the strongest alternative explanation you can think of.

These steps keep us from jumping to a quantum explanation just because a result looks surprising. And if you find no departure at all, that's useful too, as long as your estimate is precise enough.

In that case the simpler model stays a perfectly reasonable tool for that decision.

To sum up, a surprising number is interesting, but a result that falls outside a model's built-in limits is far more useful, because it tells you which models are still standing.

You now have three patterns you can test for directly: a result outside the bracket, answers that change with order, and a whole that doesn't follow from its parts.

In the next lecture, we'll look for a framework that can explain several of these patterns with a small set of ideas, make predictions in advance, and tell us honestly when the classical model is good enough.
