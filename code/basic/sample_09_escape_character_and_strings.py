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
