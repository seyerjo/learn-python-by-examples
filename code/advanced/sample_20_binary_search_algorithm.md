# Binary Search for Solution Finding

This example demonstrates how the binary search algorithm can be adapted to efficiently find a numerical solution, such as the square root of a number.

## Code

```python
""" BINARY SEARCH Algorithm.

    Instead of searching for an item in a list, this algorithm searches for a
    solution within a continuous range of numbers. It repeatedly divides the
    search range in half, discarding the half that cannot contain the solution.

"""

# ############################################################################ #
# NOTE: This example uses Type Hinting, a concept explained in detail in      #
# sample_22_type_hinting.py. It is recommended to review that example to fully #
# understand the type annotations used here (e.g., `-> None`).                 #
# ############################################################################ #


def main() -> None:
    """Main function demonstrating binary search for square root."""
    # Get a valid positive integer from the user
    while True:
        try:
            target = int(input("Enter a positive integer number: "))
            if target < 0:
                print("Error: Please enter a non-negative integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    print()
    epsilon = 0.01  # Precision level
    low = 0.0
    high = max(1.0, target)
    guess = (high + low) / 2

    # Binary search loop
    while abs(guess**2 - target) >= epsilon:
        if guess**2 < target:
            low = guess
        else:
            high = guess
        guess = (high + low) / 2

    print(f"The square root of {target} is approximately {guess:.4f}")


if __name__ == "__main__":
    main()
```

## Explanation

1.  **Search Space**: The algorithm defines a search space for the solution between a `low` and `high` boundary. For a square root, this is between `0` and the number itself.
2.  **Input Validation**: It first gets a valid non-negative integer from the user.
3.  **Midpoint Guess**: The first `guess` is the midpoint of the search space `(high + low) / 2`.
4.  **Halving the Space**: The `while` loop continues as long as the guess is not within the desired `epsilon` (precision).
    - If `guess**2` is too low, we know the answer must be in the upper half, so we set `low = guess`.
    - If `guess**2` is too high, the answer must be in the lower half, so we set `high = guess`.
5.  **Convergence**: With each iteration, the search space (`high` - `low`) is cut in half, allowing the algorithm to converge on the correct answer very quickly.

## Expected Output

```
Enter a positive integer number: 123

The square root of 123 is approximately 11.0905
```

## Points to Consider

- **Efficiency**: Binary search is significantly more efficient than linear approximation. It converges on a solution much faster, especially for large numbers.
- **Conceptual Leap**: This demonstrates that binary search is not just for finding items in discrete lists but is a powerful technique for searching any ordered and continuous solution space.
