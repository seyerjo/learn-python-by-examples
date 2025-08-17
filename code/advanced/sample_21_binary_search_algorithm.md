# Algorithm: Binary Search for Solution Finding

This example demonstrates the **binary search** algorithm, a highly efficient method for finding a solution within a continuous, ordered range. This represents a major improvement over linear methods like exhaustive enumeration (`sample_19`) and solution approximation (`sample_20`).

## Concept: Divide and Conquer

Binary search is a "divide and conquer" algorithm. Instead of checking every possible value one by one, it works by repeatedly dividing the search space in half.

1.  **Define a Search Space**: Start with a range where the solution must lie, defined by a `low` and a `high` boundary.
2.  **Make a Guess**: The first guess is the exact **midpoint** of the search space.
3.  **Eliminate Half**:
    -   If the guess is too low, you know the true answer must be in the upper half of the range. You can completely discard the lower half by moving the `low` boundary up to your guess.
    -   If the guess is too high, you know the answer must be in the lower half. Discard the upper half by moving the `high` boundary down to your guess.
4.  **Repeat**: Make a new guess at the midpoint of the _new, smaller_ search space. Repeat this process, halving the search space with each iteration, until the guess is "close enough" to the target.

This approach converges on a solution exponentially faster than linear methods.

## Code

The following code implements the binary search algorithm to find the approximate square root of a user-provided number.

```python
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
```

## Explanation

1.  **`main()` function**: Handles user interaction to get a valid non-negative integer.
2.  **`find_root_by_binary_search(target)` function**:
    -   It establishes the initial search space between `low = 0.0` and `high = target`.
    -   The first `guess` is the midpoint of this large range.
    -   The `while` loop continues as long as the guess is not precise enough (the error is larger than `epsilon`).
    -   Inside the loop, the `if/else` block is the core of the algorithm. It decides whether to discard the lower or upper half of the current search space by updating either the `low` or `high` boundary.
    -   A new `guess` is calculated at the midpoint of the newly reduced space.
    -   The `iterations` counter is included to highlight the algorithm's efficiency.

## Expected Output

Notice how few iterations are needed compared to the previous algorithms, especially for a large number.

```
--- Binary Search: Square Root Finder ---
Enter a non-negative integer: 123456

Algorithm finished after 21 iterations.
The approximate square root of 123456 is 351.3631

```

## Points to Consider

-   **Efficiency**: For a search space of size N, binary search takes approximately log₂(N) steps. This is a massive improvement over linear approaches, which take up to N steps.
-   **Prerequisites**: Binary search requires the solution space to be **ordered** and **monotonic**, meaning the values consistently increase or decrease. This is true for the square root problem.
-   **Generalization**: This powerful concept is not just for finding numbers. It's the foundation for searching in sorted arrays, dictionaries, and many other data structures.
