# Reusable, Type-Safe Input Validation

Generalize defensive `while True` / `try-except` input loops into one reusable function supporting dynamic numeric converters and optional bounds.

**Source code:** [`sample_22_robust_input_validation.py`](./sample_22_robust_input_validation.py) · **Level:** Advanced

## Core Concept

Writing separate validation loops for every integer, float, or range prompt duplicates code across an application. Because functions and types (`int`, `float`) are first-class objects in Python, a single parameterized helper can handle type conversion, optional lower/upper bounds, and `sys.stderr` error reporting cleanly.

## Guided Walkthrough

1. **Flexible signature with PEP 585/604 types:** `get_valid_number` accepts a converter (`num_type: type[int | float] = int`) and optional `min_val` / `max_val` bounds defaulting to `None`:

```python
def get_valid_number(
    prompt: str,
    num_type: type[int | float] = int,
    min_val: int | float | None = None,
    max_val: int | float | None = None,
) -> int | float:
```

2. **Safe bounds checking and `sys.stderr` diagnostics:** Inside `while True`, `min_val is not None` (rather than truthiness `if min_val:`) ensures valid zero bounds (`0` or `0.0`) are enforced, and validation errors write to `sys.stderr`:

```python
            number = num_type(input(prompt))
            # Explicit `is not None` prevents 0 or 0.0 bounds from being skipped.
            if min_val is not None and number < min_val:
                print(
                    f"Error: The value must be at least {min_val}.",
                    file=sys.stderr,
                )
                continue
```

3. **Reusability in `main() -> int`:** `main()` calls `get_valid_number` three times (unbounded `int`, bounded `float` `[0.0, 1.0]`, bounded `int` `[1, 5]`) and catches `KeyboardInterrupt` to exit with code `130`.

## Running the Example

```bash
python3 code/03_advanced/sample_22_robust_input_validation.py
```

### Expected Output

With sample inputs `thirty`, `30`, `1.5`, `0.75`, `6`, and `5` (combining `stdout` and `stderr` in terminal view):

```text
--- Demonstrating a general-purpose number validation function ---

Please enter your age (any integer): thirty
Invalid input. Please enter a valid int.
Please enter your age (any integer): 30
Valid age entered: 30

Enter a probability (a decimal between 0.0 and 1.0): 1.5
Error: The value must be no more than 1.0.
Enter a probability (a decimal between 0.0 and 1.0): 0.75
Valid probability entered: 0.75

Please rate our service (an integer from 1 to 5): 6
Error: The value must be no more than 5.
Please rate our service (an integer from 1 to 5): 5
Valid rating entered: 5
```

## Key Takeaways

- Always compare optional numeric bounds with `is not None` so `0` and `0.0` are never skipped as falsy.
- Passing `int` or `float` as `num_type` leverages Python's first-class callables to eliminate duplicated loops.
- Sending validation errors to `sys.stderr` keeps standard output clean if results are piped or logged separately.
- Next: master Python type annotations and static checking in [`sample_23_type_hinting.md`](./sample_23_type_hinting.md).
