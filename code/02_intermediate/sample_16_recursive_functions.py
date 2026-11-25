"""Demonstrates recursion with a factorial calculator and recursive input retry."""


def factorial(n):
    """Calculates the factorial of a non-negative integer recursively.

    Args:
        n: Non-negative integer whose factorial is computed.

    Returns:
        Factorial of n (n!).

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    # Base case stops the recursion.
    if n == 0:
        return 1

    return n * factorial(n - 1)


def get_non_negative_integer():
    """Prompts recursively until the user enters a non-negative integer.

    Returns:
        Valid non-negative integer entered by the user.
    """
    try:
        num = int(input("Enter a non-negative integer (e.g., 0, 1, 5): "))
        if num >= 0:
            return num
        print("The number must be non-negative. Please try again.")
        return get_non_negative_integer()
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return get_non_negative_integer()


def main():
    """Prompts for an integer and prints its recursively computed factorial."""
    print("--- Recursive Factorial Calculator ---")
    number_to_calculate = get_non_negative_integer()

    try:
        result = factorial(number_to_calculate)
        print(f"\nThe factorial of {number_to_calculate} is {result}.\n")
    except ValueError as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()
