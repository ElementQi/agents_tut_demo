"""Acceptance checks a correct seed-42 run should satisfy.

Run with: python -m unittest -v
The second test fails if the model is ever fitted on held-out rows (leakage).
"""
import json
import sys
import unittest
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import experiment  # noqa: E402


class ExperimentTest(unittest.TestCase):
    def test_split_is_disjoint(self):
        _, _, train, test = experiment.make_data()
        self.assertEqual(len(train), 20)
        self.assertEqual(len(test), 20)
        self.assertTrue(set(train).isdisjoint(set(test)))

    def test_reported_heldout_mse_uses_train_only(self):
        payload = json.loads((HERE / "metrics.json").read_text())
        x, y, train, test = experiment.make_data()
        coeffs = np.polyfit(x[train], y[train], 1)
        expected = float(np.mean((np.polyval(coeffs, x[test]) - y[test]) ** 2))
        self.assertAlmostEqual(expected, payload["models"]["linear"]["test_mse"], places=9)


if __name__ == "__main__":
    unittest.main()
