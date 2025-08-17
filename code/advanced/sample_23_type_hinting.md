# Advanced: Type Hinting (PEP 484)

**Type Hinting** is a feature introduced in PEP 484 that allows developers to formally indicate the expected data types for variables, function parameters, and return values. It is a cornerstone of modern, robust Python development.

**Key Idea**: While Python remains a dynamically-typed language (meaning the interpreter does not enforce these hints at runtime), type hints provide immense value for code quality and maintainability.

This example demonstrates:

1.  Basic type hints for variables and functions.
2.  How to use hints for complex/container types like `List` and `Dict`.
3.  How static type checkers use these hints to find bugs.

## Code

The following code shows several examples of type hinting in action.

```python
# MAIN CODE

"""
Demonstrates TYPE HINTING in Python (PEP 484).

Type Hinting allows developers to indicate the expected data types for
variables, function parameters, and return values.

IMPORTANT: Python remains a dynamically-typed language. These "hints" are
not enforced by the Python interpreter at runtime. They are primarily for:
1.  Improving code readability and self-documentation.
2.  Allowing static analysis tools (like `mypy`) to catch type-related
    errors before the code is even run.
3.  Enhancing IDE support for autocompletion and error checking.
"""

# For complex types like List, Dict, etc., we must import them from the `typing` module.
from typing import List, Dict


# --- Example 1: Basic Type Hinting ---

PI: float = 3.14159  # Variable with a type hint.


def add_numbers(a: int, b: int) -> int:
    """
    Adds two integers and returns their sum.
    This function is hinted to take two `int` and return an `int`.
    """
    return a + b


# --- Example 2: Hinting with Complex Types ---

def count_words(phrases: List[str]) -> Dict[str, int]:
    """
    Takes a list of strings and returns a dictionary with word counts.
    This demonstrates hinting with imported types like `List` and `Dict`.
    """
    word_count: Dict[str, int] = {}
    for phrase in phrases:
        for word in phrase.split():
            word_count[word] = word_count.get(word, 0) + 1
    return word_count


def main() -> None:
    """Main function to demonstrate type hinting."""
    print("--- Demonstrating Basic Type Hinting ---")
    result: int = add_numbers(10, 5)
    print(f"The result of add_numbers(10, 5) is: {result}")
    print(f"The value of PI (hinted as float) is: {PI}\n")

    print("--- Demonstrating Complex Type Hinting ---")
    sentences = ["hello world", "hello python"]
    counts = count_words(sentences)
    print(f"Counting words in: {sentences}")
    print(f"Resulting dictionary: {counts}\n")

    # --- Example of a Type Error ---
    # The following line, if uncommented, would be flagged as an error by a
    # static type checker like `mypy` because we are passing strings to a
    # function that expects integers.
    #
    # mypy would report:
    # error: Argument 1 to "add_numbers" has incompatible type "str"; expected "int"
    # error: Argument 2 to "add_numbers" has incompatible type "str"; expected "int"
    #
    # add_numbers("hello", "world")


if __name__ == "__main__":
    main()
```

## Explanation

1.  **Basic Hints**:

    -   `PI: float = 3.14159`: We declare that `PI` is intended to be a `float`.
    -   `def add_numbers(a: int, b: int) -> int:`: This signature clearly states the function expects two `int` arguments and will return an `int`.

2.  **Complex Hints**:

    -   `from typing import List, Dict`: To hint container types, we import specialized types from the `typing` module.
    -   `phrases: List[str]`: This indicates the `phrases` parameter should be a `List` where each element is a `str`.
    -   `-> Dict[str, int]`: This indicates the function will return a `Dict` where keys are `str` and values are `int`.

3.  **Static Analysis in Action**:
    -   The commented-out line `add_numbers("hello", "world")` shows a typical programming error.
    -   While Python would run this line and concatenate the strings, a **static type checker** like `mypy` would analyze the code _before execution_ and report an error, because the function was called with types that do not match its hints. This helps catch bugs early.

## Expected Output

```
--- Demonstrating Basic Type Hinting ---
The result of add_numbers(10, 5) is: 15
The value of PI (hinted as float) is: 3.14159

--- Demonstrating Complex Type Hinting ---
Counting words in: ['hello world', 'hello python']
Resulting dictionary: {'hello': 2, 'world': 1, 'python': 1}
```

## Points to Consider

-   **Static Analysis Tools**: To get the full benefit of type hints, integrate a static type checker like `mypy` into your development workflow. You can install it via `pip install mypy` and run it from the command line: `mypy your_script.py`.
-   **Clarity and Maintainability**: Type hints are one of the most effective ways to make your code self-documenting and easier for others (and your future self) to understand and maintain.
-   **Modern Python**: Using type hints is a standard practice in modern Python, especially in larger projects, libraries, and collaborative environments.
