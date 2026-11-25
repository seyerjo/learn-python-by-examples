# Recursive Functions

Solve self-similar problems using recursion by pairing a clear **base case** with a smaller **recursive step**.

**Source code:** [`sample_16_recursive_functions.py`](./sample_16_recursive_functions.py) · **Level:** Intermediate

## Core Concept

A **recursive function** solves a problem by calling itself on a smaller version of the same input. Every valid recursive function needs two parts:
1. A **base case** that returns directly without recursing.
2. A **recursive step** that moves strictly closer to that base case.

## Guided Walkthrough

1. **Validating inputs and computing `factorial(n)`:** Negative inputs raise `ValueError` immediately; `n == 0` stops the chain by returning `1`, and every larger `n` multiplies `n * factorial(n - 1)`:

```python
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    # Base case stops the recursion.
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

For example, `factorial(3)` evaluates `3 * (2 * (1 * 1))` = `6` as the call stack unwinds.

2. **Recursive input retry:** `get_non_negative_integer()` demonstrates another recursive pattern—catching `ValueError` or negative numbers and calling itself again until the user enters a valid non-negative integer.

## Running the Example

```bash
python3 code/02_intermediate/sample_16_recursive_functions.py
```

### Expected Output

Valid input (`5`):

```text
--- Recursive Factorial Calculator ---
Enter a non-negative integer (e.g., 0, 1, 5): 5

The factorial of 5 is 120.
```

Invalid inputs (`abc`, `-2`) followed by `0`:

```text
--- Recursive Factorial Calculator ---
Enter a non-negative integer (e.g., 0, 1, 5): abc
Invalid input. Please enter a valid integer.
Enter a non-negative integer (e.g., 0, 1, 5): -2
The number must be non-negative. Please try again.
Enter a non-negative integer (e.g., 0, 1, 5): 0

The factorial of 0 is 1.
```

## Key Takeaways

- Every recursive function must guarantee a reachable base case; otherwise it hits Python's recursion limit (`RecursionError`).
- **Production tip:** Using recursion to retry user input (`get_non_negative_integer()`) is illustrative here, whereas a `while True` loop (see [`sample_12_additional_while_iterations.md`](./sample_12_additional_while_iterations.md) and [`sample_22_robust_input_validation.md`](../03_advanced/sample_22_robust_input_validation.md)) is safer in production because each recursive retry consumes another call-stack frame.
- Next: see what happens when recursion goes too deep in [`sample_17_recursion_limit.md`](./sample_17_recursion_limit.md).
