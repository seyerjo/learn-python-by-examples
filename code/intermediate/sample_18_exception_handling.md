# Exception Handling: `try-except` for Robust Input

## 1. Introduction to Exception Handling

In programming, an "exception" is an event that occurs during the execution of a program that disrupts the normal flow of instructions. When an error occurs, Python raises an exception. If unhandled, this can lead to your program crashing.

"Exception handling" is the mechanism that allows you to "catch" these errors and respond to them gracefully, preventing crashes and providing a better user experience.

## 2. The `try-except` Block

The primary construct in Python for handling exceptions is the `try-except` block.

- The `try` block contains the code that might raise an exception.
- The `except` block contains the code that will be executed if a specific type of exception occurs within the `try` block.

**Syntax:**

```python
try:
    # Code that might cause an error
    # (e.g., type conversion, file operations)
except ExceptionType:
    # Code to handle the error
    # (e.g., print an error message, ask for input again)
```

## 3. Robust Input Validation with `try-except`

A common scenario where `try-except` is invaluable is when handling user input. Users might accidentally or intentionally enter data that is not in the expected format (e.g., entering "hello" when a number is required). Without exception handling, `int("hello")` would cause a `ValueError` and crash your program.

This example demonstrates how to create a robust input function that repeatedly prompts the user until a valid integer is provided, ensuring your program continues to run smoothly.

## 4. `sample_18_exception_handling.py` Explained

The script defines a function `get_integer_input()` that takes a `prompt` string as an argument.

1.  **Infinite Loop (`while True`):** The function uses an infinite loop to keep asking for input.
2.  **`try` Block:**
    - It attempts to get `user_input` using `input(prompt)`.
    - It then tries to convert `user_input` to an integer using `int()`.
    - If successful, the `number` is returned, and the `while True` loop is exited.
3.  **`except ValueError` Block:**
    - If `int(user_input)` raises a `ValueError` (because the input was not a valid integer), the code within this block is executed.
    - An informative error message (`"Invalid input. Please enter a whole number."`) is printed to the user.
    - The loop then continues (`while True`), prompting the user again for input.

The `main()` function calls `get_integer_input()` to demonstrate its usage, showing how it gracefully handles incorrect entries.

## 5. How to Run the Example

1.  Navigate to the `code/intermediate/` directory in your terminal.
2.  Run the script using Python:

    ```bash
    python sample_18_exception_handling.py
    ```

    or

    ```bash
    python3 sample_18_exception_handling.py
    ```

3.  The program will ask you to enter your age. Try entering text (e.g., "abc") and observe how the program informs you of the error and asks again. Then, enter a valid number.

## 6. Expected Output

When running the script, you will see output similar to this:

```
--- Integer Input Validation Example ---
Please enter your age: abc
Invalid input. Please enter a whole number.
Please enter your age: twenty
Invalid input. Please enter a whole number.
Please enter your age: 30
Thank you. You have entered 30 as your age.
```
