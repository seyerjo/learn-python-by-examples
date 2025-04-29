# MAIN CODE

"""Demonstrate Python fundamentals: inputs, variables and strings.

Shows variable naming rules, dynamic typing, string operations
and input handling with proper Python conventions.
"""

import keyword


def main():
    """Main function demonstrating Python variable and string basics."""
    # FUNDAMENTALS

    # Best practices for variable names in Python:
    #   . The name may not begin with a number
    #   . The use of hyphens '-' is not allowed.
    #   . Spaces are not allowed.
    #   . The use of special characters is not allowed.
    #   . The use of reserved words is not allowed.

    # Invalid examples:
    #   2variable = 10
    #   var-iable = 10
    #   var iable = 10
    #   varia$ble = 10
    #   print = 10

    # Valid variable names examples
    # variable = 1
    # variable_two = 2.50
    # variable_three = "string"

    # Show Python reserved keywords
    print("Python reserved words:", keyword.kwlist, end='\n\n')

    # Dynamic typing demonstration
    variable_x = 1  # Integer
    variable_y = 3.75  # Float
    variable_z = "characters string"  # String
    print(variable_x, variable_y, variable_z)
    print(type(variable_x), type(variable_y), type(variable_z), end='\n\n')

    variable_x = "new string"  # Now string
    variable_y = 8  # Now integer
    variable_z = 4.25  # Now float
    print(variable_x, variable_y, variable_z)
    print(type(variable_x), type(variable_y), type(variable_z), end='\n\n')

    # Input and string concatenation example
    name = input("What's your name?: ")
    greeting = f"Hi {name}, my best regards."
    print(greeting, end='\n\n')

    # String length example using f-string
    print(
        f"Did you know that the length of this greeting is {len(greeting)} characters?"
    )


if __name__ == "__main__":
    main()
