# M1M3L2_Which Self the Recommender Optimizes

In the last lecture, we saw how an AI review screen can shape a human decision. Now let's look at a system many of you use every day: a recommendation feed.

Imagine a made-up shopping app called Juno. One version of its feed opens with “Popular near you.” Another opens with “Your goals this month.” With the popularity opening, shoppers pick impulse items 68 percent of the time.

With the goals opening, they pick goal-aligned items 61 percent of the time. It's tempting to subtract one from the other, but be careful: these percentages measure two different outcomes.

One counts impulse buys and the other counts goal-aligned buys, so the gap between them isn't a measure of the opening's effect. What these numbers do is give us a reason to look closer, by comparing the same outcomes under each opening, and by testing whether one stable set of preferences can predict both.

To test that, let's start with one common recommender model. It describes each user with a stable set of hidden preferences, and each item with a set of features.

The better the match between the two, the higher the item's score. More advanced systems, called context-aware systems, also use information about the situation, like the time of day, your location, or your device, but they still use one fixed scoring rule.

This works well when one set of goal weights explains your behavior across all those contexts. More relevant data can sharpen the estimate, and the system is checked by testing its predictions on choices it didn't see during training.

For the stable-preference benchmark we're testing, the key assumption is that your preference already exists before you open the app, in a form the system can recover. Other recommender models can allow preferences to change.

In other words, it treats the interaction as detection.

Let's make that concrete. A shopper might care about price, quality, novelty, and sustainability.

A classical model can describe those goals with one stable set of weights, meaning how much each goal matters to her. If those weights predict her choices across the different question orders we test, within normal error, then the model may be all we need for this task.

The recommender can estimate her trade-offs and check its predictions on new choices. But if one set of weights fails across the different openings, and we also see an order effect, that's a reason to look more closely at how the interface is affecting her judgment.

Simply having many goals doesn't tell us much about that process on its own.

So we can investigate this with two checks. First, estimate one stable set of goal weights and test whether it predicts choices it wasn't fitted on, under both openings.

Second, reverse the goal question and the price question across comparable users, and compare their full answer tables. Put those two checks together and you get four possibilities, which you can see in this grid: the weighting either fits or fails, and the answer pattern either stays stable or changes with order.

The lower-right box, where the weighting fails and there's also an order effect, is the one that calls for more testing. That's where the QQ test and specific predictions from rival explanations help narrow things down.

Neither check, on its own, tells you the cause.

When those checks suggest the interface is shaping the judgment, a construction explanation becomes believable. Think about the two openings.

“Popular near you” may make an immediate reward feel more vivid. “Your goals this month” may turn attention toward longer-term aims.

Whatever the shopper focuses on first then affects how she judges the next item. That creates a practical risk.

A model that averages all these responses into one stable preference might predict well with the old interface, and then fail badly after a redesign. Testing different openings shows whether the stable-preference model is good enough.

Keep in mind that learning, habit, and other explanations where preferences change over time are still possible rivals.

There's another way a product can lock in a particular frame: through the way it measures success. A metric is just the number a team uses to judge how well the product is doing.

An engagement metric, such as clicks or time spent in the app, may reward the popularity opening, because it produces more impulse choices. A goal-completion metric may reward the goals opening, because it produces more goal-aligned choices.

The diagram follows those two loops. A third option is to let users choose the mode themselves.

None of these choices, on its own, tells you which outcome is actually best for users. The team has to state what the product is for, measure outcomes that matter for users' wellbeing, and test whether the interface it picked really serves that purpose.

Giving users control is one good response. The app could invite the shopper to pick a temporary mode, like “Shop my goals” or “Explore what's popular,” and keep that choice for the rest of the session.

That makes the frame visible and creates a record that the shopper chose it. It also lets the team test later whether chosen modes lead to more lasting satisfaction, fewer reversals, and less regret.

Defaults still matter, though, so the order and wording of the mode choices need their own audit. Overall, people have more real choice when they can see the different perspectives available, and understand how the feed will rank items under each one.

Classical explanations of how preferences get shaped reach a similar conclusion by a different route. Repeated recommendations can teach people, persuade them, build habits, or even manipulate them.

There's also a technique called reinforcement learning, where a system learns by being rewarded for certain actions. If it's rewarded for engagement, it can change what it recommends, and that in turn changes how users behave later.

You'd measure effects like these by tracking behavior over time, what people were shown, and how satisfied they are afterward. Incompatibility makes a narrower claim.

It says that question order can change the pair of answers within a single interaction, and the QQ test limits what that change can look like. Both views might lead to similar safeguards, but they make different predictions, so compare those predictions before deciding which explanation is right.

Those predictions tell you what your audit needs to record. Before collecting any responses, define the users, the frames, the main outcome, and the stable-weight benchmark.

Randomize the order of the framing questions, and keep both framing answers along with the later choice. Then test how accurately the model predicts held-back choices, calculate the order effect and q, and look at what each user was shown and any problems with the interface.

As in Module 2, decide in advance what you'll do for each of four outcomes: the simpler model works; the model fails but QQ still fits the geometric model; the order pattern breaks QQ; or the evidence is too imprecise. Compare rivals before naming a cause, and tie each outcome to a specific interface decision.

Let's wrap up. A recommender can be estimating a stable target, your preferences, while its own interface is shifting the judgment that defines that target.

If your trade-offs stay stable, the classical model is fine. But if a stable-weight model fails across openings, and answers also depend on question order, construction becomes a serious possibility.

In the next lecture, we'll look at three ways to test that possibility using synthetic panels, where an AI plays the role of survey respondents: isolated calls, sequential interviews, and an ordinary all-at-once prompt. Comparing them reveals which response process a panel is actually producing.
