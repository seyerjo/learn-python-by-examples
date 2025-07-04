""" BINARY SEARCH Algorithm.

    The Binary Search Algorithm is an efficient search algorithm for finding an element in a
    sorted list. It works by measuring the middle of the list and determining if the sought
    element is greater or lesser than the element in the middle of the list. If it's greater,
    the lower half of the list is discarded and searched in the upper part; otherwise, the
    upper part of the list is discarded and searched in the lower part. This is repeated until
    the element is found or it is determined that it is not in the list.

    This code calculates the square root of a given integer number. It uses a binary search
    algorithm to find the answer, dividing the search range in half each time. The process
    starts with a lower limit of 0.0 and an upper limit of the given number, or 1.0, whichever
    is greater. The response is calculated as the midpoint of the limits. If the square of the
    response is less than the given number, the lower limit is changed to the response, otherwise
    the upper limit is changed to the response. The process is repeated until the difference
    between the square of the response and the given number is less than a certain amount
    (epsilon). After this, the response is printed as the square root of the given number.

"""

# ############################################################################ #
# NOTE: This example uses Type Hinting, a concept explained in detail in      #
# sample_23_type_hinting.py. It is recommended to review that example to fully #
# understand the type annotations used here (e.g., `-> None`).                 #
# ############################################################################ #


def main() -> None:
    """Main function demonstrating binary search algorithm for square root."""
    # Get a valid positive integer from the user
    while True:
        try:
            target: int = int(input("Enter a positive integer number: "))
            if target < 0:
                print("Error: Please enter a non-negative integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    print()  # Blank line
    epsilon: float = 0.01  # Precision level
    low: float = 0.0
    # Ensure high uses float for max comparison
    high: float = max(1.0, float(target))
    guess: float = (high + low) / 2  # Initial guess

    # Binary search loop
    while abs(guess**2 - target) >= epsilon:
        print(f"Search range: [{low:.4f}, {high:.4f}], Guess: {guess:.4f}")

        if guess**2 < target:
            low = guess
        else:
            high = guess

        guess = (high + low) / 2  # New guess

    print()  # Blank line
    print(f"The square root of {target} is approximately {guess:.4f}")


if __name__ == "__main__":
    main()
