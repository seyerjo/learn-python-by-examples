# Conditional Flow Control (`if`, `elif`, `else`)

Branch program execution based on numeric comparisons, compound boolean ranges, and nested conditionals.

**Source code:** [`sample_07_flow_control.py`](./sample_07_flow_control.py) · **Level:** Basic

## Core Concept

Conditional statements let a program choose different execution paths depending on runtime data. Python evaluates each branch in order and runs only the **first** matching block, using 4-space indentation to define which statements belong to each branch.

## Guided Walkthrough

1. **Mutually exclusive branching (`if-elif-else`):** `demonstrate_if_elif_else()` compares two integers and guarantees exactly one of three messages runs.

2. **Range checks with `and` and boundary validation:** `demonstrate_logical_flow()` checks `age < 0` first so negative numbers do not silently fall into the `"senior citizen"` `else` branch:

```python
if age < 0:
    print("Age cannot be negative.")
elif age >= 0 and age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
```

3. **Input normalization and nested `if`:** Calling `.strip().lower()` cleans accidental spaces and casing before checking sub-conditions inside an outer branch:

```python
user_role = input("Enter user role (admin/user): ").strip().lower()
is_active_str = input("Is the user active? (yes/no): ").strip().lower()

if user_role == "admin":
    print("Admin access granted.")
    if is_active_str == "yes":
        print("User is active and can make changes.")
```

## Running the Example

```bash
python3 code/01_basic/sample_07_flow_control.py
```

### Expected Output

With sample inputs `25`, `50`, `35`, `admin`, and `yes`:

```text
--- Example 1: Basic if-elif-else ---
Enter the first integer: 25
Enter the second integer: 50
Result: The second number (50) is greater than the first (25).

--- Example 2: Flow Control with Logical 'and' ---
Enter your age: 35
You are an adult.

--- Example 3: Nested if Statements ---
Enter user role (admin/user): admin
Is the user active? (yes/no): yes
Admin access granted.
User is active and can make changes.
```

## Key Takeaways

- Always handle boundary/edge cases (like `age < 0`) explicitly instead of letting unexpected values fall through into a catch-all `else`.
- Normalize string comparisons from `input()` with `.strip().lower()`.
- Keep nesting shallow where possible; deeply nested `if` blocks become harder to read.
- **Note:** Entering non-numeric text for integers raises `ValueError` (handled safely in [`sample_18_exception_handling.md`](../02_intermediate/sample_18_exception_handling.md)).
- Next: eliminate repeated logic with [`sample_08_more_fundamentals.md`](./sample_08_more_fundamentals.md).
