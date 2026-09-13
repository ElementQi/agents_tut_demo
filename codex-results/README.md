# Experiment results to a research table

This task is independent of the OpenCode demo. `results.csv` contains prepared
measurements from two **synthetic tutorial regression datasets**, not research
benchmarks. `scripts/generate_results.py` in the tutorial repository reproduces
the values using NumPy 2.1.3, seed 42, 30 training and 10 held-out points per dataset.
The datasets have Gaussian noise standard deviations 0.15 and 0.50.

Each row is a dataset/model pair. `train_mse` and `test_mse` are mean squared
errors; `train_mae` and `test_mae` are mean absolute errors. Lower is better.
`Mean` predicts the training-target mean; `Linear` fits slope and intercept by
least squares on training rows only. These are single-split results, not averages
or uncertainty estimates. CSV values are already rounded to four decimal places;
preserve their exact displayed values.

Ask Codex to create editable `results.tex` and a one-page `output/pdf/results.pdf`
with grouped Train/Test columns (MSE and MAE beneath each), multirow dataset labels,
and a concise caption. The compiler and renderer are prepared before class.
Do not rerun training for this task.

Follow up: "Rename the grouped headers to Training and Held-out test, and make
the caption explain that these are synthetic, single-split results. Keep every
number unchanged."

Then install the published OpenAI `pdf` skill and ask it to render and review the
existing PDF while retaining the LaTeX source. See STUDENT_GUIDE.md at the tutorial
root for commands. No skill is preinstalled in this distributed input folder.
