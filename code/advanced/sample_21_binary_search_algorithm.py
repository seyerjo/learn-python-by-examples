# MAIN CODE

"""
Demonstrates the BINARY SEARCH algorithm adapted for finding a numerical solution.

This "divide and conquer" algorithm is significantly more efficient than linear
methods like exhaustive enumeration or simple approximation. Instead of checking
every value, it repeatedly divides the search space in half.

This example uses it to find the approximate square root of a number.
"""

# ############################################################################ #
# NOTE: This example uses Type Hinting, a concept explained in detail in      #
# sample_23_type_hinting.py. It is recommended to review that example to fully #
# understand the type annotations used here (e.g., `-> None`, `-> int`).       #
# ############################################################################ #


def find_root_by_binary_search(target: int) -> None:
    """
    Finds an approximate square root using a binary search algorithm.

    Args:
        target (int): The number to find the square root of.
    """
    epsilon: float = 0.01  # Our margin of error.
    low: float = 0.0
    # The answer can't be larger than the target itself (unless target is < 1).
    high: float = max(1.0, float(target))
    guess: float = (high + low) / 2
    iterations: int = 0

    # Continue as long as our guess is not "close enough".
    while abs(guess**2 - target) >= epsilon:
        # If our guess is too low, we know the answer is in the upper half
        # of the current search space. So, we move the 'low' boundary up.
        if guess**2 < target:
            low = guess
        # If our guess is too high, the answer is in the lower half.
        # So, we move the 'high' boundary down.
        else:
            high = guess

        # The new guess is the midpoint of the *new*, smaller search space.
        guess = (high + low) / 2
        iterations += 1

    print(f"Algorithm finished after {iterations} iterations.")
    print(f"The approximate square root of {target} is {guess:.4f}")


def main() -> None:
    """
    Main function to get user input and run the algorithm.
    """
    print("--- Binary Search: Square Root Finder ---")

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
    find_root_by_binary_search(target_number)
    print()


if __name__ == "__main__":
    main()
