# Code Reusability and the DRY Principle

This example builds on previous concepts by creating a small, practical application: it gathers information from two different users and then compares their ages.

The key lesson in this example is the introduction of a reusable function to avoid duplicating code. This adheres to a fundamental programming principle known as **DRY (Don't Repeat Yourself)**.

## Code

```python
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
```

## Explanation

1.  **The DRY Principle**: Notice that the code for asking for a user's name and age is identical for both users. Instead of writing this code twice, we "keep it dry" by creating a single function, `get_user_data()`, that contains this logic.

2.  **Reusable Function (`get_user_data`)**:

    -   This function takes one argument, `user_title`, so we can label the output (e.g., "FIRST USER", "SECOND USER").
    -   It performs all the steps to get the name and age.
    -   It returns both the `name` and `age` as a tuple, which allows the `main` function to receive and store them in separate variables.

3.  **Main Logic (`main`)**:
    -   The `main` function is now much cleaner and easier to read.
    -   It calls `get_user_data()` twice, once for each user, and unpacks the returned tuple into corresponding variables (e.g., `name_first, age_first`).
    -   Finally, it performs the age comparison using the collected data.

## Expected Output

The program is interactive. An example session would look like this:

```
>>> FIRST USER <<<
Hi, what's your name?: Alice
Hello Alice
And how old are you?: 30
Thank you very much for the information!

>>> SECOND USER <<<
Hi, what's your name?: Bob
Hello Bob
And how old are you?: 25
Thank you very much for the information!

--- Comparison Result ---
Alice, you are older than Bob.

```

## Points to Consider

-   **DRY (Don't Repeat Yourself)** is one of the most important principles in software development. Creating reusable functions is a primary way to achieve this, leading to cleaner, more maintainable, and less error-prone code.
-   Functions can return multiple values. In Python, this is often done by returning a tuple, which can then be easily "unpacked" into multiple variables.
-   This script is still vulnerable to a `ValueError` if non-numeric input is given for the age. The robust way to handle this is covered in `sample_18_exception_handling.py`.
