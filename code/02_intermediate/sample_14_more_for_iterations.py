"""Demonstrates aggregation and enumerate() inside Python for loops."""


def calculate_sum_and_average():
    """Accumulates a list of numbers to compute their sum and average."""
    print("--- Example 1: Calculating Sum and Average ---")
    numbers = [10, 20, 30, 40, 50]
    # Avoid naming this 'sum' to prevent shadowing the built-in sum().
    total = 0
    print(f"Calculating sum and average for the list: {numbers}")

    for num in numbers:
        total += num

    print(f"  - The sum of the numbers is: {total}")
    average = total / len(numbers)
    print(f"  - The average of the numbers is: {average:.2f}")
    print()


def demonstrate_enumerate():
    """Iterates with enumerate() to unpack each item's index and value."""
    print("--- Example 2: Using enumerate() to Get Index and Value ---")
    fruits = ["apple", "banana", "cherry"]
    print(f"Iterating through the list with enumerate: {fruits}")

    for index, fruit in enumerate(fruits):
        print(f"  - Item at index {index} is: {fruit}")
    print()


def main():
    """Runs both practical for loop demonstrations."""
    calculate_sum_and_average()
    demonstrate_enumerate()


if __name__ == "__main__":
    main()
