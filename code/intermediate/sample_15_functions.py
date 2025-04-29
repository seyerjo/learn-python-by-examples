# MAIN CODE

"""Demonstrate function definitions and usage in Python.

Shows basic function syntax, docstrings, parameters and return values.
"""


def sum_numbers(a, b):
    """Return the sum of two numbers.

    Args:
        a (int): First number
        b (int): Second number

    Returns:
        int: Sum of a and b
    """
    return a + b


def full_name(name, last_name, inverse=False):
    """Combine first and last name, with optional reverse order.

    Args:
        name (str): First name
        last_name (str): Last name
        inverse (bool, optional): Reverse name order if True. Defaults to False.

    Returns:
        str: Combined name string
    """
    if inverse:
        return f"{last_name} {name}"
    return f"{name} {last_name}"


def main():
    """Main function demonstrating function usage."""
    # Demonstrate sum_numbers function
    print(sum_numbers(3, 2), end='\n\n')

    # Demonstrate full_name function variations
    print(full_name("Michael", "Smith"), end='\n\n')
    print(full_name("Michael", "Smith", inverse=True), end='\n\n')
    print(full_name(last_name="Smith", name="Michael"), end='\n\n')


if __name__ == "__main__":
    main()
