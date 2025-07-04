# Robust Input Validation in Python

This example demonstrates how to create a robust input validation loop to prevent crashes from invalid user input.

## Code

```python
""" ROBUST INPUT VALIDATION

    When writing interactive programs, it's crucial to anticipate that users
    might not always provide the input you expect. If your program expects an
    integer but receives text, it will crash with a `ValueError`.

    Robust input validation is the practice of creating a loop that repeatedly
    asks the user for input until they provide data in the correct format. This
    prevents crashes and provides a much better user experience.

    The most common pattern for this in Python is to use a `while True` loop
    combined with a `try-except` block.

"""

# ############################################################################ #
# NOTE: This example uses Type Hinting, a concept explained in detail in      #
# sample_23_type_hinting.py. It is recommended to review that example to fully #
# understand the type annotations used here (e.g., `-> int`, `-> None`).       #
# ############################################################################ #


def get_valid_integer(prompt: str) -> int:
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main() -> None:
    age = get_valid_integer("Please enter your age: ")
    print(f"\nThank you. You have entered {age} as your age.")


if __name__ == "__main__":
    main()
```

## Explanation

1.  **The Problem**: A simple `int(input())` call will raise a `ValueError` if the user types something that cannot be converted to an integer (like "abc" or "1.5"), causing the program to crash.
2.  **The Solution**: We create a function `get_valid_integer` that wraps the input prompt in a `while True` loop.
3.  **`try-except` Block**:
    - The `try` block attempts the "risky" operation: converting the user's input to an `int`.
    - If it succeeds, the function `return`s the integer, which also breaks out of the infinite loop.
    - If it fails, Python raises a `ValueError`, which is caught by the `except ValueError:` block.
4.  **Graceful Handling**: Instead of crashing, the `except` block prints a helpful error message, and the `while` loop ensures the user is prompted again.

## Expected Output

If a user enters invalid data first, the interaction will look like this:

```
Please enter your age: twenty
Invalid input. Please enter a whole number.
Please enter your age: 30

Thank you. You have entered 30 as your age.
```

## Points to Consider

- **User Experience (UX)**: This pattern is fundamental for creating user-friendly applications that don't frustrate users with unexpected crashes.
- **Specificity**: It's good practice to catch specific exceptions (like `ValueError`) rather than a generic `except:`. This prevents you from accidentally hiding other, unexpected bugs.
- **Reusability**: Encapsulating this logic in a function makes it easy to reuse throughout your project.
- **Type Hinting**: Adding type hints (`prompt: str` and `-> int`) makes the function's contract explicit: it expects a string and guarantees it will return an integer. This improves code clarity and allows for static analysis.
