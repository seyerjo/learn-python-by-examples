# MAIN CODE

"""Demonstrate user input handling and comparison with multiple users.

Collects names and ages from two users and compares their ages.
"""


def main():
    """Main function to demonstrate multi-user input and comparison."""
    # Get first user's information
    print(">>> FIRST USER <<<")
    name_first = input("Hi, what's your name?: ")
    print(f"Hello {name_first}")
    age_first = int(input("And how old are you?: "))
    print("Thank you very much for the information!", end='\n\n')

    # Get second user's information
    print(">>> SECOND USER <<<")
    name_second = input("Hi to you too, what's your name?: ")
    print(f"Hello {name_second}")
    age_second = int(input("And how old are you?: "))
    print("Thank you very much for the information!", end='\n\n')

    # Compare ages and show result
    if age_first > age_second:
        print(f"{name_first}, you are older than {name_second}", end='\n\n')
    elif age_first < age_second:
        print(f"{name_first}, you are younger than {name_second}", end='\n\n')
    else:
        print(f"{name_first}, you are the same age as {name_second}", end='\n\n')


if __name__ == "__main__":
    main()
