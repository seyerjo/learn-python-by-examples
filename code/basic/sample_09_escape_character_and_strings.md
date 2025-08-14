# Escape Characters in Python Strings

This example demonstrates how to use escape characters to include special characters within a string, such as newlines, tabs, backslashes, and quotes.

## Code

```python
# MAIN CODE

"""
Examples of working with strings and escape characters in Python.

Demonstrates newlines, tabs, backslashes, and quote escaping.
"""


def demonstrate_newline():
    """Demonstrates the newline character `\n`."""
    print("--- Newline Character (\\n) ---")
    print("This string will be split across...\n...two separate lines.")
    print()


def demonstrate_tab():
    """Demonstrates the tab character `\t`."""
    print("--- Tab Character (\\t) ---")
    print("You can create columns:\nCol1\tCol2\tCol3")
    print("A\tB\tC")
    print()


def demonstrate_backslash():
    """Demonstrates how to escape the backslash character `\\`."""
    print("--- Backslash Character (\\\\) ---")
    # To print a single backslash, you need to escape it with another one.
    print("This is a single backslash: \\")
    print("Useful for file paths in strings: C:\\Users\\Name")
    print()


def demonstrate_quotes():
    """Demonstrates how to include quotes inside a string."""
    print("--- Escaping Quotes (\\' and \\\") ---")
    # You can escape quotes to include them in a string literal.
    print("She said, \"It's a beautiful day!\"")
    # Alternatively, use the other type of quote for the string itself.
    print('He replied, "Indeed it is."')
    print()


def demonstrate_interactive_example():
    """Combines user input with escape characters."""
    print("--- Interactive Example ---")
    first_name = input("What's your first name?: ")
    last_name = input("What's your last name?: ")
    # Using \n for newlines and \" to wrap the name in quotes.
    print(f"\nYour name is:\n\t\"{first_name} {last_name}\"")
    print()


def main():
    """Main function to demonstrate all escape character examples."""
    demonstrate_newline()
    demonstrate_tab()
    demonstrate_backslash()
    demonstrate_quotes()
    demonstrate_interactive_example()


if __name__ == "__main__":
    main()
```

## Explanation

Escape characters, which begin with a backslash (`\`), are used to signal that the character following it has a special meaning. The most common are:

1.  **`\n` (Newline)**: Inserts a line break, moving the cursor to the beginning of the next line.
2.  **`\t` (Tab)**: Inserts a horizontal tab, which is useful for aligning text in columns.
3.  **`\\` (Backslash)**: Since the backslash is the escape character itself, you need to use two of them (`\\`) to print a single, literal backslash.
4.  **`\"` and `\'` (Quotes)**: These allow you to include double or single quotes inside a string literal that is defined by the same type of quote. An easier alternative is often to just use the other quote type to define the string (e.g., use single quotes for the string if it contains double quotes).

## Expected Output

The output will be a series of demonstrations, with the last one being interactive. An example session:

```
--- Newline Character (\n) ---
This string will be split across...
...two separate lines.

--- Tab Character (\t) ---
You can create columns:
Col1	Col2	Col3
A	B	C

--- Backslash Character (\\) ---
This is a single backslash: \
Useful for file paths in strings: C:\Users\Name

--- Escaping Quotes (\' and \") ---
She said, "It's a beautiful day!"
He replied, "Indeed it is."

--- Interactive Example ---
What's your first name?: John
What's your last name?: Doe

Your name is:
	"John Doe"

```

## Points to Consider

-   **Raw Strings**: For strings that contain many backslashes, like Windows file paths, it can be cumbersome to escape each one. Python offers **raw strings** for this. By prefixing a string with an `r`, you tell Python to treat backslashes as literal characters.
    -   Example: `path = r"C:\Users\New_User\Documents"` is easier to write and read than `path = "C:\\Users\\New_User\\Documents"`
