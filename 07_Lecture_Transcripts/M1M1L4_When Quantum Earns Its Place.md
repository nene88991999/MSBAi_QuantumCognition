# M1M1L4_When Quantum Earns Its Place

Welcome back. Over the last few videos we've covered a lot of ground: detection and construction, the bracket, order effects, and the arrow picture of a quantum judgment.

In this video I want to step back and ask a practical question. Suppose someone on your team says, “We should use a quantum model for this.” How would you decide whether that's a good idea?

My answer is that a model has to earn its place. It should help you predict what people will do, or help you make a better decision, and do it better than the tools you already have.

To show that, it has to make predictions that could turn out to be wrong. Let me walk you through what that looks like.

I'll begin with a difference that's easy to blur: explaining results you already have, and predicting results you haven't seen yet. Think about a student who memorizes the answers to last year's exam.

She'd score perfectly on that exam, but it tells you almost nothing about how she'll do on a new one. Models can fall into the same trap.

If a team adjusts its model separately for every dataset, each one can look like a great fit, and you still don't know whether the model understands anything. A better approach has two steps.

First, the team uses earlier tasks to set the model's settings. In the arrow picture, those might be the angle between two questions and where the arrow starts.

Then, before any new results come in, the team writes down what the model predicts for the next task, and compares. If they go back afterward and adjust the settings to match what happened, that's called refitting.

Refitting can improve a model, but it's a bit like changing your exam answers after seeing the answer key. It doesn't count as a prediction.

With that in mind, let's look at three tests a quantum model should be able to pass. The first one is the cleanest, because the model doesn't get to adjust anything.

Remember the store committee answering two questions in two different orders? For each order, we take the share of people who said yes to both questions and the share who said no to both, and add those two shares together.

That total is the agreement rate. The standard quantum model we're testing makes a firm prediction: the agreement rate should be the same in both orders.

We call the difference between the two agreement rates q, so the prediction is simply that q equals zero. A setting the model learns from data is called a parameter, and this prediction doesn't depend on any of them.

That's what makes it a tough test: no choice of angle or starting arrow can rescue the model if q comes out far from zero. If q comes out close to zero and is measured precisely enough, that supports this prediction.

It still leaves other explanations in the running. In Module 2 we'll learn how to judge that precision.

So that's our first test, and you'll see it here as the first of three. The second test is transfer, which means taking what the model learned in one situation and using it, unchanged, to predict another.

Here's how that might look in a business. Say your investment app asks about goals before it asks about risk, and you've measured how much that order shifts people's answers.

A related survey, maybe for retirement planning, asks similar questions. Transfer means using the same settings from the app to predict what will happen in the survey, before you run it.

If the prediction holds up, that's good evidence one explanation covers both situations. And if it fails, you've still learned something useful, because you've found where the model stops working.

The third test asks whether making the questions compatible removes the order effect. If a model really understands why an effect happens, it should be able to tell you what would make the effect go away.

Let's go back to the manager who rates a proposal for opportunity and then for risk. Suppose the explanation is that those two questions pull her thinking in different directions.

Then giving her one shared scorecard for both might bring the questions into line, and the order effect should shrink. What matters is that the team says this before testing it, and explains why that particular change should work.

Clearer wording or a longer pause can be useful changes, but the team still needs to explain which process each change is meant to affect. Then you run the old process and the new one, each in both orders, and see whether the effect really disappears.

If it doesn't, either the explanation or the fix needs another look.

Now, it's worth being careful about what a failed test actually tells you. A quantum model isn't the only alternative to the simple fixed-answer view.

Prospect theory, which you may know from other courses, explains choices in terms of gains and losses compared with a reference point, and it lets people weigh chances in their own way. It doesn't use quantum probability at all.

In the same way, a result outside the bracket rules out one specific model: the one that assumes people's response rates stay the same no matter how you ask. Models where the way people answer can change are still possible.

So when something fails, be precise about which model failed, and then let the three tests decide how much credit the quantum explanation deserves.

Before we wrap up, I want to clear up a common misunderstanding, because you'll probably run into it. Quantum cognition is a way of modeling behavior.

It uses the math of quantum probability to describe how people answer questions. It doesn't claim that our brains are quantum computers, or that neurons are in some strange physical state.

The model can be useful even if the brain works in completely ordinary ways. So judge it on what it predicts about people's answers, because that's what it was built to do.

Part of the confusion comes from the word quantum itself, which shows up in at least four different fields. Quantum cognition, the one we're studying, models judgments.

Quantum computing builds physical machines that use quantum effects to do calculations. Quantum game theory studies strategy when players follow special quantum rules.

And quantum-inspired machine learning borrows some of the math to build learning algorithms, usually on ordinary computers. These fields share a word, but each one needs its own evidence.

A breakthrough in quantum computing tells you nothing about how people make judgments, and a good model of judgment tells you nothing about computers.

So let's bring this back to you as a manager. If someone brings you a proposal to use a quantum model, here are three questions you can ask.

First, is the test clear? The proposal should say up front what the simple model allows, which number they'll measure, and what the strongest competing explanation is, all before anyone looks at the data.

Second, could the test actually prove the model wrong? Look for predictions that were fixed in advance, not settings adjusted afterward.

Third, would the result change what you do? A good proposal says what action follows a strong result, a weak one, or an unclear one.

If a proposal can answer all three, you have something concrete enough to evaluate, and to fund.

Let me pull all of this together. When you're studying a judgment, first check whether the simple, fixed-answer model can explain what you see.

If it can't, look at explanations that let the asking process change the answer.

A quantum model earns its place by making predictions that could fail, and then passing them: the QQ prediction holding within a carefully chosen tolerance, a prediction that transfers to a new task, and an order effect that disappears under the specified change.

In the next module, we'll put this into practice with the most manageable test there is: reversing the order of two questions and seeing what happens.
