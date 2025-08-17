# Recursive Functions in Python

A **recursive function** is a function that calls itself to solve a problem. Recursion is a powerful programming concept where a problem is broken down into smaller, self-similar subproblems. A recursive function needs two key components:

1.  **Base Case**: A condition that stops the recursion. Without a base case, the function would call itself indefinitely, leading to a "maximum recursion depth exceeded" error.
2.  **Recursive Step**: The part of the function that calls itself, typically with a modified argument that moves it closer to the base case.

This example demonstrates recursion by implementing a robust factorial calculator.

## Code

The following code defines a recursive function to calculate the factorial of a number and another to get valid user input.

```python
# MAIN CODE

"""
Demonstrates recursive functions in Python.

A recursive function is a function that calls itself to solve a problem.
This example shows two common use cases:
1.  Calculating the factorial of a number.
2.  Recursively validating user input until it is correct.
"""


def factorial(n):
    """
    Calculates the factorial of a non-negative integer recursively.

    A factorial is the product of all positive integers up to that number.
    e.g., 5! = 5 * 4 * 3 * 2 * 1 = 120.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The factorial of n.

    Raises:
        ValueError: If n is a negative number.
    """
    # Validate input: Factorial is not defined for negative numbers.
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    # Base case: The condition that stops the recursion.
    # The factorial of 0 is 1.
    if n == 0:
        return 1

    # Recursive step: The function calls itself with a smaller version
    # of the problem.
    return n * factorial(n - 1)


def get_non_negative_integer():
    """
    Recursively prompts the user until a non-negative integer is entered.

    Returns:
        int: A valid non-negative integer from the user.
    """
    try:
        num = int(input("Enter a non-negative integer (e.g., 0, 1, 5): "))
        if num >= 0:
            return num
        else:
            print("The number must be non-negative. Please try again.")
            return get_non_negative_integer()  # Recursive call
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return get_non_negative_integer()  # Recursive call


def main():
    """Main function to demonstrate recursive functions."""
    print("--- Recursive Factorial Calculator ---")

    number_to_calculate = get_non_negative_integer()

    try:
        result = factorial(number_to_calculate)
        print(f"\nThe factorial of {number_to_calculate} is {result}.\n")
    except ValueError as e:
        # This part will catch the error raised by our validation.
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

## Explanation

### The `factorial` function

1.  **Input Validation**: The first `if` statement checks if the number `n` is negative. Since factorials are not defined for negative numbers, it raises a `ValueError` to prevent invalid calculations. This makes the function more robust.
2.  **Base Case**: The condition `if n == 0:` is the crucial base case. The factorial of 0 is defined as 1. When the function receives 0, it stops calling itself and returns 1, which allows the chain of recursive calls to resolve.
3.  **Recursive Step**: The line `return n * factorial(n - 1)` is the recursive part. The function calls itself with a slightly smaller problem (`n - 1`). Each call waits for the next one to finish, and the results are multiplied up the chain.

    -   `factorial(3)` returns `3 * factorial(2)`
    -   `factorial(2)` returns `2 * factorial(1)`
    -   `factorial(1)` returns `1 * factorial(0)`
    -   `factorial(0)` returns `1` (the base case)
    -   The results are then multiplied back: `1 * 1` -> `2 * 1` -> `3 * 2` = `6`.

### The `get_non_negative_integer` function

This function also uses recursion to ensure it gets valid input. If the user enters invalid text (like "abc") or a negative number, the function prints an error message and then **calls itself** to ask for input again. It only returns a value when the input is a valid, non-negative integer.

## Expected Output

If the user enters `5`:

```
--- Recursive Factorial Calculator ---
Enter a non-negative integer (e.g., 0, 1, 5): 5

The factorial of 5 is 120.
```

If the user enters invalid input first:

```
--- Recursive Factorial Calculator ---
Enter a non-negative integer (e.g., 0, 1, 5): abc
Invalid input. Please enter a valid integer.
Enter a non-negative integer (e.g., 0, 1, 5): -2
The number must be non-negative. Please try again.
Enter a non-negative integer (e.g., 0, 1, 5): 0

The factorial of 0 is 1.
```
