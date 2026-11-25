# Solution Approximation (`epsilon` Tolerance)

Approximate non-integer square roots within a chosen margin of error (`epsilon`) by advancing in small fixed floating-point steps.

**Source code:** [`sample_20_solution_approximation_algorithm.py`](./sample_20_solution_approximation_algorithm.py) · **Level:** Advanced

## Core Concept

Many real problems do not have exact integer solutions. **Solution approximation** accepts any candidate $x$ whose squared error $|x^2 - \text{target}|$ falls strictly below a tolerance $\varepsilon$ (`epsilon`). Advancing by a fine `step = epsilon**2` prevents stepping past the valid tolerance window, exposing the classic precision-versus-speed trade-off.

## Guided Walkthrough

1. **Tolerance and step size:** `find_root_by_approximation(target)` sets `epsilon = 0.01` and `step = epsilon**2` (`0.0001`), incrementing `guess` while both `abs(guess**2 - target) >= epsilon` and `guess <= target` hold:

```python
    epsilon: float = 0.01
    # Keep step smaller than epsilon so the search does not overshoot the root.
    step: float = epsilon**2
    guess: float = 0.0
    iterations: int = 0

    while abs(guess**2 - target) >= epsilon and guess <= target:
        guess += step
        iterations += 1
```

2. **Convergence check and CLI contract:** After the loop exits, `abs(guess**2 - target) < epsilon` confirms whether an approximation was found. `main() -> int` validates non-negative integer input on `sys.stderr` and returns `130` on `KeyboardInterrupt`.

## Running the Example

```bash
python3 code/03_advanced/sample_20_solution_approximation_algorithm.py
```

### Expected Output

With sample input `26`:

```text
--- Solution Approximation: Square Root Finder ---
Enter a non-negative integer: 26

Algorithm finished after 50981 iterations.
The approximate square root of 26 is 5.0981
```

## Key Takeaways

- Approximation solves non-integer roots that exhaustive integer enumeration (`sample_19`) cannot represent.
- **Precision vs. cost:** Tightening `epsilon` by $10\times$ with `step = epsilon**2` multiplies iterations by $100\times$—for `26` at `epsilon = 0.01`, the linear scan already takes `50,981` steps.
- Avoid comparing floats with `==`; always compare against a tolerance (`abs(a - b) < epsilon`).
- Next: shrink those `50,981` iterations to logarithmic steps using [`sample_21_binary_search_algorithm.md`](./sample_21_binary_search_algorithm.md).
