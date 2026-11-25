"""Demonstrates string joining, repetition, indexing, slicing, and f-strings."""


def demonstrate_concatenation_and_repetition():
    """Demonstrates string concatenation and repetition."""
    print("--- Concatenation and Repetition ---")
    first_string = "123"
    second_string = "456"
    hip_string = "Hip"
    hurra_string = "Hurra"

    concatenated = first_string + second_string
    # sep="" suppresses the default space that print() inserts between arguments.
    print("'", first_string, "' + '", second_string, "' = '", concatenated, "'", sep="")

    triplicate = first_string * 3
    print("'", first_string, "' * 3 = '", triplicate, "'", sep="")

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

    print("Length of the large string is:", len(large_string))
    print("First character of 'World':", world_string[0])
    print("Third character of 'World':", world_string[2])
    print("Last character of 'World':", world_string[-1])
    print()


def demonstrate_slicing():
    """Demonstrates extracting substrings using slicing."""
    print("--- String Slicing ---")
    world_string = "World"

    print("Slice [2:]:", world_string[2:])
    # Slice end index is exclusive (reads indices 0, 1, and 2).
    print("Slice [:3]:", world_string[:3])
    print("Slice [:-1]:", world_string[:-1])
    # Step of 2 takes every second character.
    print("Slice [::2]:", world_string[::2])
    print()


def demonstrate_f_strings():
    """Demonstrates f-strings for readable string interpolation."""
    print("--- F-String Formatting (Modern Method) ---")
    world_string = "World"

    sentence = f"I am a citizen of the {world_string}"
    print("f-string sentence:", sentence)

    repeated = f"I am a citizen of the {world_string}, " * 2
    print("f-string repeated:", repeated)
    print()


def main():
    """Runs all string operation demonstrations."""
    demonstrate_concatenation_and_repetition()
    demonstrate_length_and_indexing()
    demonstrate_slicing()
    demonstrate_f_strings()


if __name__ == "__main__":
    main()
