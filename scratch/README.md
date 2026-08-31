# Scratch

Personal practice space, separate from the graded CS336 assignment code.

- `playground.py` — quick REPL-style exploration (unicode tests, one-off snippets)
- `algorithms/` — ML algorithms implemented from scratch, one file per algorithm, before/alongside the course work

Nothing in here is touched by `uv run pytest` (the grading suite only looks in `tests/`),
so this is a safe place to experiment, break things, and write your own sanity checks.

## Convention

One file per algorithm, numbered in rough order of complexity:

```
scratch/algorithms/
  01_linear_regression.py
  02_logistic_regression.py
  03_knn.py
  ...
```

Each file should stand alone: implement the thing, then a small `if __name__ == "__main__":`
block at the bottom that runs it on a toy example and prints/asserts something you can
sanity check by eye. That mirrors what `tests/adapters.py` does for the real assignment —
good habit to carry over.
