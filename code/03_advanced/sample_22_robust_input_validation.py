#!/usr/bin/env python3
"""Demonstrates a reusable, type-safe numeric input validation helper."""

# Uses PEP 484 type hints; see sample_23_type_hinting.py.

import sys


def get_valid_number(
    prompt: str,
    num_type: type[int | float] = int,
    min_val: int | float | None = None,
    max_val: int | float | None = None,
) -> int | float:
    """Repeatedly prompts until a numeric input matches the required type and bounds.

    Args:
        prompt: Prompt text displayed to the user.
        num_type: Target numeric converter (`int` or `float`).
        min_val: Inclusive lower bound, or None for no lower bound.
        max_val: Inclusive upper bound, or None for no upper bound.

    Returns:
        Validated number converted via `num_type`.
    """
    while True:
        try:
            number = num_type(input(prompt))

            # Explicit `is not None` prevents 0 or 0.0 bounds from being skipped.
            if min_val is not None and number < min_val:
                print(
                    f"Error: The value must be at least {min_val}.",
                    file=sys.stderr,
                )
                continue

            if max_val is not None and number > max_val:
                print(
                    f"Error: The value must be no more than {max_val}.",
                    file=sys.stderr,
                )
                continue

            return number
        except ValueError:
            print(
                f"Invalid input. Please enter a valid {num_type.__name__}.",
                file=sys.stderr,
            )


def main() -> int:
    """Demonstrates reusable validation across three numeric constraints.

    Returns:
        Exit status code (0 on completion, 130 if interrupted via Ctrl-C).
    """
    print("--- Demonstrating a general-purpose number validation function ---\n")

    try:
        age = get_valid_number("Please enter your age (any integer): ")
        print(f"Valid age entered: {age}\n")

        probability = get_valid_number(
            "Enter a probability (a decimal between 0.0 and 1.0): ",
            num_type=float,
            min_val=0.0,
            max_val=1.0,
        )
        print(f"Valid probability entered: {probability}\n")

        rating = get_valid_number(
            "Please rate our service (an integer from 1 to 5): ",
            num_type=int,
            min_val=1,
            max_val=5,
        )
        print(f"Valid rating entered: {rating}\n")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.", file=sys.stderr)
        return 130

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
