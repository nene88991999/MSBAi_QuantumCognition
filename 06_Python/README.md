# Python Examples and Audit Notebooks

All examples run on an ordinary computer. No quantum hardware is needed. Every supplied default is a simulation or an imposed mathematical example; none makes a paid model call.

## Run the Notebooks

Open a notebook in Colab, Jupyter, or VS Code, then run all cells from the top. The analysis notebooks contain their helper functions. The Lumen collection notebook uses the helper and configuration files in this folder; download the whole folder before running it. Install NumPy if your environment does not already include it. The examples were checked with Python 3.12 and NumPy 2.3.5; the dependency file allows NumPy 1.26 through 2.x.

| Order | Notebook | Purpose |
| --- | --- | --- |
| 1 | [M1 Probability Onramp](notebooks/M1_Probability_Onramp.ipynb) | States, question directions, and squared projections. |
| 2 | [M2 Order and QQ](notebooks/M2_Order_and_QQ.ipynb) | Answer-pair tables, order effects, and a classical example with q = 0. |
| 3 | [M3 Interference and Brackets](notebooks/M3_Interference_and_Brackets.ipynb) | Direct and assessed rates; the fixed-conditional-rate bracket. |
| 4 | [M3A2 Audit Practice](notebooks/M3A2_Audit_Practice.ipynb) | Check an estimator against two known data-generating processes and examine sample-size sensitivity. |
| 5 | [Project Audit Starter](notebooks/M1_4_Project_Audit_Starter.ipynb) | Analyze six-condition records and produce intervals and diagnostic notes. |

The first three are short learning examples adapted from the book. The last two support the practice assignment and project. Complete the student response cells in your own copy.

## Collect with Lumen

Open [M1_4_Lumen_Collection.ipynb](notebooks/M1_4_Lumen_Collection.ipynb) in VS Code. The [helper](lumen_collector.py) implements the six conditions, an explicit attempt log, fixed retry limits, and resumable collection. The [example configuration](lumen_example_config.json) contains fictional practice inputs. Replace it with your approved design before a main run. The [Git ignore example](lumen_team_gitignore.example) helps keep local secrets and output folders out of a public working copy.

The candidate model is Nemotron 3 Super, subject to an authenticated Lumen check and teaching-team confirmation. Never switch models silently. Main exports feed the Project Audit Starter; dry-run and pilot exports are rejected as main data. A two-persona pilot checks the service, context rules, output format, and cost before collection.

## Run the Python Files

From `06_Python`:

```bash
python -m pip install -r requirements.txt
python qc_models.py
python M1_Probability_Onramp.py
python M2_Order_and_QQ.py
python M3_Interference_and_Brackets.py
python M3A2_Audit_Practice.py
python M1_4_Project_Audit_Starter.py
python -m unittest discover -s tests -v
```

The `.py` versions preserve the notebook's code and explanatory text as comments. [qc_models.py](qc_models.py) provides reusable probability functions; [audit.py](audit.py) provides the reusable collection validation, estimation, and bootstrap functions. Code cells marked `# %%` can also run individually in VS Code. The audit scripts create `audit_outputs`; keep those outputs with your own analysis.

## Project Data

Read the [collection guide](../02_Assessments/M1_4_Project_Templates_and_Collection_Guide.md) before collecting responses. The starter's default `MODE = 'demonstration'` checks a known process. For a project, follow the notebook instructions to select `model_data`, record the approved model and settings, freeze thresholds, and supply saved interview records. Use the [Lumen collection notebook](notebooks/M1_4_Lumen_Collection.ipynb) and [student handout](../02_Assessments/M1_4_Lumen_Collection_Guide.md) for collection. Its default is offline; explicit pilot/main modes use Lumen after model and settings confirmation.

Each persona needs one complete record in each of six conditions. The fields are `interview_id`, `persona_id`, `condition`, `A`, `B`, `F`, and `raw_file`. Answers use integers 0 or 1; unasked questions use JSON `null`. Raw records retain the model version, settings, timestamp, messages, and retry history. The starter rejects missing conditions and malformed coding rather than filling them with zeros.

Use the [GitHub project workflow](../02_Assessments/M1_8_GitHub_Student_Workflow.md) to review changes and preserve the submitted version. Clear outputs from shared working copies only after preserving required results. Keep the final executed analysis notebook with its outputs, and reproduce it from saved data without repeating live collection.

Store interviews and graded work in the approved private submission location. No access key belongs in a notebook or repository. An excluded filename in `.gitignore` is only a convenience; review files before committing them.

## Interpret the Results

The project bootstrap resamples complete persona blocks, preserving all six conditions. Main statistics have 95% pointwise percentile intervals. The two direct-minus-conditional contrasts use 97.5% intervals to target approximately 95% simultaneous coverage through a Bonferroni adjustment. This does not make the entire audit one joint 95% test.

If a resample has an empty assessed subgroup, the affected interval is unavailable. Sparse or constant outcomes also require care. A large number of bootstrap draws cannot repair an uninformative sample. The notebook reports these conditions explicitly.

The results describe the tested response procedure and persona grid. A small q is one model restriction, and an out-of-bracket direct rate tests a fixed-rate benchmark. Human representativeness requires separate evidence.

## Individual Practice and Team Project

Complete `M3A2_Audit_Practice.ipynb` individually. Use `M1_4_Project_Audit_Starter.ipynb` for the shared team audit and submit one executed project notebook with the team report. Record who produced and checked each analysis step. Every member should be able to explain the records, calculations, and uncertainty during their individual oral defense.

## Agency Practice for Weeks 5 and 6

[Guide, code, and constructed data](M5_6_Agency_Practice.md) · [Notebook](notebooks/M5_6_Agency_Practice.ipynb). The exercise is ungraded and does not change the frozen project collection.
