# Functions: Parameters, Defaults, and `return`

Build reusable functions with positional parameters, default values, explicit `return` statements, and keyword arguments.

**Source code:** [`sample_15_functions.py`](./sample_15_functions.py) · **Level:** Intermediate

## Core Concept

Functions package a single, well-defined operation under a clear name so callers can reuse it with different inputs. Defining explicit parameters and returning values (instead of relying on globals or printing inside calculation helpers) keeps code modular and easy to test.

## Guided Walkthrough

1. **Parameters and `return`:** `add_numbers(a, b)` receives two inputs and sends the sum back to the caller. (Functions without an explicit `return` implicitly return `None`.)

```python
def add_numbers(a, b):
    return a + b
```

2. **Default parameter values:** `format_full_name` sets `reverse=False`, making the third argument optional for callers:

```python
def format_full_name(first_name, last_name, reverse=False):
    if reverse:
        return f"{last_name}, {first_name}"
    return f"{first_name} {last_name}"
```

3. **Positional vs. keyword arguments:** Positional calls match arguments by order, whereas keyword calls specify parameter names explicitly—making boolean flags and reordered arguments self-documenting:

```python
regular_name = format_full_name("John", "Doe")
reversed_name = format_full_name("John", "Doe", reverse=True)
kw_name = format_full_name(last_name="Doe", first_name="John")
```

## Running the Example

```bash
python3 code/02_intermediate/sample_15_functions.py
```

### Expected Output

```text
--- Demonstrating `add_numbers` function ---
The result of add_numbers(5, 3) is: 8

--- Demonstrating `format_full_name` function ---
Default order: John Doe
Reversed order: Doe, John
Called with keyword arguments: John Doe
```

## Key Takeaways

- Keep functions focused on a single responsibility and return results instead of hardcoding side effects when possible.
- Use keyword arguments for boolean flags (`reverse=True`) so call sites read clearly without checking the definition.
- **Warning:** Never use mutable objects (like `[]` or `{}`) as default parameter values; default to `None` instead and initialize inside the function.
- Next: learn how functions can call themselves in [`sample_16_recursive_functions.md`](./sample_16_recursive_functions.md) (and see [`sample_23_type_hinting.md`](../03_advanced/sample_23_type_hinting.md) for adding type annotations).
