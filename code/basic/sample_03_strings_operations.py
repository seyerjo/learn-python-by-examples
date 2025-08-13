# MAIN CODE

"""
Example demonstrating various string operations in Python.

A note on functions:
This code is organized into 'functions' (e.g., `def demonstrate_slicing():`).
A function is a reusable block of code that performs a specific task.
Using functions helps keep our code clean, organized, and easy to read.
We will cover functions in much more detail in a later example (sample_15_functions.py).
"""


def demonstrate_concatenation_and_repetition():
    """Demonstrates string concatenation and repetition."""
    print("--- Concatenation and Repetition ---")
    first_string = "123"
    second_string = "456"
    hip_string = "Hip"
    hurra_string = "Hurra"

    # Simple concatenation using the '+' operator
    concatenated = first_string + second_string
    print("'", first_string, "' + '", second_string, "' = '",
          concatenated, "'", sep="")
    # The sep="" argument prevents print() from adding extra spaces between items.

    # Repetition using the '*' operator
    triplicate = first_string * 3
    print("'", first_string, "' * 3 = '", triplicate, "'", sep="")

    # Combined repetition and concatenation
    cheer = ((hip_string + " ") * 2) + hurra_string
    print("Cheer example:", cheer)
    print()


def demonstrate_length_and_indexing():
    """Demonstrates calculating length and accessing characters by index."""
    print("--- Length and Indexing ---")
    large_string = """This is a large string
    that spans multiple lines
    and contains various characters."""
    world_string = "World"

    # Get the total number of characters in a string
    print("Length of the large string is:", len(large_string))

    # Access individual characters using zero-based indexing
    print("First character of 'World':", world_string[0])
    print("Third character of 'World':", world_string[2])
    print("Last character of 'World':", world_string[-1])
    print()


def demonstrate_slicing():
    """Demonstrates extracting substrings using slicing."""
    print("--- String Slicing ---")
    world_string = "World"

    # Slice from index 2 to the end
    print("Slice [2:]:", world_string[2:])

    # Slice from the beginning to index 3 (exclusive)
    print("Slice [:3]:", world_string[:3])

    # Slice from the beginning to the second-to-last character
    print("Slice [:-1]:", world_string[:-1])

    # Slice with a step (every second character)
    print("Slice [::2]:", world_string[::2])
    print()


def demonstrate_f_strings():
    """Demonstrates the use of f-strings for modern formatting."""
    print("--- F-String Formatting (Modern Method) ---")
    world_string = "World"

    # Embedding variables directly into a string
    sentence = f"I am a citizen of the {world_string}"
    print("f-string sentence:", sentence)

    # Repetition with f-strings
    repeated = f"I am a citizen of the {world_string}, " * 2
    print("f-string repeated:", repeated)
    print()


def main():
    """Main function to demonstrate all string operations."""
    demonstrate_concatenation_and_repetition()
    demonstrate_length_and_indexing()
    demonstrate_slicing()
    demonstrate_f_strings()


if __name__ == "__main__":
    main()
