# MAIN CODE

"""Example of printing 'Hello, World!' to the console."""


def main():
    """Prints 'Hello, World!' to the console."""
    print("Hello, World!")  # Using double quotes
    print('Hello, World!')  # Using single quotes


# The `if __name__ == "__main__":` block is a standard best practice in Python.
# It ensures that the `main()` function is called only when the script is
# executed directly (not when it is imported as a module into another script).
# This makes your code more reusable and organized.
if __name__ == "__main__":
    main()
