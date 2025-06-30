# MAIN CODE

"""Demonstrate recursive functions in Python.

Shows factorial calculation and recursive user input validation.
"""


def factorial(n):
    """Calculate the factorial of a positive integer recursively.

    Args:
        n (int): Positive integer to calculate factorial for

    Returns:
        int: Factorial of n
    """
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * factorial(n - 1)


def get_positive_number():
    """Recursively request a positive integer from the user.

    Returns:
        int: Valid positive integer entered by user
    """
    try:
        num = int(input("Enter a positive integer: "))
        if num > 0:
            return num
        print("Number must be greater than 0. Try again.")
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
