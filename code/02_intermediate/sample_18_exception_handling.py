"""Demonstrates structured exception handling using try-except-else-finally."""


def safe_division():
    """Prompts for two numbers and divides them with full exception handling."""
    print("--- Safe Division Calculator ---")
    print("This program will calculate numerator / denominator.")

    try:
        numerator_str = input("Enter the numerator: ")
        numerator = float(numerator_str)

        denominator_str = input("Enter the denominator: ")
        denominator = float(denominator_str)

        result = numerator / denominator
    except ValueError:
        print("\nError: Invalid input. Please enter valid numbers.")
    except ZeroDivisionError:
        print("\nError: Cannot divide by zero.")
    else:
        print(f"\nSuccess! The result of the division is: {result:.2f}")
    finally:
        print("\n--- Calculation attempt finished. ---")


def main():
    """Runs the safe division demonstration."""
    safe_division()


if __name__ == "__main__":
    main()
