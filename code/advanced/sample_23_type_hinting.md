# Type Hinting in Python (PEP 484)

This example explains what Type Hinting is and demonstrates its use in functions and variables.

## Code

```python
""" TYPE HINTING (PEP 484)

    Type Hinting allows developers to indicate the expected data types for
    variables, function parameters, and return values.

    IMPORTANT: Python remains a dynamically-typed language. These "hints" are
    not enforced by the Python interpreter at runtime.

"""

# Variable with a type hint
PI: float = 3.14159


def add_numbers(a: int, b: int) -> int:
    """Adds two integers and returns their sum."""
    return a + b


def main() -> None:
    """Main function to demonstrate type hinting."""
    result = add_numbers(10, 5)
    print(f"The result is: {result}")


if __name__ == "__main__":
    main()
```

## Explanation

1.  **What is Type Hinting?**: It's a formal way to indicate the type of a value in your Python code. For a variable, you use `variable_name: type`. For a function, you specify the type of each parameter (`param: type`) and the type of the return value (`-> type`).
2.  **Why is it useful?**:
    - **Clarity and Readability**: It makes the code self-documenting. Anyone reading the `add_numbers` function immediately knows it's designed to work with integers.
    - **Error Detection**: Static type checkers like `mypy` can analyze your code _before_ you run it and find potential bugs, such as passing a string to a function that expects an integer.
    - **IDE Support**: Code editors like VS Code use these hints to provide better autocompletion, refactoring, and error highlighting.
3.  **Runtime Behavior**: It is crucial to understand that Python does **not** check these types when the code runs. If you call `add_numbers("hello", "world")`, it will still work because the `+` operator works for strings. The benefit of type hints is realized through external tools, not the interpreter itself.

## Expected Output

```
The result is: 15
```

## Points to Consider

- **Static Analysis**: To get the full benefit of type hints, you should run a static type checker like `mypy` on your code. You can install it via pip (`pip install mypy`) and run it with `mypy your_script.py`.
- **Complex Types**: For more complex types like lists or dictionaries, you need to import them from the `typing` module (e.g., `from typing import List, Dict, Optional`).
- **Modern Practice**: Type hinting is considered a best practice in modern Python development, especially for libraries and large applications where code clarity and correctness are critical.
