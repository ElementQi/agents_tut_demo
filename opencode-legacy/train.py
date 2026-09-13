"""Tutorial-authored legacy NumPy API fixture. See README.md for provenance."""
import json
from pathlib import Path
import numpy as np


def experiment():
    rng = np.random.default_rng(42)
    x = np.linspace(-1, 1, 40).astype(np.float)
    y = 2 * x + 1 + rng.normal(0, 0.15, len(x))
    order = rng.permutation(len(x))
    train, test = order[:30], order[30:]
    w, b = np.polyfit(x[train], y[train], 1)
    mean = y[train].mean()
    return {
        'seed': 42, 'train_n': len(train), 'test_n': len(test),
        'slope': float(w), 'intercept': float(b),
        'mean_test_mse': float(np.mean((mean - y[test]) ** 2)),
        'line_test_mse': float(np.mean((w * x[test] + b - y[test]) ** 2)),
    }


if __name__ == '__main__':
    result = experiment()
    Path('metrics.json').write_text(json.dumps(result, indent=2) + '\n')
    print(f"Train: {result['train_n']} | Test: {result['test_n']}")
    print(f"Fitted line: y = {result['slope']:.4f} x + {result['intercept']:.4f}")
    print(f"Mean predictor test MSE: {result['mean_test_mse']:.4f}")
    print(f"Fitted line test MSE:    {result['line_test_mse']:.4f}")
