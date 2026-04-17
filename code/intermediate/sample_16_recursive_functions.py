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
