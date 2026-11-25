"""Demonstrates reading text with input() and converting numeric strings."""


def demonstrate_string_input():
    """Reads string input and prints it using several formatting styles."""
    print("--- String Input ---")
    # input() always returns a str, regardless of what the user types.
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
    """Converts string input to integers before performing arithmetic."""
    print("--- Numeric Input ---")
    age_str = input("Enter your age: ")
    print(f"The type of input received is: {type(age_str)}")

    # int() raises ValueError on non-numeric text; try-except is covered in sample_18.
    age_num = int(age_str)
    print(f"After converting to integer, the type is: {type(age_num)}")
    print(f"In ten years, you will be {age_num + 10} years old.")

    print("\n--- Combined input and conversion ---")
    number = int(input("Enter a number to be multiplied by two: "))
    print(f"{number} * 2 = {number * 2}")
    print()


def main():
    """Runs string and numeric input demonstrations."""
    demonstrate_string_input()
    demonstrate_numeric_input()


if __name__ == "__main__":
    main()
