# MAIN CODE

"""
Demonstrates the EXHAUSTIVE ENUMERATION algorithm, also known as GUESS AND CHECK.

This algorithm finds a solution to a problem by trying every possible answer
(enumerating all possibilities) until the correct one is found. It is a simple
brute-force approach.

This example uses it to find the integer square root of a number.
"""

# ############################################################################ #
# NOTE: This example uses Type Hinting, a concept explained in detail in      #
# sample_23_type_hinting.py. It is recommended to review that example to fully #
# understand the type annotations used here (e.g., `-> None`, `-> int`).       #
# ############################################################################ #


def find_square_root(target: int) -> None:
    """
    Finds the integer square root of a target number using exhaustive enumeration.

    Args:
        target (int): The number to find the square root of.
    """
    guess: int = 0
    iterations: int = 0

    # We keep guessing until our guess squared is greater than or equal to the target.
    while guess**2 < target:
        guess += 1
        iterations += 1

    print(f"Algorithm finished after {iterations} iterations.")

    # After the loop, we check if we found an exact square root.
    if guess**2 == target:
        print(f"The exact square root of {target} is {guess}.")
    else:
        print(f"{target} does not have an exact integer square root.")


def main() -> None:
    """
    Main function to get user input and run the algorithm.
    """
    print("--- Exhaustive Enumeration: Integer Square Root Finder ---")

    # Get a valid non-negative integer from the user.
    while True:
        try:
            target_number: int = int(input("Enter a non-negative integer: "))
            if target_number < 0:
                print("Error: Please enter a non-negative integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    print()  # Add a blank line for readability.
    find_square_root(target_number)
    print()


if __name__ == "__main__":
    main()
