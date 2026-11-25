# Hello World and the `__main__` Guard

Write your first runnable Python script using `print()`, quote delimiters, and the standard `if __name__ == "__main__":` entry guard.

**Source code:** [`sample_01_hello_world.py`](./sample_01_hello_world.py) · **Level:** Basic

## Core Concept

Python executes a file from top to bottom. Placing your program's entry logic inside a `main()` function and calling it behind `if __name__ == "__main__":` ensures the script runs automatically when invoked from a terminal, yet stays quiet if another file imports it as a module.

## Guided Walkthrough

1. **Printing text with double or single quotes:** Both `"..."` and `'...'` create valid string literals in Python:

```python
def main():
    """Prints 'Hello, World!' using double and single quotes."""
    print("Hello, World!")
    print('Hello, World!')  # fmt: skip
```

2. **The `__main__` entry guard:** Python automatically sets the special `__name__` variable to `"__main__"` only when a file is executed directly (`python3 sample_01_hello_world.py`). When imported by another script, `__name__` equals the module name instead:

```python
if __name__ == "__main__":
    main()
```

*(Notice `# fmt: skip` on the single-quoted line: it tells `Ruff` to keep the single quotes intact so both quote styles stay visible in this lesson.)*

## Running the Example

```bash
python3 code/01_basic/sample_01_hello_world.py
```

### Expected Output

```text
Hello, World!
Hello, World!
```

## Key Takeaways

- `print()` writes text to standard output followed by a newline by default.
- Double and single quotes behave identically in Python; pick one consistent style (double quotes by default) unless a string contains the other quote character.
- Adopt `def main():` + `if __name__ == "__main__":` from day one to keep every script modular and import-safe.
- Next: explore Python's core data types in [`sample_02_primitives_data_types.md`](./sample_02_primitives_data_types.md).
