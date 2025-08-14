# Flow Control in Python

This example illustrates fundamental techniques for controlling the flow of a program using conditional statements. It covers three core patterns:

1.  A basic `if-elif-else` chain for multiple exclusive conditions.
2.  Using logical operators like `and` within an `if` statement to check for multiple conditions simultaneously.
3.  Nested `if` statements to handle sub-conditions.

## Code

```python
# MAIN CODE

"""
Demonstrates basic flow control in Python using if-elif-else,
logical operators, and nested if statements.
"""


def demonstrate_if_elif_else():
    """Compares two integers to show basic if-elif-else structure."""
    print("--- Example 1: Basic if-elif-else ---")
    # IMPORTANT: The int() function will cause a ValueError if you enter
    # non-numeric text. A robust solution is covered in sample_18.
    num_1 = int(input("Enter the first integer: "))
    num_2 = int(input("Enter the second integer: "))

    if num_1 > num_2:
        result = f"The first number ({num_1}) is greater than the second ({num_2})."
    elif num_1 < num_2:
        result = f"The second number ({num_2}) is greater than the first ({num_1})."
    else:
        result = f"Both numbers are equal ({num_1})."
    print(f"Result: {result}\n")


def demonstrate_logical_flow():
    """Uses the 'and' operator to check if a number is within a range."""
    print("--- Example 2: Flow Control with Logical 'and' ---")
    # IMPORTANT: Vulnerable to ValueError. See sample_18 for the solution.
    age = int(input("Enter your age: "))

    if age > 0 and age < 18:
        print("You are a minor.")
    elif age >= 18 and age < 65:
        print("You are an adult.")
    else:
        print("You are a senior citizen.")
    print()


def demonstrate_nested_if():
    """Shows a nested if statement to check a sub-condition."""
    print("--- Example 3: Nested if Statements ---")
    # Using .lower() to make the comparison case-insensitive
    user_role = input("Enter user role (admin/user): ").lower()
    is_active_str = input("Is the user active? (yes/no): ").lower()

    if user_role == "admin":
        print("Admin access granted.")
        # This 'if' is nested inside the first one.
        if is_active_str == "yes":
            print("User is active and can make changes.")
        else:
            print("User is inactive and has read-only access.")
    else:
        print("General user access granted.")
    print()


def main():
    """Main function to demonstrate all flow control examples."""
    demonstrate_if_elif_else()
    demonstrate_logical_flow()
    demonstrate_nested_if()


if __name__ == "__main__":
    main()
```

## Explanation

1.  **`if-elif-else` Chain**: This is the standard way to check a series of mutually exclusive conditions. Python evaluates each condition from top to bottom and executes the code block for the _first_ one that is `True`. If none are `True`, the `else` block is executed.

2.  **Logical Operators in `if`**: You can create more complex conditions by combining them with logical operators. The `and` operator requires _both_ conditions to be `True` for the entire expression to be `True`. This is perfect for checking if a value falls within a range.

3.  **Nested `if` Statements**: Placing one `if` statement inside another allows for more granular control. The inner `if` is only checked if the outer `if`'s condition is met. This is useful for checking a secondary condition after a primary one has been confirmed.

## Expected Output

The output is interactive and will depend on your inputs. Here is an example of a complete session:

```
--- Example 1: Basic if-elif-else ---
Enter the first integer: 25
Enter the second integer: 50
Result: The second number (50) is greater than the first (25).

--- Example 2: Flow Control with Logical 'and' ---
Enter your age: 35
You are an adult.

--- Example 3: Nested if Statements ---
Enter user role (admin/user): admin
Is the user active? (yes/no): yes
Admin access granted.
User is active and can make changes.

```

## Points to Consider

-   Flow control statements like `if`, `elif`, and `else` are the fundamental building blocks for creating programs that can make decisions.
-   Pay close attention to indentation. In Python, the indentation level defines which block of code a statement belongs to.
-   **`ValueError` Risk**: The examples that convert input to an integer with `int()` will crash if you provide text. The correct, robust way to handle this is with `try-except` blocks, which is covered in `sample_18_exception_handling.py`.
