# MAIN CODE

"""Demonstrate for loops with list operations in Python.

Shows how to calculate sum and average of numbers in a list.
"""


def main():
    """Main function demonstrating list operations with for loops."""
    numbers = [1, 2, 3, 4, 5]
    print(f"For this list of numbers: {numbers}", end='\n\n')

    # Calculate sum of numbers
    total = 0  # Avoid using 'sum' as it's a built-in function
    for num in numbers:
        total += num

    print(f"The sum is: {total}", end='\n\n')

    # Calculate average
    average = total / len(numbers)
    print(f"The average is: {average:.2f}", end='\n\n')


if __name__ == "__main__":
    main()
