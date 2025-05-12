# Code Style Guide: Learn Python by Examples

This document describes the code style standards and conventions that should be followed when contributing to the "Learn Python by Examples" project. Adhering to these guidelines helps maintain consistency, readability, and quality of code and documentation throughout the repository.

## General Principles

The main style guide for Python code is **PEP 8**. This document complements PEP 8 with specific guidelines for this project.

-   **Readability:** Code should be easy to read and understand for beginners. Avoid overly complex language tricks or constructs if a simpler alternative is possible.

-   **Consistency:** Maintain a consistent style with existing code in the project.

-   **Clarity:** The purpose of the code should be obvious. Use descriptive names for variables, functions, and classes.

-   **Simplicity:** Prioritize simple and straightforward solutions.

## Detailed Coding Standards (Based on PEP 8)

-   **Indentation:** Use 4 spaces per indentation level. Do not use tabs!

-   **Line Length:** Limit lines to a maximum of 79 characters for code and 72 for comments and docstrings.

-   **Blank Lines:**

    -   Surround top-level functions and classes with two blank lines.

    -   Surround method definitions within a class with a single blank line.

    -   Use blank lines sparingly to separate logical sections within a function or method.

-   **Whitespace:**

    -   Avoid superfluous whitespace immediately inside parentheses, brackets, or braces.

    -   Avoid superfluous whitespace immediately before a comma, semicolon, or colon.

    -   Use a single space around assignment (`=`), comparison (`==`, `<`, `>`, `!=`, etc.), and arithmetic (`+`, `-`, `*`, `/`, etc.) operators when used in expressions.

    -   Do not use spaces around the `=` sign when used to indicate a keyword argument or a default parameter value.

-   **Comments:**

    -   Comments should be complete, concise, and kept up-to-date with the code.

    -   Inline comments should be separated from the code by at least two spaces.

    -   Start comments with a space (unless they start at the beginning of the line).

-   **Docstrings:**

    -   Write docstrings for all public modules, classes, functions, and methods.

    -   Use triple double quotes (`"""Docstring here"""`).

    -   For single-line docstrings, the opening and closing quotes should be on the same line.

    -   For multi-line docstrings, the summary line should be on its own line, followed by a blank line, and then the rest of the description.

## Naming Conventions

Follow the naming conventions recommended by PEP 8:

-   **Modules:** Short, all lowercase names. Underscores can be used if it improves readability (e.g., `utility_module`).

-   **Packages:** Short, all lowercase names. Do not use underscores (e.g., `mypackage`).

-   **Classes:** PascalCase convention (e.g., `MyClass`).

-   **Functions:** snake_case convention, all lowercase with underscores to separate words (e.g., `my_function`).

-   **Variables:** snake_case convention, all lowercase with underscores to separate words (e.g., `my_variable`).

-   **Constants:** All uppercase with underscores to separate words (e.g., `MY_CONSTANT`).

-   **Method Arguments:** The first argument of an instance method should be `self`. The first argument of a class method should be `cls`.

## Recommended Patterns

-   Use list, dictionary, and set comprehensions where appropriate to create collections concisely.

-   Use context managers (`with`) for resources that need to be closed (files, network connections, etc.).

-   Use f-strings for string formatting.

-   Use iterators and generators for working with large datasets efficiently.
