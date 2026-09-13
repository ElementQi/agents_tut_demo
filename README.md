# Coding Agents for Machine Learning — demo materials

Companion files for the DDA5001 tutorial. Clone this repository and follow along
at your own pace; the live session does not wait.

```sh
git clone https://github.com/ElementQi/agents_tut_demo.git
cd agents_tut_demo
```

## Folder 1 — OpenCode: get an old project running

`opencode-legacy/` is an authored legacy fixture, not a broken third-party
repository. Its `train.py` deliberately uses `np.float`, removed in NumPy 1.24, to
reproduce a real compatibility error on NumPy 2.x.

```sh
cd opencode-legacy
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python train.py        # fails with AttributeError on np.float
```

Ask your agent to run the example in a project-local environment and fix the
dependency/API error without changing the intended algorithm. The one-line repair
is `.astype(np.float)` -> `.astype(float)`. Good output: 30 training / 10 test
points, baseline test MSE 1.5476, fitted-line test MSE 0.0133.

`reference-opencode/` holds the failure log, the fixed `train.py`, the successful
log, `metrics.json`, and `SETUP.md`. These are author-executed references, not a
recording of a model session.

## Folder 2 — Codex: turn results into a reviewed PDF

`codex-results/` contains a prepared `results.csv` (four rows, four metric columns)
and a README describing its synthetic provenance. No training is required.

Ask Codex to turn `results.csv` into a publication-style LaTeX table with grouped
metric columns and multirow dataset labels, preserve the source values, and compile
a one-page PDF. Then install a PDF skill and ask it to render and review the page.
`reference-results/` holds the expected `results.tex`, `results.pdf`, and the
author's review notes.

## Provenance and honesty

- The data are synthetic (NumPy, seed 42) and the code is tutorial-authored.
- Reference outputs are reproducible artifacts, not authenticated model
  transcripts.
- Values in the CSV are already rounded to four decimal places; preserve them.
