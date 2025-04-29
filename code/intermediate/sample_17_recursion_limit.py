# MAIN CODE

"""Demonstrate Python's recursion limit and how to modify it.

Shows the default recursion limit, how to check it, and how to change it,
with warnings about modifying this limit.
"""

# Import sys module to access system-specific parameters and functions
# including getrecursionlimit() and setrecursionlimit()
import sys


def main():
    """Main function to demonstrate recursion limit operations."""
    # Show default recursion limit
    print(f"Default recursion limit: {sys.getrecursionlimit()}", end='\n\n')

    # Demonstrate changing the limit
    sys.setrecursionlimit(999)
    print(f"New recursion limit set to: {sys.getrecursionlimit()}", end='\n\n')

    # Reset to default
    sys.setrecursionlimit(1000)
    print(
        f"Recursion limit reset to default: {sys.getrecursionlimit()}", end='\n\n')

    # Warning about changing recursion limit
    print("Warning: Modifying recursion limit can lead to stack overflow!")
    print("Consider using iterative solutions for deep recursion cases.", end='\n\n')


if __name__ == "__main__":
    main()
