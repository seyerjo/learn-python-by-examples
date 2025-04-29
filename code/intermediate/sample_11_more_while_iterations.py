# MAIN CODE

"""Demonstrate nested while loops in Python.

Shows how to use nested loops to print combinations of numbers.
"""


def main():
    """Main function demonstrating nested while loops."""
    outer_count = 0  # Outer loop counter

    # Outer loop runs 5 times
    while outer_count < 5:
        inner_count = 0  # Inner loop counter

        # Inner loop runs 6 times
        while inner_count < 6:
            print(outer_count, inner_count)
            inner_count += 1  # Increment inner counter

        outer_count += 1  # Increment outer counter

    print()  # Final newline


if __name__ == "__main__":
    main()
