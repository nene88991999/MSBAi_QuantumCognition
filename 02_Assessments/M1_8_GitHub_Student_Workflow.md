# GitHub for the Course Project

Your team needs to preserve what it planned, what it collected, and why its conclusions changed. GitHub keeps these versions together so another person can follow the analysis. Use this guide with the [program's student guide](https://github.com/Business-Analytics-at-Gies/msbai-github-for-students). The assignment briefs and confirmed Canvas instructions govern submission requirements, dates, grading, and permitted AI assistance.

## Start in the Right Repository

A **repository**, often shortened to **repo**, is a project folder with a recorded history of changes. The [public course repository](https://github.com/nene88991999/MSBAi_QuantumCognition) supplies readings, slides, and notebook templates. Use the instructor-approved **private team repository** for your proposal, interview records, analysis, report, and contribution logs. Follow Canvas for individual submissions.

Use the same GitHub account across courses. Accept the invitation to your assigned private repository and confirm that your teammates and instructor have access. If the invitation has expired or no repository has been assigned, contact the teaching team. Do not place assessed work in a public fork of the course repository.

In VS Code, open the Command Palette, choose **Git: Clone**, and paste the assigned private repository's HTTPS address. Open the resulting local folder. Cloning creates a working copy on your computer; it does not change the repository's access settings. Copy the required course templates into the agreed folders. Identify the course-template version in your team README.

## Save Work That Others Can Follow

A **commit** saves a named version in your local history. A **push** sends committed changes to GitHub. A **pull** brings remote changes into your local copy. Saving a file alone does not publish it to your teammates.

1. Before editing, pull from VS Code's Source Control menu and agree on who is editing each shared notebook or document.
2. Complete one coherent task, such as checking the denominator in an answer table. Review the changed files in Source Control, including notebook outputs.
3. Stage only the intended files and commit with a descriptive message, such as “Correct the excluded-record count in the AB table.”
4. Push, open the repository on GitHub, and verify that the intended files and version are visible.

If Git reports a conflict, preserve your work and review the competing changes with the other editor. Resolve the conflict before pushing again. Ask for help when the correct version is unclear. Do not force a push or discard changes to bypass the problem. [VS Code's source-control documentation](https://code.visualstudio.com/docs/sourcecontrol/overview) explains the interface and recovery options.

## Connect the History to the Audit

| When | Record to Preserve | Review to Complete |
| --- | --- | --- |
| Week 3 proposal | Decision, questions, design, rival explanation, and team contributions | Another member checks that the proposed comparison answers the decision question. |
| Week 4 freeze | Exact collection plan, prompts, settings, pilot repairs, thresholds, and a commit ID | Reconstruct the question histories and confirm what each condition measures. |
| Weeks 5–6 collection | Frozen-plan reference, complete call records, and dated deviations | Check coverage, exclusions, retries, and consistency with the plan. |
| Week 7 studio | Analysis, figures, draft claims, peer feedback, and revisions | Reproduce the tables from the preserved data and check the interpretation. |
| Week 8 submission | Final files, executed analysis, contribution and attribution logs, and a commit ID | Every member checks the evidence and prepares to explain it in the individual defense. |

An **issue** records a task or question and its discussion. A **pull request** presents a proposed change for review before it joins the shared version. Use an issue or the existing contribution log to name the task owner and reviewer. Use a pull request or a documented review for consequential changes to questions, coding, analysis, or interpretation.

For example, a review of an exclusion rule should identify the rule, the affected records, the revised denominator, and the reason for the decision. A comment saying “looks good” does not supply that evidence. Record paired work and contributions made through discussion, even when one person operates the keyboard. Commit counts do not determine understanding or grades.

## Keep Working and Submitted Notebooks Distinct

To reduce editing conflicts, clear outputs from the team's shared working copy after preserving results that must be retained. Keep a separate final executed analysis notebook with its tables, figures, and explanatory text visible. Review both copies for unintended data before committing them.

Reproduce the analysis from the saved collection data and frozen settings. Running the analysis again should not collect new model responses. The Lumen collector has separate offline, pilot, and main modes; run live collection only under the agreed collection plan. Follow the [Lumen handout](M1_4_Lumen_Collection_Guide.md) for the API key and call records.

## Submit the Exact Version

Finish the review, commit the final files, and push. Record the full commit ID in the Canvas submission and team README. On GitHub, open a submitted file and press **y**, then copy its address. This **permalink** identifies that file at a particular commit, so later edits do not change the submitted version. It does not grant the recipient access to a private repository. [GitHub's permalink guide](https://docs.github.com/en/repositories/working-with-files/using-files/getting-permanent-links-to-files) shows the procedure.

Follow each brief for the files to upload in Canvas. The project calls for an executed `.ipynb` notebook and supporting records; a repository link alone does not replace those deliverables. An HTML export is optional unless Canvas requests it. Confirm that the instructor can open the private repository. Keep a later correction in a new commit and identify it explicitly if the instructor accepts an amended submission.

## Protect Records and Preserve Attribution

Keep API keys out of every repository, including private ones. Inspect the actual files and outputs before staging. A `.gitignore` entry prevents some new files from being tracked; it does not remove secrets from an existing history. If a key is exposed, revoke it through the provider and inform the teaching team. Keep required interview records in the approved private submission location and explain their location in the README.

Apply each assignment's AI policy. Where independent initial work is required, preserve it before using assistance. Record substantive AI contributions, what you changed, and how you checked the result in the existing AI Attribution Log. An assistant can explain GitHub steps; you remain responsible for understanding the work you submit. Obtain permission before including team work in a public portfolio.

Use the [Project Templates and Collection Guide](M1_4_Project_Templates_and_Collection_Guide.md) for the existing attribution, contribution, and revision records. The [program guide](https://github.com/Business-Analytics-at-Gies/msbai-github-for-students) provides account setup and further help.
