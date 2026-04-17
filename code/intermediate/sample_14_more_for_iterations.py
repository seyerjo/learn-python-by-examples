# MAIN CODE

"""
Demonstrates practical applications and useful tools for `for` loops in Python.

This example covers two key topics:
1.  A common use case: calculating the sum and average of numbers in a list.
2.  Using the built-in `enumerate()` function to get both the index and the
    value of items in a sequence during iteration.
"""


def calculate_sum_and_average():
    """
    Iterates through a list of numbers to calculate their sum and average.
    """
    print("--- Example 1: Calculating Sum and Average ---")
    numbers = [10, 20, 30, 40, 50]
    total = 0
    print(f"Calculating sum and average for the list: {numbers}")

    # The for loop iterates through each number in the list.
    for num in numbers:
        total += num  # Add the current number to the total.

    # It's good practice to avoid using 'sum' as a variable name because it
    # shadows the built-in sum() function.

    print(f"  - The sum of the numbers is: {total}")

    # Calculate the average by dividing the sum by the number of items.
    average = total / len(numbers)
    print(f"  - The average of the numbers is: {average:.2f}")
    print()


def demonstrate_enumerate():
    """
    Shows how to use enumerate() to get the index and value of each item.
    """
    print("--- Example 2: Using enumerate() to Get Index and Value ---")
    fruits = ["apple", "banana", "cherry"]
    print(f"Iterating through the list with enumerate: {fruits}")

    # enumerate() returns a tuple containing the index and the value for each item.
    # We can unpack this tuple directly into two variables (e.g., `index`, `fruit`).
    for index, fruit in enumerate(fruits):
        print(f"  - Item at index {index} is: {fruit}")
    print()


def main():
    """Main function to demonstrate practical `for` loop examples."""
    calculate_sum_and_average()
    demonstrate_enumerate()


if __name__ == "__main__":
    main()
