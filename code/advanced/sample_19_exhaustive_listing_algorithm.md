# Exhaustive Enumeration (Guess and Check)

This example demonstrates the exhaustive enumeration algorithm, also known as "guess and check," to find the exact square root of an integer.

## Code

```python
""" EXHAUSTIVE LISTING algorithm, also called GUESS AND CHECK.

    This algorithm iterates through all possible solutions to find the correct
    one. In this case, it starts guessing from 0 and increments by 1 until
    its square is equal to or greater than the target number.

"""

# ############################################################################ #
# NOTE: This example uses Type Hinting, a concept explained in detail in      #
# sample_23_type_hinting.py. It is recommended to review that example to fully #
# understand the type annotations used here (e.g., `-> None`).                 #
# ############################################################################ #


def main() -> None:
    """Main function to demonstrate exhaustive listing algorithm."""
    # Get a valid non-negative integer from the user
    while True:
        try:
            target_number = int(input("Enter an integer number: "))
            if target_number < 0:
                print("Please enter a non-negative integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    print()

    # Find square root by exhaustive listing
    guess = 0
    while guess**2 < target_number:
        guess += 1

    # Check if a perfect square was found
    if guess**2 == target_number:
        print(f"The square root of {target_number} is {guess}")
    else:
        print(f"{target_number} does not have an exact square root")


if __name__ == "__main__":
    main()
```

## Explanation

1. An exhaustive listing algorithm involves listing all possible solutions or elements.
2. The `exhaustive_listing` function takes a list of items and prints each one.

## Expected Output

When you run this code, it will print the elements of the `items` list.

## Points to Consider

- Exhaustive listing can be useful for small datasets but may be impractical for large ones.
- It's a straightforward approach to ensure all elements are considered.
