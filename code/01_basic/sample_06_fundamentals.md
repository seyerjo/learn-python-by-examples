# Python Fundamentals: Naming, Keywords, and Dynamic Typing

Apply PEP 8 naming conventions, inspect Python's reserved keywords, observe dynamic typing in action, and measure text with `len()`.

**Source code:** [`sample_06_fundamentals.py`](./sample_06_fundamentals.py) · **Level:** Basic

## Core Concept

Consistent naming makes Python code immediately readable across any codebase. Python also enforces a small list of reserved keywords you cannot reuse as identifiers, while allowing variable names to be rebound to objects of different types at runtime (**dynamic typing**).

## Guided Walkthrough

1. **PEP 8 naming conventions:** `show_naming_conventions()` prints Python's standard identifier styles:
   - `snake_case` for variables and functions (`user_name`, `calculate_total()`)
   - `PascalCase` for classes (`MyNewClass`)
   - `UPPER_SNAKE_CASE` for constants (`MAX_CONNECTIONS = 5`)
   - Leading underscore for internal helpers or values (`_internal_value`)

2. **Reserved keywords:** Python's standard-library `keyword` module exposes `keyword.kwlist`, the exact set of words reserved for language syntax (`if`, `for`, `def`, `True`, etc.):

```python
import keyword

print(keyword.kwlist)
```

3. **Dynamic typing:** Reassigning `my_variable` from an `int` to a `float` and then a `str` binds the name to a new object each time:

```python
my_variable = 1
print(f"my_variable is '{my_variable}' of type {type(my_variable)}")
my_variable = 3.75
print(f"my_variable is now '{my_variable}' of type {type(my_variable)}")
```

4. **Combining input and `len()`:** `demonstrate_string_input_and_len()` builds a greeting via an f-string and reports its exact character count.

## Running the Example

```bash
python3 code/01_basic/sample_06_fundamentals.py
```

### Expected Output

With sample input `Alex` (note that `keyword.kwlist` reflects Python 3.11+):

```text
--- Naming Conventions (PEP 8) ---
  - snake_case: Variables and functions (e.g., user_name, calculate_total()).
  - PascalCase: Classes (e.g., class MyNewClass:).
  - UPPER_SNAKE_CASE: Constants (e.g., PI = 3.14, MAX_CONNECTIONS = 5).
  - Descriptive names: Prefer customer_address over addr or c_a.
  - Leading underscore: Indicates internal use (e.g., _internal_value).

--- Python Reserved Keywords ---
These words have special meaning and cannot be used as variable names:
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

--- Dynamic Typing Demonstration ---
my_variable is '1' of type <class 'int'>
my_variable is now '3.75' of type <class 'float'>
my_variable is now 'hello' of type <class 'str'>

--- Input, F-Strings, and Length ---
What's your name?: Alex
Hi Alex, my best regards.
Length of this greeting: 25 characters.
```

## Key Takeaways

- Follow PEP 8 naming consistently so readers recognize constants, variables, functions, and classes at a glance.
- Never name variables after reserved keywords (`class`, `from`, `import`) or built-in functions (`list`, `str`, `len`).
- Dynamic typing gives flexibility, while **type hinting** (covered in [`sample_23_type_hinting.md`](../03_advanced/sample_23_type_hinting.md)) helps large codebases catch type mismatches before runtime.
- Next: make decisions in code with [`sample_07_flow_control.md`](./sample_07_flow_control.md).
