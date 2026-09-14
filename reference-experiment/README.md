# Reference experiment (author-written)

This is an author-written implementation of the Demo A prompts in `PROMPTS.md`,
not a transcript of an agent session. It exists so the slides, the runbook, and
`scripts/verify.py` can check real numbers and so the tutor has a fallback if the
live run stalls.

```sh
python3 experiment.py           # writes metrics.json and prints the table
python3 test_experiment.py -v   # 2 tests; the second catches train/test leakage
```

Seed-42 reference values (20 training / 20 held-out):

| Model | Training MSE | Held-out MSE |
| --- | --- | --- |
| Mean baseline | 1.2922 | 1.7700 |
| Linear | 0.0289 | 0.1035 |
| Degree-9 polynomial | 0.0223 | 0.1429 |

The polynomial has the lowest training error but the highest held-out error: the
overfitting point used in prompt A5.
