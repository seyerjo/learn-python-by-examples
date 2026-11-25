"""Demonstrates iterating over lists, strings, and ranges with for loops."""


def iterate_over_list():
    """Iterates over each element in a list."""
    print("--- Example 1: Iterating over a list ---")
    fruits = ["apple", "banana", "cherry"]
    print(f"Iterating through the list: {fruits}")
    for fruit in fruits:
        print(f"  - Current fruit: {fruit}")
    print()


def iterate_over_string():
    """Iterates over each character in a string."""
    print("--- Example 2: Iterating over a string ---")
    word = "Python"
    print(f"Iterating through the characters of the word: '{word}'")
    for letter in word:
        print(f"  - Current letter: {letter}")
    print()


def iterate_with_range():
    """Iterates over a generated numeric sequence using range()."""
    print("--- Example 3: Iterating with range() ---")
    print("Looping from 0 to 4 using range(5):")
    # range(5) yields 0 through 4 (stop is exclusive).
    for number in range(5):
        print(f"  - Current number: {number}")
    print()


def main():
    """Runs all for loop demonstrations."""
    iterate_over_list()
    iterate_over_string()
    iterate_with_range()


if __name__ == "__main__":
    main()
