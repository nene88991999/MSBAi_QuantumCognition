# M1M3L1_Cognitive Asymmetry and the Intermediate Step

Welcome to Module 3. So far, we've looked at how the order of questions can shape people's answers.

In this module, we bring AI into the picture. Many companies now add an AI assistant to a review process.

Picture a fraud team: the model scores each case, an employee reads the score, and then the employee makes the final call. It sounds like a neat division of labor, where the model predicts and the person decides.

But the interface does more than show a number. It decides what the person sees first, which questions they answer, and whether they have to commit to an assessment before they act.

Each of those choices can shape the judgment that ends up in the final decision. So the real design question is this: which human response is the system helping to construct, and what does the organization do with it?

To see why this matters, think about what can and can't change during a review. The AI system usually runs on a fixed scoring rule.

One ingredient in training or choosing that rule is a loss function, which assigns a cost to mistakes. The training objective and the final decision threshold may play different roles, so the audit records both.

For example, how bad is it to block a legitimate payment, compared with letting a fraudulent one through? That rule stays the same from case to case.

The person reading the score, however, may respond differently depending on how the interface presents it. That's the cognitive asymmetry we're investigating in this lecture: a stable scoring rule sitting inside a human judgment process that can change.

An audit should test that possibility in the real workflow, and also check whether the model itself behaves differently in different contexts. Knowing that the score is accurate doesn't answer either question.

Let's make this concrete with three design choices that come up again and again when people work with AI. First, does the reviewer have to state an assessment, such as “this looks fraudulent,” before choosing an action?

Second, which consideration does the interface put front and center first? Third, does the team treat the reviewer's response as a preference that was already there, or as a judgment that formed during the interaction?

That last question is the detection-versus-construction distinction from Module 1. Each of these choices can change the state of mind the person decides from.

And because they help produce the final decision, they belong on the process map, right next to the model version, the data source, and the decision rule.

Here's an example we'll use for the rest of this lecture, a made-up company called Meridian Pay. It has two versions of its review screen.

The Direct console shows a suspicious transaction and asks the analyst to block it or allow it. The Assess-first console asks one extra question first: is this transaction fraudulent or legitimate?

Then it asks for the same action. Everything else is kept comparable: the case information, the model score, the pool of analysts, and their incentives.

The only designed difference is that extra assessment step. Now suppose the Direct console ends up blocking more transactions.

Can a simple mix of the two assessed groups explain that? That question gives us a clear benchmark to check before we reach for any psychological explanation.

So let's work out what a fixed-rate model allows. This is the bracket idea from Module 1, now applied to Meridian.

The benchmark assumes that the block rates we see after each assessment carry over, unchanged, to the Direct console. To build the prediction, take the block rate after a fraud judgment and multiply it by the share of cases judged fraud.

Then take the block rate after a legitimate judgment and multiply it by the share judged legitimate. Add the two together.

That's a weighted average, and because the two shares add up to one, it always lands somewhere between the two block rates. That range is what we call the classical bracket.

The averaging rule comes from a basic law of probability, called the law of total probability. Using it to predict the Direct console, though, depends on the key assumption that the block rates don't change when the assessment step is removed.

Now let's put in some numbers. Suppose that in the Assess-first console, analysts block 63 percent of cases after judging them fraud, and 41 percent after judging them legitimate.

Suppose about eighteen out of every twenty-two assessments are fraud judgments, and the other four are legitimate. Weighting the two block rates by that mix gives an average of 59 percent, which matches Assess-first's overall block rate.

Now the Direct console: it blocks 69 percent. That's more than the weighted prediction.

In fact, it exceeds even the higher of the two block rates, so it's outside the bracket altogether. No change in the mix of hidden fraud and legitimate judgments can get you to 69 percent, because every possible mix stays between 41 and 63.

The arithmetic flags the problem before we choose any psychological explanation.

There are actually two separate comparisons here, and it's worth keeping them apart. The first is the interference estimate, which is simply the direct rate minus the weighted prediction.

Here, that's 0.69 minus 0.59, which is positive 0.10. Now imagine a different result, where the direct rate came out at 0.49.

That would give negative 0.10 against the same prediction. The two differences are the same size, but only 0.69 falls outside the bracket from 0.41 to 0.63.

The 0.49 rate is still inside it. So a nonzero interference estimate and a bracket violation are two different findings, and you should report both, each with its uncertainty.

To get that uncertainty, use the bootstrap from Module 2: repeatedly resample whole respondents, with replacement, and recalculate, keeping each person's assessment and action together.

So what's going on in a construction account? The idea is that making the assessment explicit changes the state of mind the analyst acts from.

In the Direct console, she acts while her assessment is still unresolved. In Assess-first, she has to commit to one before acting.

A quantum model can describe that difference as interference between the possible paths her judgment could take, much like the arrow picture from Module 1. One subtle point here.

Assess-first's overall block rate always equals the weighted average of its own two block rates. That's just arithmetic, not evidence for anything.

The question you can actually test is whether a comparable Direct group differs from that prediction, and whether the proposed model correctly predicts how it differs.

It's also important to be clear about what the bracket does and doesn't rule out. It rules out one type of explanation: those that only change the mix of judgments while keeping the two assessed block rates fixed.

It doesn't rule out every anchoring or learning explanation. Take what's called an exemplar model.

An exemplar is a remembered case that you use as a reference. A two-stage exemplar model lets the first assessment change which remembered cases, or which features, guide the later action.

A model like that can produce results outside the bracket too. Meridian's example also raises a practical concern: Assess-first analysts say they trust the AI more and override it less.

So the firm should test both the quality of the decisions and how much people rely on the AI, while comparing the competing explanations.

Let's sum up. The intermediate-step audit turns a workflow design choice into something you can test.

Write down the unchanged-rate benchmark, compare the Direct and Assess-first consoles, and calculate both the gap from the weighted prediction and the bracket comparison. Then test the strongest rival explanation.

Just as important, decide who is responsible for the order of the questions, the timing of the AI's advice, and the action taken after each audit result. The same kind of responsibility comes up in recommender systems, where the opening screen may change which of a user's goals gets attention.

That's where we're headed in the next lecture.
