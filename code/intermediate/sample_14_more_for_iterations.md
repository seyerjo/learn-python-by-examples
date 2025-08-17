# More `for` Loop Examples in Python

This example demonstrates more practical applications of `for` loops and introduces the powerful `enumerate()` function, which is frequently used when iterating.

We will cover two topics:

1.  A common practical task: calculating the sum and average of numbers in a list.
2.  Using the `enumerate()` function to access both the index and the value of an item during iteration.

## Code

The following code is divided into two functions, each demonstrating one of the concepts above.

```python
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
```

## Explanation

### 1. Calculating Sum and Average

-   **Concept**: This is a classic example of how a `for` loop is used to process items in a list. We initialize a `total` variable to zero, then loop through each `num` in the `numbers` list, adding it to our `total`. Finally, we calculate the average.
-   **Expected Output**:
    ```
    --- Example 1: Calculating Sum and Average ---
    Calculating sum and average for the list: [10, 20, 30, 40, 50]
      - The sum of the numbers is: 150
      - The average of the numbers is: 30.00
    ```

### 2. Using `enumerate()` to Get Index and Value

-   **Concept**: Often when looping, you need to know the position (or index) of the item you are currently processing. The `enumerate()` function makes this easy. It takes a sequence (like a list) and returns a series of pairs, where each pair contains the index and the item at that index.
-   **In the code**: `for index, fruit in enumerate(fruits):` is a clean way to get both the `index` (0, 1, 2, ...) and the `fruit` ('apple', 'banana', ...) in each iteration.
-   **Expected Output**:
    ```
    --- Example 2: Using enumerate() to Get Index and Value ---
    Iterating through the list with enumerate: ['apple', 'banana', 'cherry']
      - Item at index 0 is: apple
      - Item at index 1 is: banana
      - Item at index 2 is: cherry
    ```

## Points to Consider

-   Using a `for` loop for aggregation tasks like calculating a sum is a fundamental pattern in programming.
-   `enumerate()` is the preferred "Pythonic" way to access item indexes within a loop. It is much more readable and less error-prone than manually managing a counter variable (e.g., `i = 0; ...; i += 1`).
