# Comments, Docstrings, and Script Structure

Learn how to document Python code cleanly using single-line comments, inline comments, docstrings, and the standard `main()` entry guard.

**Source code:** [`sample_00_comments_types.py`](./sample_00_comments_types.py) · **Level:** Basic

## Core Concept

Readable code explains itself through clear names, while comments and docstrings capture *intent* and *usage*. Python treats `#` lines as ignored comments, whereas triple-quoted string literals (`"""..."""`) placed at the top of a module, class, or function become **docstrings** accessible via `help()`.

## Guided Walkthrough

1. **Single-line and inline comments** start with `#` and are ignored by Python at runtime. Use them sparingly to clarify *why* a value or rule exists rather than narrating obvious syntax:

```python
# Single-line comment explaining a module-level constant.
INITIAL_VALUE = 10  # Inline comment explaining an expression or value.
```

2. **Google-style docstrings** document what a function does, its parameters (`Args:`), and its output (`Returns:`), forming a contract for anyone calling it:

```python
def calculate_square(number):
    """Calculate the square of a number.

    Args:
        number: The numeric value to square.

    Returns:
        The squared value.
    """
    return number * number
```

3. **Entry-point structure and disabled code:** Wrapping execution inside `main()` under `if __name__ == "__main__":` keeps the module safe to import, while `#` can temporarily disable lines during debugging without deleting them.

## Running the Example

```bash
python3 code/01_basic/sample_00_comments_types.py
```

### Expected Output

```text
5 squared = 25
10 + 25 = 35
```

## Key Takeaways

- Prefer self-explanatory variable and function names first; write comments to explain *why*, not *what*.
- Always start modules and public functions with concise `"""..."""` docstrings.
- Avoid leaving large blocks of commented-out code in finished scripts; rely on Git history instead.
- Next: see [`sample_01_hello_world.md`](./sample_01_hello_world.md) for a closer look at `main()` and `__name__ == "__main__"`.
