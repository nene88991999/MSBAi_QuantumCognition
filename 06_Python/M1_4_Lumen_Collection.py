# %% [markdown]
# # Collecting a Synthetic Panel with Lumen
# 
# **BADM 590 | Team project | Six-condition collection**
# 
# This notebook records model responses for your order-effects audit. Read the [student handout](../../02_Assessments/M1_4_Lumen_Collection_Guide.md) and the [design guide](../../02_Assessments/M1_4_Project_Templates_and_Collection_Guide.md) first.
# 
# The default **dry run is entirely offline** and uses constructed responses. Change the mode explicitly for an authenticated preflight, a two-persona pilot, or the main run. Keep these outputs separate. A live run uses Lumen coins under your own account.
# 
# Open the whole `06_Python` folder in VS Code. Keep this notebook, `lumen_collector.py`, and the configuration together. Select a Python kernel; install `ipykernel` if needed. No external API client library is required.

# %%
from pathlib import Path
import copy
import getpass
import json
import re
import sys

candidates = [Path.cwd(), Path.cwd().parent]
PYTHON_FOLDER = next((p for p in candidates if (p / "lumen_collector.py").is_file()), None)
if PYTHON_FOLDER is None:
    raise FileNotFoundError("Open the course 06_Python folder, with its helper and configuration files.")
if str(PYTHON_FOLDER) not in sys.path:
    sys.path.insert(0, str(PYTHON_FOLDER))
from lumen_collector import LumenHTTP, preflight, collect, plan_summary, check_export, budget_estimate

CONFIG_PATH = PYTHON_FOLDER / "lumen_example_config.json"
CONFIG = json.loads(CONFIG_PATH.read_text())
print(plan_summary(CONFIG))

# %% [markdown]
# ## Choose the Mode and Run Name
# 
# The example contains 24 fictional personas, 144 interviews, and 360 nominal calls. Replace it with your approved questions and persona grid before the main run. Set `example_only` to `false` in your own configuration only after replacing the example.
# 
# The candidate model and settings require teaching-team confirmation. Set `MODEL_AND_SETTINGS_APPROVED` to `True` only when that confirmation has been provided. A preflight can inspect access and prices before that confirmation. It does not send a model-generation request.
# 
# Use a new run name for a genuinely new, documented batch. To resume an interrupted batch, keep the same name and configuration. Never rerun a valid answer to obtain a preferred result.

# %%
MODE = "dry_run"  # dry_run, preflight, pilot, or main
RUN_NAME = "practice_01"
MODEL_AND_SETTINGS_APPROVED = False

if MODE not in {"dry_run", "preflight", "pilot", "main"}:
    raise ValueError("Choose one of the four documented modes.")
if not re.fullmatch(r"[A-Za-z0-9_-]{1,64}", RUN_NAME):
    raise ValueError("Use letters, numbers, underscores, or hyphens for the run name.")
RUN_FOLDER = PYTHON_FOLDER / "collection_runs" / RUN_NAME / MODE
RUN_CONFIG = copy.deepcopy(CONFIG)
if MODE == "pilot":
    RUN_CONFIG["personas"] = RUN_CONFIG["personas"][:2]
    RUN_CONFIG["max_total_attempts"] = 90
print("Mode:", MODE, "| Output:", RUN_FOLDER)
print(plan_summary(RUN_CONFIG))

# %% [markdown]
# ## Connect Only for the Live Steps
# 
# Create your key in your own Lumen profile and enter it below when prompted. Do not paste it into a code cell. The prompt is hidden; the key is held in the running kernel and is never part of the saved configuration. Restart the kernel when finished.
# 
# For a pilot or main run, the collector checks exposed metadata and usage before generation calls. It stops on access, budget, protocol, or response problems that need review. A model fallback is a teaching-team decision.

