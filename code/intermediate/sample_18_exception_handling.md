# Exception Handling: The `try-except-else-finally` Block

In programming, an "exception" is an error that occurs during program execution. Python uses **exception handling** to manage these errors gracefully, preventing the program from crashing.

This example demonstrates the full power of Python's exception handling by using the complete `try-except-else-finally` structure.

## The `try-except-else-finally` Structure

This structure provides a robust way to control program flow when errors might occur.

1.  **`try`**: You place the code that might raise an exception inside the `try` block.
2.  **`except`**: If an error occurs in the `try` block, Python looks for a matching `except` block to handle it. You can have multiple `except` blocks to handle different, specific types of exceptions.
3.  **`else`**: The code in the `else` block is executed **only if no exceptions were raised** in the `try` block. It's useful for code that should run only when the initial operation was successful.
4.  **`finally`**: The code in the `finally` block is **always executed**, no matter what. It runs whether an exception occurred or not. This is the perfect place for cleanup actions, like closing a file or a network connection.

## Code

The following code implements a "Safe Division Calculator" that asks the user for two numbers and demonstrates how each part of the `try-except-else-finally` block works.

```python
# MAIN CODE

"""
Demonstrates the full structure of exception handling in Python using a
`try-except-else-finally` block.

This example shows how to handle multiple, specific exceptions and how to use
the `else` and `finally` clauses for more robust program flow.
"""


def safe_division():
    """
    Performs division on two numbers entered by the user, handling potential
    errors gracefully.
    """
    print("--- Safe Division Calculator ---")
    print("This program will calculate numerator / denominator.")

    try:
        # The `try` block contains code that might raise an error.
        numerator_str = input("Enter the numerator: ")
        numerator = float(numerator_str)

        denominator_str = input("Enter the denominator: ")
        denominator = float(denominator_str)

        result = numerator / denominator

    except ValueError:
        # This block runs ONLY if a `ValueError` occurs (e.g., `float("abc")`).
        print("\nError: Invalid input. Please enter valid numbers.")

    except ZeroDivisionError:
        # This block runs ONLY if a `ZeroDivisionError` occurs.
        print("\nError: Cannot divide by zero.")

    else:
        # The `else` block runs ONLY if NO exceptions occurred in the `try` block.
        print(f"\nSuccess! The result of the division is: {result:.2f}")

    finally:
        # The `finally` block runs ALWAYS, regardless of whether an exception
        # occurred or not. It's often used for cleanup operations.
        print("\n--- Calculation attempt finished. ---")


def main():
    """Main function to demonstrate the exception handling example."""
    safe_division()


if __name__ == "__main__":
    main()
```

## How to Run and Test

Run the script and try entering different values to see how each block is executed:

1.  **Successful Case**: Enter `10` and `5`. The `try` and `else` blocks will run, followed by `finally`.
2.  **`ValueError` Case**: Enter `abc` for the numerator. The `try` block will fail, and the `except ValueError` block will run, followed by `finally`.
3.  **`ZeroDivisionError` Case**: Enter `10` for the numerator and `0` for the denominator. The `try` block will fail, and the `except ZeroDivisionError` block will run, followed by `finally`.

## Expected Output

### Scenario 1: Success

```
--- Safe Division Calculator ---
This program will calculate numerator / denominator.
Enter the numerator: 10
Enter the denominator: 4

Success! The result of the division is: 2.50

--- Calculation attempt finished. ---
```

### Scenario 2: Invalid Input

```
--- Safe Division Calculator ---
This program will calculate numerator / denominator.
Enter the numerator: ten

Error: Invalid input. Please enter valid numbers.

--- Calculation attempt finished. ---
```

### Scenario 3: Division by Zero

```
--- Safe Division Calculator ---
This program will calculate numerator / denominator.
Enter the numerator: 10
Enter the denominator: 0

Error: Cannot divide by zero.

--- Calculation attempt finished. ---
```
