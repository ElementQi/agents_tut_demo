# Rehearsed working setup

Python 3.13.5; NumPy 2.1.3; Windows PowerShell. From the project folder:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe train.py
```

The original run failed because NumPy removed `np.float`. Replacing
`.astype(np.float)` with `.astype(float)` preserves the intended floating-point
conversion. No data, split, model, or dependency version changed. The successful
run scores 10 held-out observations and writes metrics.json.

This is an author-executed recovery artifact, not an OpenCode conversation.