# %%
client = None
if MODE != "dry_run":
    if MODE in {"pilot", "main"} and not MODEL_AND_SETTINGS_APPROVED:
        raise ValueError("Confirm the teaching team's model and settings before live collection.")
    client = LumenHTTP(getpass.getpass("Your Lumen API key (hidden): "))

if MODE == "preflight":
    snapshot = preflight(client, CONFIG["model"])
    RUN_FOLDER.mkdir(parents=True, exist_ok=True)
    (RUN_FOLDER / "preflight_review.json").write_text(json.dumps(snapshot, indent=2))
    metadata = snapshot["model_metadata"]
    print({k: metadata.get(k) for k in ["id", "parent", "tags", "input_cost_per_million", "output_cost_per_million"]})
    print("Coins currently available:", snapshot["usage"].get("coins_available"))
    print("Review the model notice, current allocation, and settings with the teaching team.")

# %% [markdown]
# ## Collect and Preserve Every Attempt
# 
# An isolated question receives a fresh message history. A constructed interview retains its own earlier questions and actual replies. The assessed condition retains A when asking F. No history crosses persona-condition interviews.
# 
# The collector logs an attempt before dispatch and saves the result before using it. Three attempts per question means the initial call and at most two retries. Retries send the same request. A complete run is not called again when this cell is rerun. An unknown interrupted attempt, changed configuration, or changed model identity requires review.
# 
# The spending check uses recorded usage; delayed accounting or one final call can exceed the chosen stop level. The attempt cap is also enforced. Keep the kernel and computer running during collection.

# %%
summary = None
if MODE != "preflight":
    summary = collect(RUN_CONFIG, RUN_FOLDER, mode=MODE, transport=client,
                      model_and_settings_approved=MODEL_AND_SETTINGS_APPROVED)
    print({k: summary[k] for k in ["mode", "complete", "personas", "interviews", "attempts", "other_attempts", "records_file"]})
    print(check_export(RUN_FOLDER))

# %% [markdown]
# ## Inspect the Histories and Pilot Cost
# 
# Open the saved JSON files for at least one isolated and one constructed interview. In a constructed A-B-F interview, the requests contain 2, 4, and 6 messages. An isolated interview has 2 messages in every request. These counts include the system instruction and current question.
# 
# The pilot estimate scales observed token use to the configured main persona count and adds a 50% planning allowance. It is an estimate, not a guaranteed charge. Review missing usage, failed calls, actual account balance, and differences in prompt length. The observed key cost can include concurrent activity using the same key.

# %%
if summary is not None:
    print(budget_estimate(CONFIG, RUN_FOLDER))
    records = json.loads((RUN_FOLDER / summary["records_file"]).read_text())
    for condition in ["isolated_AB", "constructed_AB", "assessed"]:
        record = next(r for r in records if r["condition"] == condition)
        raw = json.loads((RUN_FOLDER / record["raw_file"]).read_text())
        print(condition, [(m["question"], len(m["request_messages"])) for m in raw["messages"]])

# %% [markdown]
# ## Move the Main Export into the Analysis
# 
# Keep the full run directory together. In `M1_4_Project_Audit_Starter.ipynb`, select `MODE = 'model_data'` and set `DATA_FILE` to this main run's `interviews.json`. Fill in `MODEL_METADATA`, the paths to your frozen proposal/persona grid/exclusion log, and the frozen decision thresholds. Relative `raw_file` paths are resolved from the JSON file's parent folder.
# 
# Only a completed main run creates `interviews.json`. Dry-run and pilot exports use different names and retain labels that the audit validator rejects in main-analysis mode. Preserve partial records if collection stops; resolve missing conditions before analysis.
# 
# Use the approved private team repository for records and graded work. Record who collected, checked, analyzed, and reviewed the data. Commit the frozen plan before collection and identify the final submission by commit ID. Review notebook outputs before sharing and never commit a credential. See `lumen_team_gitignore.example` for local exclusions; it does not remove already tracked files.
# 
# **Team record:** [Collector, reviewer, frozen-plan commit, collection dates, deviations, and the reason for each decision.]

