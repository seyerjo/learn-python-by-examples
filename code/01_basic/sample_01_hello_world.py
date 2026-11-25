"""Demonstrates printing 'Hello, World!' and the __main__ entry guard."""


def main():
    """Prints 'Hello, World!' using double and single quotes."""
    print("Hello, World!")
    print('Hello, World!')  # fmt: skip


# Run main() only when executed directly, not when imported as a module.
if __name__ == "__main__":
    main()
