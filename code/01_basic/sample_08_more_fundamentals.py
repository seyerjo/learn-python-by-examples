"""Demonstrates code reuse and the DRY principle by comparing user ages."""


def get_user_data(user_title):
    """Prompts for and returns the name and age for a labeled user.

    Args:
        user_title: Label identifying the user prompt (e.g., "FIRST").

    Returns:
        A (name, age) tuple entered by the user.
    """
    print(f">>> {user_title} USER <<<")
    name = input("Hi, what's your name?: ")
    print(f"Hello {name}")

    # int() raises ValueError on non-numeric input; handled safely in sample_18.
    age = int(input("And how old are you?: "))
    print("Thank you very much for the information!\n")
    return name, age


def main():
    """Collects data for two users via a reusable helper and compares ages."""
    name_first, age_first = get_user_data("FIRST")
    name_second, age_second = get_user_data("SECOND")

    print("--- Comparison Result ---")
    if age_first > age_second:
        print(f"{name_first}, you are older than {name_second}.\n")
    elif age_first < age_second:
        print(f"{name_first}, you are younger than {name_second}.\n")
    else:
        print(f"{name_first}, you are the same age as {name_second}.\n")


if __name__ == "__main__":
    main()
