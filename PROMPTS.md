# Prompt-only demos

Both demonstrations start from an **empty folder**. There are no fixtures to copy:
the prompt sequence is the lesson, and the agent builds everything. This makes the
demos trivial to hand on — students copy the prompts and run them at their own pace.

Prerequisites on the student machine: Python 3.13, Node.js LTS, OpenCode, Codex CLI
(for Demo B), and — for the PDF step — a LaTeX distribution plus Poppler. Internet
access is needed for the first `pip` install and for installing skills.

The reference numbers below come from an author-written implementation of the same
prompts (`demo/reference-experiment/`); the live agent's files and wording may
differ, but a seed-42 run should land on the same values.

---

## Step 0 — Preflight: let the agent check, and install, your tools

Run this once in each empty project folder before the demo prompts. It turns tool
installation into an agent task instead of a prerequisite.

> Before we start, check this machine and report what you find: the Python version,
> whether conda is available, and whether a LaTeX compiler (pdflatex from MiKTeX,
> TeX Live, or MacTeX) and Poppler (pdftoppm) are installed. If anything is missing,
> install it for me and tell me exactly what you installed.

Expected evidence: a short report of versions and paths; the agent then installs
what is missing (it may ask for permission, or for a package manager such as
Homebrew, Chocolatey, or apt). Nothing else to prepare by hand.

---

## Demo A — OpenCode: build and supervise a small ML experiment

Create an empty folder and start OpenCode there (`opencode`). Submit the prompts
in order; do not paste them all at once.

**A1 — plan first (no files yet).**
> We are going to build a small machine-learning experiment from scratch in this
> empty folder. First propose a short plan: the files you will create, the data,
> the model, and how we will check the result. Do not create anything yet.

Expected evidence: a short plan and file list. This is the read-only planning step.

**A2 — build and run.**
> Go ahead and build it. Create a project-local Python environment, then write and
> run a script that generates a 1-D regression dataset and compares two models.
> Data: x is 40 points evenly spaced in [-1, 1]; y = 2x + 1 plus Gaussian noise with
> standard deviation 0.3; use seed 42 for the noise and a second seed-42 permutation
> to split 20 training and 20 held-out points. Fit (a) a mean baseline and (b) a
> linear model on the training points, report mean squared error on the held-out
> points for each, and save the numbers to metrics.json.

Expected evidence: environment creation, the script, a run printing two held-out
MSE values, and `metrics.json`. Reference: baseline 1.7700, linear 0.1035.

**A3 — introduce the validity question (do not keep this change).**
> Now try a variant: fit the linear model on all 40 points but still report the
> error on the 20 held-out points. Is that still a valid held-out estimate? Explain
> what changed and why it matters.

Expected evidence: the agent states that the fit now sees held-out rows, so the
reported error is no longer a clean held-out estimate (leakage).

**A4 — revert, guard with a test, plot.**
> Revert to fitting on the 20 training points only. Add a test that would fail if
> the fit ever used held-out rows, and add a residual plot. Rerun everything and
> show the test result.

Expected evidence: a diff back to the train-only fit, a passing test, and a plotted
figure.

**A5 — a flexible model.**
> Now also fit a degree-9 polynomial on the training points. Compare its held-out
> error with the linear model. Which generalizes better, and why?

Expected evidence: a comparison; the polynomial has lower training error but higher
held-out error. Reference: linear held-out 0.1035 vs polynomial held-out 0.1429.

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

Both demos are throwaway. To run again, delete the two working folders (or use new
names) and start from `opencode` / `codex` in an empty directory. Nothing in this
repository needs to be copied in.
