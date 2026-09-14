# Reference results page (author-written)

Fallback for Demo B. `results.tex` and `results.pdf` are the author's version of
the page the Codex prompts should produce from the reference experiment's
`metrics.json` (mean baseline, linear, degree-9 polynomial; training and held-out
MSE). They are a reproducible artifact, not a recording of a model session.

Rebuild:

```sh
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=demo/reference-results demo/reference-results/results.tex
```

Values match `demo/reference-experiment/metrics.json`: mean 1.2922 / 1.7700,
linear 0.0289 / 0.1035, polynomial 0.0223 / 0.1429.
