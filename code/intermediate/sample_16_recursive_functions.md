# Recursive Functions in Python

This example demonstrates how to use recursive functions in Python.

## Code

```python
"""Demonstrate recursive functions in Python.

Shows factorial calculation and recursive user input validation.
"""


def factorial(n):
    """Calculate the factorial of a positive integer recursively."""
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * factorial(n - 1)


def get_positive_number():
    """Recursively request a positive integer from the user."""
    try:
        num = int(input("Enter a positive integer: "))
        if num >= 0:
            return num
        print("Number must be positive or zero. Try again.")
        return get_positive_number()
    except ValueError:
        print("Invalid input. Please enter a number.")
        return get_positive_number()


def main():
    """Main function to demonstrate recursive functions."""
    print("\n>>> Factorial Calculator <<<", end='\n\n')

    number = get_positive_number()
    print(f"\nThe factorial of {number} is {factorial(number)}", end='\n\n')


if __name__ == "__main__":
    main()
```

## Explanation

1. A recursive function is a function that calls itself.
2. The `factorial` function calculates the factorial of a number `n` by calling itself with `n-1` until it reaches the base case (`n == 0`).
3. The base case returns 1, and the recursive calls return the product of `n` and the factorial of `n-1`.

## Expected Output

When you run this code, it will print the factorial of 5.

## Points to Consider

- Recursive functions can be an elegant way to solve problems that have a recursive structure.
- Be cautious to avoid infinite recursion by ensuring a proper base case.
