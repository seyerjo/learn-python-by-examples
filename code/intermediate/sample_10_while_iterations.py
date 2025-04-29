# MAIN CODE

"""Demonstrate basic while loop iteration in Python.

Shows a simple counter that increments from 0 to 9.
"""


def main():
    """Main function demonstrating while loop usage."""
    counter = 0  # Initialize counter

    # Loop while counter is less than 10
    while counter < 10:
        print(counter)
        counter += 1  # Increment counter

    print()  # Final newline


if __name__ == "__main__":
    main()
