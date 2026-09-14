# Prompt-only demos

The ML and report demos start from an **empty folder**. There are no fixtures to
copy: the prompt sequence is the lesson, and the agent builds everything. This
makes the demos trivial to hand on — students copy the prompts and run them at their
own pace. Step 1 navigates a cloned public repository instead.

Prerequisites on the student machine: Python 3.13, Node.js LTS, git, OpenCode,
Codex CLI (for Demo B), and — for the report step — a LaTeX distribution plus
Poppler. Internet access is needed for the first `pip` install, for cloning the
navigation repository, and for installing skills.

The reference numbers below come from an author-written implementation of the same
prompts (`demo/reference-experiment/`); the live agent's files and wording may
differ, but a seed-42 run should land on the same values.

---

## Step 0 — Preflight: let the agent check, and install, your tools

Run this once in each empty project folder before the demo prompts. It turns tool
installation into an agent task instead of a prerequisite.

> Before we start, check this machine and report what you find: the Python version
> and pip, whether conda is available, git, Node.js and npm, a LaTeX compiler
> (pdflatex from MiKTeX, TeX Live, or MacTeX), and Poppler (pdftoppm). If anything
> is missing, install it for me and tell me exactly what you installed.

Expected evidence: a short report of versions and paths; the agent then installs
what is missing (it may ask for permission, or for a package manager such as
Homebrew, Chocolatey, apt, or winget). git is needed to clone the repository we
navigate and to power undo; Python, Node.js, LaTeX, and Poppler are used by the ML,
report, and PDF steps. Nothing else to prepare by hand.

---

## Step 1 — Repository navigation: find the system prompt

Clone a large real repository and treat it as unfamiliar code. This demonstrates
repository navigation on a 15k-commit codebase.

```sh
git clone --depth 1 https://github.com/anomalyco/opencode.git
cd opencode
opencode
```

> In this repository, find where OpenCode defines the system prompt it sends to the
> model. Which file(s) hold the prompt text, how is the prompt chosen for a given
> model, and for a trivial chat message what exactly is sent to the provider --- the
> system prompt, the tool definitions, and my message? Cite the file paths.

Expected evidence: the agent locates `packages/opencode/src/session/prompt/*.txt`
(for example `gpt-astra.txt`, `gpt.txt`, `anthropic.txt`, `default.txt`), finds the
selection logic in `packages/opencode/src/session/system.ts` (GPT-6 selects
`gpt-astra.txt`, Claude selects `anthropic.txt`, otherwise `default.txt`), and notes
that the request is assembled in `packages/opencode/src/session/prompt.ts` and
`session/llm/request.ts`, with your message appended as a user turn.

---

## Demo A — OpenCode: build and supervise a small ML experiment

Create an empty folder and start OpenCode there (`opencode`). Submit the prompts
in order; do not paste them all at once. The library, exact data generation, split,
models, metric, and filenames are pinned so the numbers are reproducible live.

**A1 — plan first (no files yet).**
> We are going to build a small machine-learning experiment from scratch in this
> empty folder. The deliverables will be `experiment.py`, `metrics.json`, and a
> residual plot, using NumPy for the math and Matplotlib for plots only (no
> scikit-learn, no regularization). Propose a short plan first: the files, the data,
> the models, and how we check the result. Do not create anything yet.

Expected evidence: a short plan and file list. This is the read-only planning step.

**A2 — build and run.**
> Go ahead and build it. Create a project-local Python environment, then write
> `experiment.py` using only NumPy and Matplotlib. Generate the data exactly like
> this:
>
> ```python
> rng = np.random.default_rng(42)
> x = np.linspace(-1, 1, 40)
> y = 2*x + 1 + rng.normal(0, 0.3, 40)
> order = rng.permutation(40)
> train, test = order[:20], order[20:]
> ```
>
> Fit two models on the training rows only: (a) a mean baseline that predicts the
> training-target mean, and (b) a linear model by ordinary least squares
> (`np.polyfit(x[train], y[train], 1)`). Report mean squared error for each on the
> training and held-out rows, print them to four decimals, and save `metrics.json`
> with keys `mean` and `linear`, each holding `train_mse` and `test_mse`.

Expected evidence: environment creation, `experiment.py`, a run printing four
numbers, and `metrics.json`. Reference: mean 1.2922 / 1.7700, linear 0.0289 / 0.1035
(train / held-out).

**A3 — introduce the validity question (do not keep this change).**
> Now try a variant: fit the linear model on all 40 points but still report the
> error on the 20 held-out points. Is that still a valid held-out estimate? Explain
> what changed and why it matters.

Expected evidence: the agent states that the fit now sees held-out rows, so the
reported error is no longer a clean held-out estimate (leakage).

**A4 — revert, guard with a test, plot.**
> Revert to fitting on the 20 training points only. Add a test that asserts the
> model is fitted on training rows only and that the reported held-out MSE equals a
> train-only recomputation; add a residual plot saved as `residuals.png`. Rerun
> everything and show the test result.

Expected evidence: a diff back to the train-only fit, a passing test, and
`residuals.png`.

**A5 — a flexible model.**
> Add a third model to `experiment.py`: a degree-9 polynomial fitted with
> `np.polyfit(x[train], y[train], 9)`. Report its training and held-out MSE in the
> same four-decimal format, add it to `metrics.json` under the key `poly9`, and tell
> me which model generalizes best and why.

Expected evidence: a comparison; the polynomial has lower training error but higher
held-out error. Reference: linear training/held-out 0.0289 / 0.1035; polynomial
0.0223 / 0.1429.

**A6 — reuse a skill.**
> Install the matplotlib skill from k-dense-ai/scientific-agent-skills, then use it
> to regenerate the plot at publication quality. Keep the data and every number
> unchanged.

Install command (terminal, in the project folder):

```sh
npx skills add https://github.com/k-dense-ai/scientific-agent-skills --skill matplotlib --agent opencode --copy --yes
```

Expected evidence: the skill's instructions are loaded, the plot is regenerated,
and the before/after figures differ in labels, legend, grid, and type size — not in
the numbers.

---

## Demo B — Codex: write a short research report from the results

Open a second empty folder and start Codex there (`codex`).

**B1 — write the report.**
> Copy ../ml-demo/metrics.json into this folder. Use the academic-paper skill to
> write a short research report in LaTeX on this synthetic regression experiment:
> an abstract, a method section (data, seed, 20/20 split), a results section with a
> table of training and held-out MSE for the mean baseline, the linear model, and
> the degree-9 polynomial, and a short discussion. Use only the numbers in
> metrics.json; do not invent results. Compile a one-page PDF.

Install the report skill (terminal, in the project folder):

```sh
npx skills add https://github.com/imbad0202/academic-research-skills --skill academic-paper --agent codex --copy --yes
```

Expected evidence: the skill's instructions load, `results.tex` and
`output/pdf/results.pdf` appear. Check the report once against `metrics.json`.

**B2 — refine the discussion.**
> Tighten the discussion: state that this is a single split without uncertainty, and
> that the flexible model overfits the training rows. Keep every number unchanged.

**B3 — review with a PDF skill.**
> Install the pdf skill from openai/skills, then: `$pdf` Render and review the
> results PDF. Check for clipped text, overlapping cells, unreadable labels, and
> awkward spacing. Fix layout problems without changing the data or dropping the
> editable LaTeX source.

Expected evidence: the skill instructions load, a renderer produces a page image,
and that image is inspected.

---

## Reset

Everything is throwaway. To run again, delete the cloned `opencode/` and the two
working folders (or use new names) and start over. Nothing in this repository needs
to be copied in.
