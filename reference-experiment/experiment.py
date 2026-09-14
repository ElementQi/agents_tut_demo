"""Author-written reference implementation of PROMPTS.md Demo A.

This is not a transcript of an agent session. It reproduces, in one file, the
experiment a seed-42 run of prompts A1-A5 should reach, so the slides, the runbook,
and scripts/verify.py can check real numbers. The live agent may structure its
files differently; keep the prompts, not this file.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

SEED = 42
N = 40
NOISE_SD = 0.3
TRAIN_N = 20


def make_data() -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    rng = np.random.default_rng(SEED)
    x = np.linspace(-1.0, 1.0, N)
    y = 2.0 * x + 1.0 + rng.normal(0.0, NOISE_SD, N)
    order = rng.permutation(N)
    return x, y, order[:TRAIN_N], order[TRAIN_N:]


def mse(pred: np.ndarray, target: np.ndarray) -> float:
    return float(np.mean((pred - target) ** 2))


def main() -> dict:
    x, y, train, test = make_data()
    mean = float(y[train].mean())

    results: dict[str, dict[str, float]] = {}
    results["mean"] = {
        "train_mse": mse(np.full(TRAIN_N, mean), y[train]),
        "test_mse": mse(np.full(len(test), mean), y[test]),
    }
    for name, degree in [("linear", 1), ("poly9", 9)]:
        coeffs = np.polyfit(x[train], y[train], degree)
        results[name] = {
            "train_mse": mse(np.polyval(coeffs, x[train]), y[train]),
            "test_mse": mse(np.polyval(coeffs, x[test]), y[test]),
        }

    payload = {
        "seed": SEED,
        "n": N,
        "noise_sd": NOISE_SD,
        "train_n": int(TRAIN_N),
        "test_n": int(len(test)),
        "models": results,
    }
    out = Path(__file__).resolve().parent
    (out / "metrics.json").write_text(json.dumps(payload, indent=2) + "\n")
    return payload


if __name__ == "__main__":
    data = main()
    models = data["models"]
    print(f"Train: {data['train_n']} | Held-out: {data['test_n']}")
    print(f"Mean baseline   train {models['mean']['train_mse']:.4f}  test {models['mean']['test_mse']:.4f}")
    print(f"Linear          train {models['linear']['train_mse']:.4f}  test {models['linear']['test_mse']:.4f}")
    print(f"Degree-9 poly   train {models['poly9']['train_mse']:.4f}  test {models['poly9']['test_mse']:.4f}")
