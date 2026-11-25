# Exhaustive Enumeration (Guess and Check)

Find exact integer square roots by enumerating candidates sequentially, while applying production CLI habits (`main() -> int`, `sys.stderr`, and `Ctrl-C` handling).

**Source code:** [`sample_19_exhaustive_listing_algorithm.py`](./sample_19_exhaustive_listing_algorithm.py) · **Level:** Advanced

## Core Concept

**Exhaustive enumeration** (also called *guess and check*) solves a problem by testing every candidate in a countable search space in order until the answer is found or passed. It is simple and guaranteed to find an exact integer root when one exists, at the cost of linear $O(\sqrt{N})$ growth as the target grows.

## Guided Walkthrough

1. **Guess-and-check loop:** Starting from `guess = 0`, `find_square_root(target)` increments `guess` and `iterations` until `guess**2 >= target`, then checks whether it hit an exact match:

```python
def find_square_root(target: int) -> None:
    guess: int = 0
    iterations: int = 0

    while guess**2 < target:
        guess += 1
        iterations += 1

    print(f"Algorithm finished after {iterations} iterations.")
    if guess**2 == target:
        print(f"The exact square root of {target} is {guess}.")
    else:
        print(f"{target} does not have an exact integer square root.")
```

2. **Validated input and stream separation:** `main() -> int` loops until a non-negative integer is entered, routing invalid-input errors to `sys.stderr`, catching `KeyboardInterrupt` (`Ctrl-C`) to exit with standard Unix code `130`, and returning `0` via `raise SystemExit(main())`.

## Running the Example

```bash
python3 code/03_advanced/sample_19_exhaustive_listing_algorithm.py
```

### Expected Output

Scenario 1 — Perfect square (`81`):

```text
--- Exhaustive Enumeration: Integer Square Root Finder ---
Enter a non-negative integer: 81

Algorithm finished after 9 iterations.
The exact square root of 81 is 9.
```

Scenario 2 — Non-perfect square (`80`):

```text
--- Exhaustive Enumeration: Integer Square Root Finder ---
Enter a non-negative integer: 80

Algorithm finished after 9 iterations.
80 does not have an exact integer square root.
```

## Key Takeaways

- Exhaustive enumeration is straightforward to verify, making it a useful baseline for correctness before optimizing.
- It only finds **exact integer** solutions (`80` fails because $\sqrt{80}$ is irrational) and scales linearly with the root size.
- Notice the `03_advanced` CLI pattern: `main() -> int` + `raise SystemExit(main())`, error messages on `sys.stderr`, and `KeyboardInterrupt` returning `130`.
- Next: approximate non-integer roots within a tolerance in [`sample_20_solution_approximation_algorithm.md`](./sample_20_solution_approximation_algorithm.md).
