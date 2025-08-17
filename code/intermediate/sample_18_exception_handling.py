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
