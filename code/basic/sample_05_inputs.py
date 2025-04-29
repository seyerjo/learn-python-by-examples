# MAIN CODE

"""Demonstrate different ways to handle user input in Python.

Shows string and numeric input handling, type conversion,
and various output formatting methods.
"""


def main():
    """Main function to demonstrate input handling examples."""
    # String input example
    name = input("What's your name?: ")
    print()  # Single blank line

    # Different output formatting methods
    print(name)
    print("Your name is " + name)
    print("Your name is", name)
    # Using end='\n\n' to print two newlines after the string
    print(f"Your name is {name}", end='\n\n')

    # Numeric input with conversion
    number = input("Enter a number that will be multiplied by two: ")
    number = int(number) * 2
    print(number, end='\n\n')

    # Combined input and conversion
    number = int(input("Enter a number that will be multiplied by two: "))
    print(number * 2)


if __name__ == "__main__":
    main()
