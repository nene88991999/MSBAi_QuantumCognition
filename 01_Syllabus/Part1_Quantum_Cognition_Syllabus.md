BADM 590  ·  Quantum Approaches for Decision Making

Part 1: Quantum Cognition for Human-AI Decision Teaming

Spring 2027  ·  2 credit hours  ·  4 weeks  ·  MSBAi, Gies College of Business, University of Illinois Urbana-Champaign

Instructor: Nathan Yang  ·  Eight 90-minute sessions, two per week  ·  Roughly 10 to 11 hours of student effort per week

Course Description

A manager may receive different answers to the same question when its wording, position, or preceding discussion changes. The decision is whether to redesign that process, improve a conventional model, or use a model that represents how judgments develop during questioning. This course compares these explanations. A classical probability model assigns probabilities to specified events; a fixed-preference version assumes that asking a question reveals an answer without changing it. Quantum probability provides another mathematical representation in which the sequence of judgments can change the predicted answer. Students examine the restrictions of each model and compare their predictions with evidence.

The applications concern surveys, recommendation systems, and human review of AI advice. A system can influence a decision through the questions and intermediate judgments it requests. The course examines these design choices without assuming that AI systems are rational or that a particular model explains all human judgment. No physics background is required. The core explanations use arithmetic, and guided Python notebooks provide the calculations.

Learning Outcomes

| Learning Outcome | Level |
| --- | --- |
| Explain how a quantum probability model represents judgment and when its predictions provide a useful comparison with a specified classical model. | Literacy |
| Identify question-order effects, constructed preference, and direct-versus-assessed differences, and state the assumptions needed to interpret each. | Literacy |
| Evaluate how an AI-supported decision process changes the questions, sequence, and goals presented to a person. | Competency |
| Document how an analytical judgment changed across the project, including the evidence that prompted the revision. | Competency |
| Design and execute an audit of an AI-generated respondent panel for a real firm and defend a recommendation within the scope of the collected evidence. | Expertise |

Schedule

| Week | Live Session (90 min) | Project Studio (90 min) |
| --- | --- | --- |
| 1 | Module 1. Why classical models break down. Detection versus construction; the measurement story and its hidden assumption; what a catalog of biases cannot do. | Company selection and problem framing. Instructor sign-off on scope. |
| 2 | Module 2. Contextuality and order effects. Sequential judgments; the QQ equality as one testable restriction; classical rivals; intervals and practical tolerances. | Battery design and proposal workshop. Part 1 due end of week. |
| 3 | Module 3. Human-AI decision teaming. Elicitation by systems; synthetic respondents; the audit statistics and the Tier 2 boundary. | Panel generation, audit troubleshooting, and peer critique of preliminary results. |
| 4 | Individual presentations and oral defense. Ten minutes each, followed by five minutes of questions. Additional blocks are needed if there are more than six presenters. | Debrief and synthesis: what patterns held across audits, and where the framework did not apply. Part 2 due end of week. |

Individual Project: A Synthetic Panel, Audited

The project runs in two parts and is individual throughout. Choose a real, publicly documented company decision and audit how an AI-generated respondent panel answers a short survey under different procedures. The evidence concerns the tested model, prompts, and persona grid. Any proposal to replace human respondents requires separate evidence from the relevant human population.

Part 1. Research proposal (due end of Week 2). Identify the management decision and translate it into a research question. Explain why a synthetic panel could help with preliminary investigation. Ground two competing frames in public evidence about the market, then specify two framing questions, A and B, and one focal question, F. Name the strongest plausible alternative explanation and a fair test that could distinguish it. Freeze the wording, coding, collection conditions, and decision thresholds before examining results. State what the company should do after a clear result, a practically small result, or an inconclusive result. The detailed instructions are in M2A2_Project_Part_1.

Part 2. Audit report, deck, and oral defense (due end of Week 4). Use the same persona grid in all six conditions: isolated A/B and B/A interviews, constructed A/B and B/A interviews that retain prior answers, a direct F-only condition, and an assess-first A-then-F condition. The last two conditions support the interference and bracket comparisons. Compute the focal order difference, the QQ statistic, and the direct-minus-assessed difference, with intervals that preserve the sampling structure. Assess alternative explanations and recommend an action supported by the evidence. Document changes from the proposal. Submit the report, executed notebook, records, 6–10 slides, and logs described in M4A1_Project_Part_2; present for ten minutes followed by five minutes of questions.

Assessment

| Component | Weight | AIAS | L-C-E |
| --- | --- | --- | --- |
| Three diagnostic discussions, each including a post and peer response | 30% | 2 | Literacy |
| Project Part 1: research proposal | 25% | 3 | Competency |
| Project Part 2: audit report, deck, and oral defense | 35% | 4 (defense: 0) | Expertise |
| Reflection memo (800 words) | 10% | 1 | Expertise |

AI Policy

Each assessment declares a level on the MSBAi AI Assessment Scale: 0 no AI, 1 brainstorming only, 2 drafting with human revision, 3 collaboration with disclosure, and 4 AI as the subject of analysis. Project Part 2 is Level 4, with permitted assistance and disclosure specified in its instructions. The oral defense is Level 0. The reflection is Level 1: write the submitted reflection yourself.

Every project submission carries an AI Attribution Log recording the tools and model versions used, the prompts submitted, and how your judgment modified or overrode what came back. The log is graded. Within each part, do your own framing before you consult a model, and check what the model gives you against the institutional record afterward.

Materials, Tools, and Course Policies

No textbook purchase is required. The repository provides short module notes adapted from Quantum Cognition for Management (Yang, manuscript), lecture transcripts, and a reading guide linking journal articles, author manuscripts, and tutorials. Begin with the suggested introductory readings. Technical and extension readings are optional unless Canvas assigns them.

Use Python notebooks in Colab, Jupyter, or VS Code. The introductory examples and practice audit need NumPy and make no model calls. Project data collection uses the course-approved model access and budget; the audit starter analyzes saved records. Submit through the Canvas assignment link, including a repository link when requested. Keep graded submissions and raw interviews in the approved private location. Exact dates and course-wide grading arrangements are posted in Canvas.

Regular live-session and studio attendance is recommended and is not graded separately. Modules 1–3 each have one assessed discussion post and one peer response. The individual presentation and oral defense in Module 4 are required components of Project Part 2. All assessments in Modules 1–4 are individual. The assessment weights sum to 100% within this four-module part; the full-course syllabus governs its contribution to the eight-module course grade.
