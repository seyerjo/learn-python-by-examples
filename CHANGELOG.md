# Changelog

All notable changes to this project will be documented in this file.

## [1.1.0] - Quality and Pedagogy Refactor

### Changed

-   Systematic refactoring and improvement of the first 11 code samples (00 to 10) to enhance code quality, modularity, and pedagogical value.
-   Restructured monolithic scripts into multiple, single-purpose functions to improve clarity and demonstrate best practices.
-   Enhanced `print()` statements to be more descriptive, making the program flow easier for beginners to follow.
-   Added pedagogical comments to warn about common errors (e.g., `ValueError` on `int(input())`) and to explain specific parameters (e.g., `sep=""`).

### Added

-   Introduced and explained the DRY (Don't Repeat Yourself) principle in `sample_08`.
-   Added explanatory notes on key concepts directly within the documentation, such as "raw strings", mutability, and type hinting previews.

### Fixed

-   Corrected all identified inconsistencies between code examples (`.py`) and their corresponding documentation (`.md`), ensuring perfect synchronization.

## [1.0.4]

### Added

-   New intermediate example `sample_18_exception_handling.py` and its documentation (`sample_18_exception_handling.md`) demonstrating robust input validation using `try-except` blocks.

### Changed

-   Renumbered advanced examples in `code/advanced/` from `sample_18` to `sample_22` to `sample_19` to `sample_23` respectively, to accommodate new `intermediate` examples and maintain sequential order.
-   Added type hints to variables in all advanced examples (`sample_19` through `sample_23`) to ensure full compliance with code style guidelines.
-   Refactored code in `sample_03_strings_operations.py`, `sample_06_inputs_variables_and_strings.py`, and `sample_20_solution_approximation_algorithm.py` to fix lines exceeding 79 characters.
-   Restructured `sample_01_hello_world.py` to include a `main` function and an `if __name__ == "__main__":` guard for better code organization.
-   Added detailed explanation of `if __name__ == "__main__":` in `sample_01_hello_world.py` and its corresponding documentation (`sample_01_hello_world.md`).

## [1.0.3]

### Added

-   New advanced example `sample_22_robust_input_validation.py` to teach robust user input handling.
-   New advanced example `sample_23_type_hinting.py` to explain the use and benefits of Type Hinting (PEP 484).
-   Cross-reference comments in advanced examples (`19` to `22`) pointing to the new Type Hinting explanation.

### Changed

-   Improved advanced examples (`19`, `20`, `21`) by adding robust input validation and Type Hinting.
-   Improved intermediate example `sample_16_recursive_functions.py` to correctly handle the `n=0` edge case for factorials.
-   Updated documentation for all modified examples (`.md` files) to ensure code and explanations are synchronized and accurate.

## [1.0.2]

### Added

-   Detailed documentation for each code example.

### Changed

-   No changes in this version.

### Fixed

-   Minor corrections in documentation for clarity.

## [1.0.1]

### Added

-   New Python code examples for basic, intermediate, and advanced levels.

### Changed

-   Updated `README.md` to include a more comprehensive list of examples.
-   Refined the project structure to improve navigation.

### Fixed

-   Minor corrections in documentation for clarity.

## [1.0.0] - Initial Release

### Added

-   Initial project structure and documentation.
