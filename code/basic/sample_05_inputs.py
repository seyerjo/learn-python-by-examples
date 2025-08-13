# MAIN CODE

"""
Demonstrates different ways to handle user input in Python, highlighting
the crucial difference between reading strings and numbers.
"""


def demonstrate_string_input():
    """Shows how to get string input and display it in various ways."""
    print("--- String Input ---")
    # The input() function always reads user input as a string.
    name = input("What's your name?: ")

    print("\n--- Different ways to display the string ---")
    print("1. Simple print:")
    print(name)

    print("\n2. Concatenation with '+':")
    print("Your name is " + name)

    print("\n3. Multiple arguments in print():")
    print("Your name is", name)

    print("\n4. Using an f-string (modern and recommended):")
    print(f"Your name is {name}")
    print()


def demonstrate_numeric_input():
    """Shows how to handle numeric input and the need for type conversion."""
    print("--- Numeric Input ---")
    print("The input() function returns a string, so we must convert it to a "
          "number for math.")

    # Step-by-step conversion
    age_str = input("Enter your age: ")
    print(f"The type of input received is: {type(age_str)}")

    # IMPORTANT: The int() function converts a string to an integer.
    # This line will cause a ValueError if you enter non-numeric text.
    # A robust solution using try-except is covered in sample_18.
    age_num = int(age_str)
    print(f"After converting to integer, the type is: {type(age_num)}")
    print(f"In ten years, you will be {age_num + 10} years old.")

    print("\n--- Combined input and conversion ---")
    # This is a more common, compact way to do it.
    number = int(input("Enter a number to be multiplied by two: "))
    print(f"{number} * 2 = {number * 2}")
    print()


def main():
    """Main function to demonstrate input handling examples."""
    demonstrate_string_input()
    demonstrate_numeric_input()


if __name__ == "__main__":
    main()
