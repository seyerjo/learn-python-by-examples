# Continuous Binary Search

Approximate square roots in logarithmic $O(\log N)$ time by halving a monotonic search interval on every iteration.

**Source code:** [`sample_21_binary_search_algorithm.py`](./sample_21_binary_search_algorithm.py) · **Level:** Advanced

## Core Concept

**Binary search** applies a divide-and-conquer strategy whenever the search space is ordered and monotonic. Instead of stepping linearly from `0`, it evaluates the **midpoint** of `[low, high]` and discards half of the remaining range on each step—cutting thousands or millions of iterations down to a few dozen.

## Guided Walkthrough

1. **Search-space bounds:** Setting `high = max(1.0, float(target))` guarantees the root stays inside `[low, high]` even when `target` is `0` (or between `0` and `1`, where $\sqrt{x} \ge x$):

```python
    epsilon: float = 0.01
    low: float = 0.0
    # Upper bound is at least 1.0 so targets in [0, 1) stay inside the search space.
    high: float = max(1.0, float(target))
    guess: float = (high + low) / 2
    iterations: int = 0
```

2. **Halving the interval:** Each pass checks whether `guess**2 < target` to move `low` up or `high` down, then computes the new midpoint:

```python
    while abs(guess**2 - target) >= epsilon:
        if guess**2 < target:
            low = guess
        else:
            high = guess
        guess = (high + low) / 2
        iterations += 1
```

3. **CLI lifecycle:** `main() -> int` validates non-negative integer input (`sys.stderr` for errors, `130` on `KeyboardInterrupt`) and exits cleanly via `raise SystemExit(main())`.

## Running the Example

```bash
python3 code/03_advanced/sample_21_binary_search_algorithm.py
```

### Expected Output

With sample input `123456`:

```text
--- Binary Search: Square Root Finder ---
Enter a non-negative integer: 123456

Algorithm finished after 30 iterations.
The approximate square root of 123456 is 351.3631
```

## Key Takeaways

- **Algorithmic comparison (`19` → `20` → `21`):** Linear approximation (`sample_20`) needed `50,981` steps just for `26`, whereas binary search approximates `123,456` in only **`30` iterations**.
- Binary search requires a **monotonic** ordered domain; it will not work directly on unsorted or non-monotonic functions.
- Setting `high = max(1.0, float(target))` avoids a classic boundary bug for small targets in `[0, 1)`.
- Next: generalize reusable validation helpers in [`sample_22_robust_input_validation.md`](./sample_22_robust_input_validation.md).
