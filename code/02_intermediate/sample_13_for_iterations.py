# MAIN CODE

"""
Demonstrates the versatility of the `for` loop in Python.

A `for` loop is used for iterating over a sequence (that is either a list,
a tuple, a dictionary, a set, or a string). This is less like the `for`
keyword in other programming languages, and works more like an iterator
method as found in other object-orientated programming languages.
"""


def iterate_over_list():
    """Shows how to iterate over each item in a list."""
    print("--- Example 1: Iterating over a list ---")
    fruits = ["apple", "banana", "cherry"]
    print(f"Iterating through the list: {fruits}")
    for fruit in fruits:
        print(f"  - Current fruit: {fruit}")
    print()


def iterate_over_string():
    """Shows that a string is a sequence of characters and can be iterated."""
    print("--- Example 2: Iterating over a string ---")
    word = "Python"
    print(f"Iterating through the characters of the word: '{word}'")
    for letter in word:
        print(f"  - Current letter: {letter}")
    print()


def iterate_with_range():
    """
    Shows how to use the range() function to generate a sequence of numbers
    to loop through, which is useful when you need to perform an action a
    specific number of times.
    """
    print("--- Example 3: Iterating with range() ---")
    # range(5) generates numbers from 0 up to (but not including) 5.
    print("Looping from 0 to 4 using range(5):")
    for number in range(5):
        print(f"  - Current number: {number}")
    print()


def main():
    """Main function to demonstrate all `for` loop examples."""
    iterate_over_list()
    iterate_over_string()
    iterate_with_range()


if __name__ == "__main__":
    main()
