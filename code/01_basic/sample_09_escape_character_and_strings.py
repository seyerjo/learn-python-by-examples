r"""Demonstrates escape sequences (\n, \t, \\, quotes) and raw strings in Python."""


def demonstrate_newline():
    r"""Demonstrates the newline escape sequence `\n`."""
    print("--- Newline Character (\\n) ---")
    print("This string will be split across...\n...two separate lines.")
    print()


def demonstrate_tab():
    r"""Demonstrates the horizontal tab escape sequence `\t`."""
    print("--- Tab Character (\\t) ---")
    print("You can create columns:\nCol1\tCol2\tCol3")
    print("A\tB\tC")
    print()


def demonstrate_backslash():
    r"""Demonstrates escaping literal backslashes with `\\`."""
    print("--- Backslash Character (\\\\) ---")
    print("This is a single backslash: \\")
    print("Useful for Windows paths: C:\\Users\\Name")
    print()


def demonstrate_raw_strings():
    r"""Demonstrates raw strings (`r"..."`) that treat backslashes literally."""
    print('--- Raw Strings (r"...") ---')
    # Raw strings avoid double-escaping in paths and regular expressions.
    windows_path = r"C:\Users\Name\Documents"
    print(f"Raw string path: {windows_path}")
    print()


def demonstrate_quotes():
    r"""Demonstrates escaping quotes or alternating quote styles."""
    print("--- Escaping Quotes (\\' and \\\") ---")
    print("She said, \"It's a beautiful day!\"")  # fmt: skip
    print('He replied, "Indeed it is."')
    print()


def demonstrate_interactive_example():
    """Combines user input with newline, tab, and escaped-quote formatting."""
    print("--- Interactive Example ---")
    first_name = input("What's your first name?: ")
    last_name = input("What's your last name?: ")
    print(f"\nYour name is:\n\t\"{first_name} {last_name}\"")  # fmt: skip
    print()


def main():
    """Runs all escape sequence and raw string demonstrations."""
    demonstrate_newline()
    demonstrate_tab()
    demonstrate_backslash()
    demonstrate_raw_strings()
    demonstrate_quotes()
    demonstrate_interactive_example()


if __name__ == "__main__":
    main()
