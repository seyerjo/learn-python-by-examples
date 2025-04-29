# MAIN CODE

"""Demonstrate nested while loops with break statement in Python.

Shows how to use nested loops with conditional break to control iterations.
The inner loop breaks when counter reaches 3, despite having a higher limit.
"""


def main():
    """Main function demonstrating nested while loops with break."""
    outer_count = 0  # Outer loop counter

    # Outer loop runs 5 times
    while outer_count < 5:
        inner_count = 0  # Inner loop counter

        # Inner loop breaks when count reaches 3
        while inner_count < 6:
            print(outer_count, inner_count)
            inner_count += 1

            # Exit inner loop early when count reaches 3
            if inner_count >= 3:
                break

        outer_count += 1  # Increment outer counter

    print()  # Final newline


if __name__ == "__main__":
    main()
