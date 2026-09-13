# A small linear-regression project

This is a **tutorial-authored legacy API fixture**, not a broken third-party
repository. It deliberately uses the old `np.float` alias, deprecated in NumPy
1.20 and removed in 1.24, to reproduce a real compatibility error on NumPy 2.1.3.

The example fits a straight line to 30 synthetic observations, then compares its
mean squared error (MSE) on 10 held-out observations with a constant mean predictor.
The data use seed 42. No download or GPU is needed.

Files: `train.py` is the smallest example; `requirements.txt` records the package
version used for the rehearsal. Run `python train.py` in a project-local environment.
The starting version fails before training. Ask the agent to inspect the project,
create `.venv`, diagnose the failure, and record a working setup in `SETUP.md`.
Keep the data, split, and least-squares algorithm unchanged.

Prepare a fresh copy with
`python scripts/prepare_demo.py opencode-session --demo opencode` from the tutorial root.
