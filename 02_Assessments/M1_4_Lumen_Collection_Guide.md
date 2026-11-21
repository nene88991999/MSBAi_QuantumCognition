# Collecting a Synthetic Panel with Lumen

BADM 590 | Team Project Collection | November 21 2026

Your team will examine whether the order of questions changes an AI model's answers. Use the Lumen collection notebook to send the questions, preserve the responses, and prepare the input for the Project Audit Starter. Lumen is the campus model gateway; an API is the interface through which your Python code sends a request and receives a response.

The notebook makes the interview procedure explicit. You can inspect the exact messages and requested settings for every call. The resulting evidence concerns the tested model, questions, and fictional personas. It does not establish how actual customers would respond.

## Set Up Your Workspace

1. Download the course repository or package. Open its `06_Python` folder in VS Code. Keep `lumen_collector.py`, `lumen_example_config.json`, and the `notebooks` folder together.
2. Select your Python interpreter and the Jupyter notebook kernel. If needed, install the VS Code Python and Jupyter extensions and run `python -m pip install ipykernel numpy`. The collector itself uses Python's standard library.
3. Open `notebooks/M1_4_Lumen_Collection.ipynb`. Run it with `MODE = "dry_run"`. This produces constructed practice responses locally and requires no account or key. A completed dry run is a software check.
4. Sign in to [Lumen](https://lumen.ncsa.illinois.edu/) using your university account. Check model access and your coin balance. In Profile, create your own API key. A key is a secret credential that lets code use your account.
5. For the later live steps, enter the key only in the notebook's hidden input prompt. It remains in the running kernel. Restart the kernel when finished. Each teammate uses their own key; nominate one collector for the shared run to avoid duplicate collection.

Keep the key out of code, notebook cells, screenshots, logs, and GitHub. Use fictional personas and approved public background facts. If a credential is exposed, revoke it in Lumen before creating a replacement.

## Follow the Course Schedule

Prepare the proposal in Week 3. Check the collection workflow and freeze the plan in Week 4. Collect in Weeks 5 and 6, then analyze and review the evidence in Week 7. Use Canvas for exact dates. The collection exercise supports the existing team project.

<!-- pagebreak -->

## Preserve the Six Interview Conditions

A and B are framing questions about the same decision. F is the final yes-or-no decision question. Every persona appears in all six conditions. Each persona-condition interview starts fresh. Within an interview, the condition determines whether earlier answers remain in the message history.

| Condition | Questions in Order | Earlier Answers | Calls |
| --- | --- | --- | ---: |
| isolated_AB | A, B, F | Fresh history for each question | 3 |
| isolated_BA | B, A, F | Fresh history for each question | 3 |
| constructed_AB | A then B then F | Retain actual questions and replies | 3 |
| constructed_BA | B then A then F | Retain actual questions and replies | 3 |
| direct | F alone | Fresh history | 1 |
| assessed | A then F | Retain the A question and reply | 2 |

For example, suppose A asks about convenience and B asks about privacy. In `constructed_AB`, the privacy question is sent with the convenience question and its actual answer. In `isolated_AB`, the privacy question receives only the common instruction, persona, background, and privacy question. An answer from another interview is never added.

The collector shuffles the order of whole persona-condition interviews using a saved schedule seed. A seed fixes the shuffle so it can be reconstructed. It does not make model answers deterministic. The question order inside each interview follows the table.

## Replace the Example Design

The supplied configuration contains 24 fictional personas for an illustrative service decision. Replace their descriptions, common facts, and questions with your approved project design. Keep the same persona grid across conditions. Review AI-generated wording and record its source in your attribution log.

The six conditions require 15 nominal calls per persona. With 24 personas, that is 144 interviews and 360 calls before retries. This is a planning example. Choose the sample with the instructor, considering the budget and whether conditional groups will contain enough observations. The number of calls alone does not establish statistical power or human representativeness.

<!-- pagebreak -->

## Freeze the Model and Settings

Use the exact model and settings confirmed by the teaching team. The proposed starting model is NVIDIA Nemotron 3 Super. The configuration uses the candidate Lumen ID `nemotron-3-super-120b-a12b`; confirm that ID through the authenticated preflight before collection. The preflight reads model metadata and usage without asking the model a question.

| Setting | Starting Value | What It Controls |
| --- | --- | --- |
| API base URL | https://lumen.ncsa.illinois.edu/v1 | Campus gateway |
| temperature | 1.0 | Randomness in response sampling |
| top_p | 0.95 | Probability mass retained when sampling |
| max_tokens | 50 | Maximum generated tokens per call |
| enable_thinking | false | Request to disable reasoning output |
| Attempts per question | 3 total | First attempt plus at most two retries |
| Main run attempt cap | 450 in the example | Total calls including failed attempts |

The NVIDIA model card documents the reasoning-off request. Confirm in a pilot that Lumen accepts it and returns complete YES or NO answers. A short output limit is suitable only if the model follows this response format. If reasoning appears, a response is truncated, or a setting is rejected, stop and have the teaching team revise the settings before freezing the main run.

Save the exact instruction, facts, questions, persona grid, model ID, exposed version information, settings, coding, retry rules, schedule seed, sample, and spending stop level. The collector stores these in `frozen_plan.json` and records the model metadata separately. It refuses to resume a run after its configuration or collector code changes.

A gateway alias can continue to exist while its underlying deployment changes. The collector checks exposed model identity and pricing and records returned model identifiers. It cannot establish an immutable weight revision when the service does not expose one. Report the collection dates and available version information.

The proposed fallback is Gemma 4, subject to a separate teaching-team check. There is no automatic fallback. A switch requires a documented decision, a new configuration and output folder, and an agreed analysis. Keep model batches separate; do not fill missing answers with a different model and pool them as one panel. Common settings aid comparison across teams when their tasks and designs are also comparable.

<!-- pagebreak -->

## Pilot the Procedure and Check the Budget

After the teaching team confirms the model and settings, set `MODE = "preflight"` and enter your key. Review the model ID, access notices, prices, and available coins. Read any acknowledgment yourself in the Lumen dashboard. The notebook does not accept notices on your behalf.

Next use `MODE = "pilot"` with two personas. This runs all six conditions for each, requiring 30 nominal calls. Inspect the saved messages for isolated and sequential interviews, valid answers, error rates, token use, and actual key usage. Keep pilot data separate from the main sample. A successful pilot checks operation; it does not select the desired direction of an effect.

Use the model's current input and output prices with the pilot token counts to estimate the main-run cost. Sequential calls include earlier messages and therefore can use more input tokens. Allow room for failed calls and retries. The pilot's observed coin change provides a second check if that key had no other activity during the run. The notebook reports a planning estimate and preserves the usage snapshots.

The example spending stop level is 0.25 coins, a configurable ceiling for review rather than a cost forecast. The collector checks recorded usage before each generation call. Accounting delays or a final request can take spending above the stop level; it is not a provider-enforced spending cap. The fixed attempt cap also limits the run. Check your own account allocation and refill rules before starting.

## Start and Resume the Main Run

Replace the example design, set `example_only` to `false`, and record the instructor's approved settings in the notebook. Use `MODE = "main"` and a new run name. Keep the frozen configuration, collector, and output folder together. The first valid YES or NO is retained. Capitalization and surrounding whitespace are normalized; additional words or punctuation are invalid.

The fixed retry rule repeats the identical request after a format error, transient network error, or eligible rate-limit error. It preserves every attempt and never coaches the model or replaces a valid answer. Report format failures because accepting only valid responses can affect the observed response distribution.

Authentication, access, exhausted quota, changed model identity, truncation, and reasoning output require review. An interrupted call may have reached the provider even if no reply was saved. Preserve its record and seek help before resuming. Never delete logs or start another run solely to obtain a more favorable result.

<!-- pagebreak -->

## Analyze and Document the Run

The completed main run produces `interviews.json`, one record per condition interview, with A, B, and F coded as 0 or 1 when asked. Unasked questions are `null`. Each record points to its file in `raw/`. The `attempts/` folder preserves every generation request and response or recorded error, with timestamps and the accepted attempt identified.

Keep the entire run folder together. In `M1_4_Project_Audit_Starter.ipynb`, select `MODE = "model_data"` and set `DATA_FILE` to the main run's `interviews.json`. Complete `MODEL_METADATA`, including the frozen proposal, persona grid, and exclusion-log paths, and enter the frozen decision thresholds. The raw paths are resolved relative to the JSON file. The analysis checks the six conditions and resamples complete persona blocks. Dry-run and pilot exports carry explicit labels and are rejected as main project data.

Retain the frozen plan, preflight, final usage, summary, raw records, and attempt logs with the executed analysis. If collection stops early, `partial_interviews.json` is a progress record. Resolve missing conditions with the instructor before analysis and report all departures and attrition.

## Use GitHub to Make Team Work Reviewable

Use the approved private team repository for graded work and collection records. The public course repository supplies templates and readings. Record each substantive task as an issue or contribution-log entry with an owner and a reviewer. Commit the frozen plan before collection. Use a pull request or documented review for changes to questions, coding, analysis, and interpretation.

For each review, state what was checked and what changed. Record paired work and discussion contributions even when only one member commits the file. Identify the submitted version by its commit ID, and have every member review the final results before the individual oral defense. Commit counts alone do not measure understanding and do not determine grades.

Before committing, inspect the actual files and notebook outputs for credentials and unintended data. The supplied Git ignore example helps exclude local secrets and collection outputs from a public working copy. It does not remove files that Git already tracks. Preserve required records in the approved private submission location.

## Technical References

[Lumen API reference](https://lumen.ncsa.illinois.edu/help/api), [Profile and API keys](https://lumen.ncsa.illinois.edu/help/profile), and [model details](https://lumen.ncsa.illinois.edu/help/models/detail) explain the service. The [NVIDIA model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16) describes the proposed primary model. [Google's Gemma documentation](https://ai.google.dev/gemma/docs/core) describes the proposed fallback family. Use the authenticated Lumen catalog for current deployment IDs, access, and prices.

Adapted from Vishal's collection handout for the course's six-condition audit. The [Project Templates and Collection Guide](M1_4_Project_Templates_and_Collection_Guide.md) supplies the research design and analysis definitions. The [collection notebook](../06_Python/notebooks/M1_4_Lumen_Collection.ipynb) implements the procedure.
