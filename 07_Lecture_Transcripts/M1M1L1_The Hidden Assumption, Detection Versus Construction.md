# M1M1L1_The Hidden Assumption, Detection Versus Construction

Hi everyone, and welcome to the first lecture of this module. I want to start with a situation you could easily run into at work.

A fraud analyst is looking at a payment the system has flagged. She reads through the case and decides to block it.

Her company saves that decision, and later it may use decisions like hers to train its next fraud-detection model. So what exactly did the company save?

Most of us would assume she already had an opinion about the payment, and the review simply recorded it. But maybe the order she saw the evidence in, or a question the system asked her a minute earlier, helped her make up her mind.

The same question applies to a committee approving a new store, or a shopper choosing a phone. Was the answer already there, or did the process help create it?

That's what this lecture is about.

Let's look at the two possible answers one at a time. I'll call the first possibility detection.

In research, an explanation like this is called an account, so you'll hear me say “the detection account.” The idea is that the person's preference already exists, and a question just reads it, the way a thermometer reads the temperature of a room. The temperature was there before you looked, and looking doesn't change it.

A lot of business tools work on this assumption: product surveys, recommender systems, and most onboarding forms. A well-designed question reads the preference accurately, and a badly designed one adds some noise.

Under this explanation, a larger sample can reduce random noise. A leading question can still create a systematic error, so question design matters too.

The key assumption, and the one that's easy to miss, is that asking doesn't change what you're measuring.

To make this more concrete, picture a shopper choosing between two phones. If detection is right, she already has an opinion about each phone's price, battery, and camera.

You could imagine writing those opinions into a small table before you ask her anything. Then, when you ask about price, you're just looking up one cell in that table.

Ask about the camera, and you look up another. Now think about what that means.

If questions only look things up, the order you ask them in shouldn't matter. Price first or camera first, you'd get the same answers, apart from a little random noise.

That expectation is what I'll call a benchmark. A benchmark is simply the result a simple model tells us to expect, so we have something to compare real data against.

Classical probability is the ordinary way of assigning chances to possible outcomes and combining them. It supports many different models, including models of learning.

Here we're testing one simple classical model: questions just read answers that hold still. We'll call that the fixed-answer benchmark.

Keeping this distinction in mind will help us say exactly which assumption a result challenges.

So that's detection. Let's go back to our two possibilities and look at the second one.

The second possibility is construction. Here, the judgment isn't fully formed when the questions start.

It forms as you answer. Think about our shopper again.

She might not know how much she cares about battery life compared with the camera until she's holding both phones and comparing them. Or think about a manager deciding how much risk she's comfortable with.

She may not have a firm number in mind until the examples, the comparisons, and the order of the questions make some risks feel more real than others. Her answer is still genuine, and it still matters.

It just depends on the context it was given in. And if our questions helped shape it, then some of the responsibility for that answer belongs to whoever designed the questions.

Why does this matter for a manager? Because the same recorded answer can come from either process, and the two lead to different questions about your data.

With detection, you ask: did we measure accurately? With construction, you also have to ask: which answer did our design help produce?

Let me give you an example. Suppose two versions of an onboarding flow lead similar customers toward different investment portfolios.

If the difference persists in a fair comparison, it may reflect the design of the flow. It's part of the product you're shipping, and you need to know whether it actually serves your customers' goals.

If you treat every answer as a fact the customer walked in with, the effect of your own design disappears from view.

Let's make that even more concrete with a financial app, one I've made up for this course. The app asks about your goals first, then your risk tolerance, and then it recommends investments.

Imagine a customer whose first choice is “Protect my family.” With her family on her mind, losing money feels like a bigger deal, so she picks a low risk level, and the app gives her a cautious mix of investments. Now rewind, and imagine the first screen had offered “Build wealth” instead.

Now she's thinking about the opportunities she might miss, so she picks a higher risk level and gets a growth-oriented mix. Same person, same app, two different paths.

And notice something we never got to see: how she would have answered with no goal question in front of her at all. To find that out, we'd need a separate comparison.

The same issue shows up when people work alongside AI, which is becoming more and more common. Picture a fraud review tool where the system summarizes each case for the reviewer.

It decides which piece of evidence she sees first, and sometimes it asks a follow-up question that nudges her toward one way of looking at the case. Then she makes her call, and that call gets saved as a label.

A label is just the recorded answer that a future model will learn from. If the interface helped shape her judgment, then that label really has two contributors: the reviewer and the interface.

That can still be good data, as long as we treat it as the result of a designed process. The trouble comes when we file it as “human ground truth,” meaning the correct answer according to a person.

That gives her all the credit and hides the part the system played.

And it doesn't stop there, because these labels get reused. A scoring model learns from reviewers' past decisions, and a recommender learns from people's clicks.

If a prompt or a screen helped produce those responses, then the effect of that design ends up baked into the training data. The next model might predict those responses really well, while the company still misunderstands what they mean.

Collecting more data won't fix this on its own. More data can describe behavior under the current process more precisely.

It doesn't automatically tell you what a different process would produce. To learn that, you have to actually compare processes and see whether the same judgment shows up when the interface changes.

So how would you check which process is going on? You'd run what I'll call an audit, which is just a planned test of whether a judgment stays the same across different reasonable ways of asking.

There are a few simple ways to do it. You can reverse the order of two questions.

You can change which consideration people see first. Or you can compare a decision made right away with the same decision made after an assessment.

Keep everything else the same, and make sure the groups are comparable. If the answers shift, that points toward construction, but it isn't the only possible cause.

People sometimes learn something from the first question. They might remember what they said earlier and try to stay consistent.

And some people give the answer they think the researcher wants to hear, which is called a demand effect. A good audit plans ahead for how to tell these explanations apart.

Let me wrap up with the one question I'd like you to carry into every decision you study. It comes down to this: can one fixed answer explain how people behave across all these different ways of asking?

If yes, the simpler model is probably good enough for that decision. If no, it's time to consider a broader model.

That might be a model of learning, a model where the way people respond can change, or quantum probability, which we'll picture in the next video. Keep in mind that stability belongs to a specific judgment in a specific setting.

A customer's shoe size doesn't change while she's browsing, but her taste in styles might.

After the next video, we'll look at three warning signs that the simple model is breaking down: a result outside the range it allows, answers that change with question order, and a judgment about a whole that its parts can't explain.
