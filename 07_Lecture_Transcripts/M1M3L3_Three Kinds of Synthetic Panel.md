# M1M3L3_Three Kinds of Synthetic Panel

In the last lecture, we asked how to test whether an interface helps shape a preference. Now let's consider a tool teams may use to explore questions like that: synthetic panels.

Imagine a client who wants a fast estimate of local support for a proposed data center. A survey of real residents is too expensive for early exploration, so the research team considers using language models that role-play as residents instead.

The first run is cheap, consistent, and nicely balanced across demographic groups. But those qualities describe how the panel was produced.

They don't show that it represents any real group of people. A synthetic respondent is really a language model working under a specific prompt, conversation history, settings, and persona, which is the character it's asked to play.

Its answers reflect those choices. So before using a panel's support rate for a business decision, we need to compare how different panel designs produce their answers.

Let's start with what needs to stay the same. Begin with one persona grid, which is just a table of fictional respondent descriptions that fit the market you're studying.

Each row might describe someone's age, job, whether they own a home, where they live, and their general view of development. Use the same grid in every panel.

Also keep the model version, the question wording, how answers are coded, and the timing of the runs the same. Keep the temperature the same too.

Temperature is a setting that controls how random the model's output is. These controls help us isolate the one thing we want to compare: the response procedure.

And remember, matching demographic labels doesn't make the model's answers representative of real people with those traits. What we're comparing is how the model behaves under carefully controlled descriptions.

Now let's look at the three panel designs, one at a time. The first gives the model everything at once.

In this ordinary panel, a single prompt contains the persona and the full set of questions. That can encourage the model to make all its answers sound consistent with each other, or to guess what the study is trying to find.

It can still produce a large order effect. In our made-up Fenwick data-center survey, the effect is fourteen percentage points, and q is 0.085.

That q is a warning sign, so we'd want to check its uncertainty interval against the tolerance we set in advance. The size of the main effect, on its own, tells us very little about whether the full pattern of answers fits the model we have in mind.

The second design takes away all earlier answers. We call this the classical panel, and you can think of it as an isolated-item baseline.

Each persona-and-question pair goes to the model in its own separate call, with no earlier questions or answers in view. You ask for one coded answer each time.

Because no call ever sees a sequence of questions, an order label alone shouldn't create any effect. That makes it a useful baseline.

It doesn't prove that the model holds a stable attitude inside, though. And answers stitched together from separate calls aren't the same as a real interview where questions follow one another, so keep that in mind when you look at statistics built from answer pairs.

The third design lets answers carry forward. In the constructed panel, each persona gets one sequential interview.

You present the two framing questions and then the main outcome question, and the earlier questions and answers stay in the conversation. Personas are randomly assigned to answer A then B, or B then A.

You ask the model to answer as the persona, without telling it what effect you're hoping to see. This design allows earlier answers to influence later ones.

It doesn't guarantee a quantum pattern, and it doesn't guarantee a human-like way of answering either. The QQ test, and a separately designed interference comparison, are what test the more specific predictions.

Next, the prompts. They need to keep these three designs distinct without handing the model the answer.

Tell the model how to answer, but leave the actual choice open. The classical prompt asks the persona to answer one item, without thinking about other questions.

The constructed prompt presents the items in order and keeps earlier answers in view. Neither prompt should mention the order effect you expect, the QQ value, or the direction of interference.

Giving the model those targets would be like handing it the answer key. Also keep the client's preferred result and the study's purpose hidden.

Record every system instruction, user prompt, model name, temperature, random seed if one is available, and the rule for when you retry a call.

Even clear prompts don't guarantee that runs are comparable. Synthetic runs can drift, which means their pattern of answers changes even when the prompts look the same.

Updates from the AI provider, hidden system instructions, sampling settings, the length of the conversation, and retry rules can all change the output. So generate all the comparison groups within a short time window, and shuffle the order of the runs.

Use the same demographic cells in every group. Decide in advance how to code answers that are garbled or too long, when to retry, and which response counts.

A panel you can reproduce needs a complete record of how it was generated, including the tools, versions, prompts, and any human decisions along the way.

That record also makes any changes traceable, so let's talk about how to store it. Keep one row for each answer a respondent gives to a question.

Each row should include a respondent ID, a persona-group ID, the panel design, the assigned order, the question, and the coded answer. Also keep the model version, a timestamp, and the prompt version.

Save the raw answer exactly as it came back, before you convert yes and no into numbers. With this table, you should be able to rebuild every interview, and spot missing answers, duplicates, or coding mistakes.

It supports the order-effect and QQ calculations. One caution: interference needs extra conditions, a direct condition and the assessed conditions, that a three-question interview may not include, so plan for those separately.

Now let's compare two of our illustrative panels side by side. The constructed panel has a fifteen-point main effect, and q is close to zero.

The ordinary panel has a fourteen-point effect, and q is 0.085. Their main effects look almost the same, but their QQ results are quite different.

Before reaching a verdict, we'd still need intervals, the tolerance we set in advance, and checks against rival explanations. The isolated-item panel gives us a baseline where we'd expect very little order effect.

Use examples like these to think through what different results could mean. And again, keep the prompts free of any instructions about what effect or q value the model should produce.

Let's wrap up. The three panel designs differ in what information the model gets to see.

The ordinary panel sees the whole question set at once. The classical baseline sees one question at a time.

The constructed panel carries its answers forward through an interview. Keeping the personas and settings the same is what makes this comparison meaningful.

Calculate the order effect and QQ from the right records, and add the extra conditions you'd need for interference. Most importantly, remember what these results describe: the response process of the model you tested.

To show that the same process happens in real people, you need a study with real people. That's the boundary we'll focus on in the next lecture.
