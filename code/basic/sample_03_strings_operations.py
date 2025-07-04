# MAIN CODE

"""Example demonstrating various string operations in Python."""


def main():
    """Main function to demonstrate string operations."""
    # Variables
    first_string = "123"
    second_string = "456"
    hip_string = "Hip"
    hurra_string = "Hurra"
    large_string = """This is a large string
    that spans multiple lines
    and contains various characters."""
    world_string = "World"

    # Displaying string content.
    print(first_string)  # Output: 123
    print()  # Print a blank line for separation

    # Displaying string content in triplicate.
    print(first_string * 3)  # Output: 123123123
    print()

    # Concatenated strings.
    print(first_string + second_string)  # Output: 123456
    print()

    # Strings duplicate and concatenation.
    print(((hip_string + " ") * 2) + hurra_string)  # Output: Hip Hip Hurra
    print()

    # Using f-strings for concatenation.
    print(f'{((hip_string + " ") * 2)}{hurra_string}')  # Output: Hip Hip Hurra
    print()

    # String length.
    print(len(large_string))  # Output: length of large_string
    print()

    # Selecting characters from a string.
    print(world_string[0])  # Output: W
    print(world_string[1])  # Output: o
    print(world_string[2])  # Output: r
    print(world_string[3])  # Output: l
    print(world_string[4])  # Output: d
    print()

    # Slicing the string.
    print(world_string[2:])  # Output: rld
    print()
    print(world_string[:3])  # Output: Wor
    print()
    print(world_string[:-1])  # Output: Worl
    print()
    print(world_string[::2])  # Output: Wrd
    print()

    # Example of string concatenation using the '+' operator.
    # Output: I am a citizen of the World
    print("I am a citizen of the " + world_string)
    print()

    # Example of string formatting using f-strings.

    # f-strings provide a modern and readable way to embed
    # expressions inside string literals.

    # The syntax f"{}" is used for string interpolation, where {}
    # is replaced with the value of the variable inside the brackets.

    # Output: I am a citizen of the World
    print(f"I am a citizen of the {world_string}")
    print()

    # Example of string repetition and concatenation using f-strings.
    # Output: repeated string
    repeated_string = f"I am a citizen of the {world_string}, " * 2
    print(repeated_string)
    print()


if __name__ == "__main__":
    main()
