""" SOLUTION APPROXIMATION algorithm

    The approximation algorithm is a method for finding an approximate solution to a
    problem. This is achieved by using a series of iterative steps that are applied
    until a satisfactory solution is obtained.
    
    The basic steps followed to find the approximation to the solution are: 

    1. Define the problem.
    2. Establish the parameters of the solution.
    3. Generate an initial solution.
    4. Evaluate the initial solution.
    5. Generate a new solution.
    6. Re-evaluate the new solution.
    7. Compare the initial solution with the new solution.
    8. Repeat steps 5 to 7 until the approximate solution is found.
    
    This code is an approximation algorithm that tries to find the square root of
    an integer number given by the user.

    First, the user chooses a number and a constant "epsilon" is declared with a
    value of 0.01. This constant will control the level of accuracy of the algorithm.
    Then, a variable "response" is initialized at 0.0 which will then be incremented
    with the step of the algorithm.

    A while loop is initiated to calculate the square root of the number. The loop
    compares the square root of the response variable with the target number. If the
    difference is less than the epsilon value, the algorithm assumes it has found the
    answer. If the difference is greater, the loop continues and the response variable
    is incremented with the defined step.

    Finally, the algorithm checks if the square root of the response is within the epsilon
    margin and, if so, prints the response on the screen. If not, it prints a message
    indicating that the square root has not been found.

"""


def main():
    """Main function demonstrating solution approximation algorithm."""
    # Set precision level (epsilon) and step size
    epsilon = 0.01  # Controls accuracy of approximation
    step = epsilon**2  # Smaller step for finer approximation

    # Get target number from user
    target = int(input("Enter an integer number: "))
    print()  # Blank line

    # Initialize guess and perform approximation
    guess = 0.0
    while abs(guess**2 - target) >= epsilon and guess <= target:
        print(
            f"Current error: {abs(guess**2 - target):.4f}, Guess: {guess:.4f}")
        guess += step

    print()  # Blank line

    # Check if approximation was successful
    if abs(guess**2 - target) < epsilon:
        print(f"Approximate square root of {target} is {guess:.4f}")
    else:
        print(f"Could not find square root of {target} within given precision")


if __name__ == "__main__":
    main()
