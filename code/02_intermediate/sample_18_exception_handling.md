# Exception Handling: `try-except-else-finally`

Handle runtime errors gracefully with specific `except` clauses, run success-only code in `else`, and guarantee cleanup in `finally`.

**Source code:** [`sample_18_exception_handling.py`](./sample_18_exception_handling.py) · **Level:** Intermediate

## Core Concept

Python's complete exception-handling statement separates four distinct responsibilities:
- **`try`**: code that might raise an error.
- **`except <Error>`**: handlers for specific anticipated failures (`ValueError`, `ZeroDivisionError`).
- **`else`**: code that runs **only if `try` succeeded** without raising an exception (keeping the `try` block small and focused).
- **`finally`**: cleanup code that **always runs**, whether an exception occurred or not.

## Guided Walkthrough

1. **Protecting conversion and division:** `safe_division()` converts two inputs with `float()` and computes `numerator / denominator` inside `try`:

```python
    try:
        numerator_str = input("Enter the numerator: ")
        numerator = float(numerator_str)

        denominator_str = input("Enter the denominator: ")
        denominator = float(denominator_str)

        result = numerator / denominator
    except ValueError:
        print("\nError: Invalid input. Please enter valid numbers.")
    except ZeroDivisionError:
        print("\nError: Cannot divide by zero.")
```

2. **Separating success and guaranteed finish:** Placing the success print inside `else` avoids accidentally catching unrelated errors raised while formatting results, while `finally` always prints the closing banner:

```python
    else:
        print(f"\nSuccess! The result of the division is: {result:.2f}")
    finally:
        print("\n--- Calculation attempt finished. ---")
```

## Running the Example

```bash
python3 code/02_intermediate/sample_18_exception_handling.py
```

### Expected Output

Scenario 1 — Valid numbers (`10`, `4`):

```text
--- Safe Division Calculator ---
This program will calculate numerator / denominator.
Enter the numerator: 10
Enter the denominator: 4

Success! The result of the division is: 2.50

--- Calculation attempt finished. ---
```

Scenario 2 — Non-numeric input (`ten`):

```text
--- Safe Division Calculator ---
This program will calculate numerator / denominator.
Enter the numerator: ten

Error: Invalid input. Please enter valid numbers.

--- Calculation attempt finished. ---
```

Scenario 3 — Division by zero (`10`, `0`):

```text
--- Safe Division Calculator ---
This program will calculate numerator / denominator.
Enter the numerator: 10
Enter the denominator: 0

Error: Cannot divide by zero.

--- Calculation attempt finished. ---
```

## Key Takeaways

- Always catch **specific** exception classes (`ValueError`, `ZeroDivisionError`)—never use a bare `except:`, which hides bugs and intercepts `KeyboardInterrupt`.
- Put normal post-success logic in `else` so your `try` block covers only the risky operation itself.
- Use `finally` (or context managers with `with`) for cleanup that must happen regardless of failure.
- Next: advance to the algorithmic series in [`sample_19_exhaustive_listing_algorithm.md`](../03_advanced/sample_19_exhaustive_listing_algorithm.md) and reusable validation loops in [`sample_22_robust_input_validation.md`](../03_advanced/sample_22_robust_input_validation.md).
