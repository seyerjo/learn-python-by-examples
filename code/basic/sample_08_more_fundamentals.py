# MAIN CODE

"""
Demonstrates user input handling for multiple users by creating a reusable
function, following the DRY (Don't Repeat Yourself) principle.
"""


def get_user_data(user_title):
    """
    Prompts for and returns the name and age for a given user.

    This function encapsulates the logic for getting user data, allowing it
    to be reused instead of duplicated.

    Args:
        user_title (str): A string to identify the user (e.g., "FIRST").

    Returns:
        tuple: A tuple containing the user's name (str) and age (int).
    """
    print(f">>> {user_title} USER <<<")
    name = input("Hi, what's your name?: ")
    print(f"Hello {name}")

    # IMPORTANT: The int() function will cause a ValueError if you enter
    # non-numeric text. A robust solution is covered in sample_18.
    age = int(input("And how old are you?: "))
    print("Thank you very much for the information!\n")
    return name, age


def main():
    """Main function to get data for two users and compare their ages."""
    # Get first user's information by calling the reusable function
    name_first, age_first = get_user_data("FIRST")

    # Get second user's information by calling the same function again
    name_second, age_second = get_user_data("SECOND")

    # Compare ages and show result
    print("--- Comparison Result ---")
    if age_first > age_second:
        print(f"{name_first}, you are older than {name_second}.\n")
    elif age_first < age_second:
        print(f"{name_first}, you are younger than {name_second}.\n")
    else:
        print(f"{name_first}, you are the same age as {name_second}.\n")


if __name__ == "__main__":
    main()
