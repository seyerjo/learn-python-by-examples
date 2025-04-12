# MAIN CODE

"""Example demonstrating various primitive data types in Python."""


def main():
    """Main function."""
    # Variables of different data types.
    integer_variable = 1
    float_variable = 3.14
    complex_variable = 1 + 2j
    string_variable = "Hello, Coder!"
    list_variable = [1, 2, 3]
    tuple_variable = (4.0, 5.5, 6.9)
    dictionary_variable = {"key": "value"}
    set_variable = {7, 8, 9}
    boolean_variable = False
    none_variable = None

    # Using the 'type' function to determine data types.
    print(type(integer_variable))       # int
    print(type(float_variable))         # float
    print(type(complex_variable))       # complex
    print(type(string_variable))        # str
    print(type(list_variable))          # list
    print(type(tuple_variable))         # tuple
    print(type(dictionary_variable))    # dictionary
    print(type(set_variable))           # set
    print(type(boolean_variable))       # bool
    print(type(none_variable))          # NoneType


if __name__ == "__main__":
    main()
