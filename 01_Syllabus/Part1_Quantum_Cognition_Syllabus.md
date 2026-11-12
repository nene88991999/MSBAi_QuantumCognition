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
| 4 | Team audit presentations and individual oral defenses. Ten minutes per team plus five minutes per member. Schedule additional blocks when needed. | Team revision of the report and individual reflection. Part 2 and reflection due at the end of the week. |

Team Project: A Synthetic Panel, Audited

The project runs in two team-based parts, with a separate individual oral defense. Use the team assigned in Canvas to audit a real, publicly documented company decision. Submit one proposal, report, deck, executed notebook, and set of supporting records per team. Record member contributions and have another member check substantive work. Every member should understand the full audit. The evidence concerns the tested model, prompts, and persona grid. Any proposal to replace human respondents requires separate evidence from the relevant human population.

Part 1. Team research proposal (due end of Week 2). Identify the management decision and research question. Explain why a synthetic panel could support preliminary investigation. Ground two competing frames in public evidence, then specify framing questions A and B and focal question F. Name the strongest plausible rival and a fair test. Freeze the wording, coding, collection conditions, and decision thresholds before examining results. State the company action after a clear, practically small, or inconclusive result. See M2A2_Project_Part_1.

Part 2. Team audit report and deck with individual oral defense (Week 4). Use the same persona grid in all six conditions: isolated A/B and B/A, constructed A/B and B/A with prior answers retained, direct F-only, and assessed A-then-F. Compute the order difference, QQ statistic, and direct-minus-assessed difference with appropriate intervals. Assess rivals and recommend an action supported by the evidence. Submit the report, executed notebook, records, 6–10 slides, and shared attribution, contribution, and revision logs. Present for ten minutes per team, followed by a five-minute oral defense for each member. The team report and deck and each student’s defense receive separate scores. See M4A1_Project_Part_2.

Assessment

| Component | Type | Part 1 | Full Course |
| --- | --- | --- | --- |
| Discussion 1 | Individual | 10% | 5% |
| Discussion 2 | Individual | 10% | 5% |
| Discussion 3 | Individual | 10% | 5% |
| Project Part 1 proposal | Team | 25% | 12.5% |
| Project Part 2 report and deck | Team | 30% | 15% |
| Project Part 2 oral defense | Individual | 5% | 2.5% |
| Reflection memo | Individual | 10% | 5% |
| Audit practice notebook | Individual | Ungraded | Ungraded |
| Total |  | 100% | 50% |

AI Policy

Each assessment declares a level on the MSBAi AI Assessment Scale: 0 no AI, 1 brainstorming only, 2 drafting with human revision, 3 collaboration with disclosure, and 4 AI as the subject of analysis. Project Part 2 is Level 4, with permitted assistance and disclosure specified in its instructions. The oral defense is Level 0. The reflection is Level 1: write the submitted reflection yourself.

Each team submission includes an AI Attribution Log recording the tools and model versions, prompts, outputs used, member responsible, checks, and revisions. Retain each member’s initial reasoning before consulting AI and verify company facts against public sources. Record contributions and cross-checks in the shared contribution record.

Materials, Tools, and Course Policies

No textbook purchase is required. The repository provides short module notes adapted from Quantum Cognition for Management (Yang, manuscript), lecture transcripts, and a reading guide linking journal articles, author manuscripts, and tutorials. Begin with the suggested introductory readings. Technical and extension readings are optional unless Canvas assigns them.

Use Python notebooks in Colab, Jupyter, or VS Code. The introductory examples and practice audit need NumPy and make no model calls. Project data collection uses the course-approved model access and budget; the audit starter analyzes saved records. Submit through the Canvas assignment link, including a repository link when requested. Keep graded submissions and raw interviews in the approved private location. Exact dates and course-wide grading arrangements are posted in Canvas.

Regular live-session and studio attendance is recommended and is not graded separately. Discussions, Module 3 practice, the oral defense, and the reflection are individual. The proposal, audit report, deck, and project records are team submissions. Modules 1–4 contribute 50% of the full-course grade; Modules 5–8 contribute the other 50%. The table shows both the allocation within this part and its contribution to the full course. Team work contributes 27.5 course percentage points and individual work contributes 22.5.
