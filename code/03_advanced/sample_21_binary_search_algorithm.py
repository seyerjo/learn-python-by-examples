#!/usr/bin/env python3
"""Demonstrates continuous binary search for approximating square roots."""

# Uses PEP 484 type hints; see sample_23_type_hinting.py.

import sys


def find_root_by_binary_search(target: int) -> None:
    """Approximates the square root of a target integer via binary search.

    Args:
        target: Non-negative integer whose square root is approximated.
    """
    epsilon: float = 0.01
    low: float = 0.0
    # Upper bound is at least 1.0 so targets in [0, 1) stay inside the search space.
    high: float = max(1.0, float(target))
    guess: float = (high + low) / 2
    iterations: int = 0

    while abs(guess**2 - target) >= epsilon:
        if guess**2 < target:
            low = guess
        else:
            high = guess

        guess = (high + low) / 2
        iterations += 1

    print(f"Algorithm finished after {iterations} iterations.")
    print(f"The approximate square root of {target} is {guess:.4f}")


def main() -> int:
    """Prompts for a non-negative integer and runs binary search.

    Returns:
        Exit status code (0 on completion, 130 if interrupted via Ctrl-C).
    """
    print("--- Binary Search: Square Root Finder ---")

    try:
        while True:
            try:
                target_number: int = int(input("Enter a non-negative integer: "))
                if target_number < 0:
                    print(
                        "Error: Please enter a non-negative integer.",
                        file=sys.stderr,
                    )
                    continue
                break
            except ValueError:
                print(
                    "Invalid input. Please enter a valid integer.",
                    file=sys.stderr,
                )
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.", file=sys.stderr)
        return 130

    print()
    find_root_by_binary_search(target_number)
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
