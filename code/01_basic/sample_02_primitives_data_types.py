"""Demonstrates Python's core scalar and collection types using type()."""


def main():
    """Creates variables of ten built-in types and prints each object's type."""
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

    print(type(integer_variable))
    print(type(float_variable))
    print(type(complex_variable))
    print(type(string_variable))
    print(type(list_variable))
    print(type(tuple_variable))
    print(type(dictionary_variable))
    print(type(set_variable))
    print(type(boolean_variable))
    print(type(none_variable))


if __name__ == "__main__":
    main()
