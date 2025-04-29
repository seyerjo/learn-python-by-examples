"""Examples of working with strings and escape characters in Python.

Demonstrates newlines, tabs, backslashes, and quote escaping.
"""


def main():
    """Main function demonstrating string escape characters."""
    print("--------\nEXAMPLES\n--------", end='\n\n')

    # 1. Multi-line text with single print
    print("Line 1.\nLine 2.\nLine 3.\nLine 4.", end='\n\n')

    # 2. Tabular data with tabs
    print("A\tB\tC\tD\nE\tF\tG\tH\nI\tJ\tK\tL\nM\tN\tO\tP", end='\n\n')

    # 3. Displaying special characters
    print("This is the slash character: /.\nThis is the backslash character: \\.", end='\n\n')

    # 4. Escaping quotes
    print("\"Y\" isn't a number.", end='\n\n')

    # 5. Combined example with user input
    first_name = input("What's your first name: ")
    last_name = input("What's your last name: ")
    print(f"\nYour name is:\n\"{first_name} {last_name}\"\n")


if __name__ == "__main__":
    main()
