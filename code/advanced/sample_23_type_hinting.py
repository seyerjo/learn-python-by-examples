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
