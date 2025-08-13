# Getting User Input in Python

This example shows how to get input from the user in Python. It highlights the critical difference between reading text (strings) and reading numbers, which requires type conversion.

## Code

```python
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
```

## Explanation

1.  **`input()` Function**: This built-in function pauses the program and waits for the user to type something and press Enter. It **always** returns the user's entry as a **string**.

2.  **String Input**: When we ask for a name, the string returned by `input()` is exactly what we need. We can then print it in various ways, with f-strings (`f"..."`) being the most modern and flexible method.

3.  **Numeric Input & Type Conversion**: When we need to perform mathematical operations, we cannot use the string directly. We must convert it to a numeric type, such as an integer, using the `int()` function. This process is called **type casting** or **type conversion**.

## Expected Output

The output will vary based on what you enter. Here is an example session:

```
--- String Input ---
What's your name?: Alex

--- Different ways to display the string ---
1. Simple print:
Alex

2. Concatenation with '+':
Your name is Alex

3. Multiple arguments in print():
Your name is Alex

4. Using an f-string (modern and recommended):
Your name is Alex

--- Numeric Input ---
The input() function returns a string, so we must convert it to a number for math.
Enter your age: 30
The type of input received is: <class 'str'>
After converting to integer, the type is: <class 'int'>
In ten years, you will be 40 years old.

--- Combined input and conversion ---
Enter a number to be multiplied by two: 5
5 * 2 = 10

```

## Points to Consider

- **`ValueError` Risk**: If you run this script and enter text (e.g., "abc") when asked for a number, the `int()` function will fail and the program will crash with a `ValueError`. This is because "abc" cannot be converted to an integer.
- **Robust Solution**: The correct way to handle potential user errors is with `try-except` blocks, which is an error-handling mechanism. This is a more advanced topic and is covered in detail in `sample_18_exception_handling.py`.
