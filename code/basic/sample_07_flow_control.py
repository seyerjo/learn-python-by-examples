# MAIN CODE

"""Demonstrate basic flow control in Python using if-elif-else statements.

Compares two integers entered by the user and shows which is greater.
"""


def main():
    """Main function to demonstrate flow control with if-elif-else."""
    # Get two integers from user
    num_1 = int(input("Enter first integer: "))
    num_2 = int(input("Enter second integer: "))

    # Compare the numbers
    if num_1 > num_2:
        print("The first number is greater than the second.", end='\n\n')
    elif num_1 < num_2:
        print("The second number is greater than the first.", end='\n\n')
    else:
        print("The two numbers are the same.", end='\n\n')


if __name__ == "__main__":
    main()
