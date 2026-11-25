# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added
- Added local repository visual assets (`.github/assets/banner.png` and `.github/assets/avatar.png`) for the root `README.md`.
- Added the pedagogical progression boundary matrix (`01_basic`, `02_intermediate`, `03_advanced`) in `docs/02_engineering_guidelines.md`.
- Added a pedagogical forward-reference note for PEP 484 type hints in `code/02_intermediate/sample_15_functions.py`.

### Changed
- Bumped the minimum supported Python version from `3.7+` to `3.10+` across `README.md`, `docs/01_project_blueprint.md`, and `docs/02_engineering_guidelines.md`, and modernized type annotations in `sample_22` and `sample_23` to PEP 585/604 syntax.
- Audited and formatted all 24 baseline scripts (`sample_00`–`sample_23`) with `Black` (88-character line length), added `#!/usr/bin/env python3` and `sys.exit(0)` across `code/03_advanced/`, and resynchronized all twin `.md` documentation files.
- Redesigned `README.md` with a centered showcase header, strict 1:1 section navigation, open-by-default color-badged example tables and project structure, Mermaid diagram under `## Architecture`, and a borderless Author Card with contact badges, updated tagline (`"Engineering for the future."`), and Star callout.
- Aligned formatting and typing documentation across `README.md` and `docs/02_engineering_guidelines.md` to `Black` (88-character line length), `Prettier`, and progressive adoption of `try-except` and PEP 484 type hints.
- Scoped public `/docs` references in `README.md` and `docs/02_engineering_guidelines.md` to `01_project_blueprint.md` and `02_engineering_guidelines.md`.

### Fixed
- Moved module-level `try-except` execution in `sample_00_comments_types.py` inside `main()` to prevent side effects on import, added missing `Args:`/`Returns:` Google docstrings in `sample_17` and `sample_23`, and resolved pre-existing `.py`/`.md` code block drifts.

### Removed
- Removed obsolete archived planning, draft code, and legacy documentation files.
- Excluded the internal project log from the public repository.

## [1.2.5] - 2026-08-25

### Changed
- Consolidated project documentation into a streamlined 4-anchor architecture (`docs/01_project_blueprint.md`, `docs/02_engineering_guidelines.md`, `docs/03_project_log.md`, and `CHANGELOG.md`).
- Renamed code subdirectories to `01_basic`, `02_intermediate`, and `03_advanced` to enforce natural pedagogical sorting in file trees and synchronized all documentation cross-references.
- Updated root documentation (`README.md`) to align with project workflows.
- Archived legacy planning and documentation files.
- Sanitized internal development terminology across all public repository documentation.

## [1.2.0] - Major Refactoring and Synchronization

### Changed
- **Project-Wide Refactoring (Samples 11-23):** Performed a comprehensive, sample-by-sample review and refactoring of the existing codebase.
- **Code Quality and Modularity:** Refactored monolithic scripts into smaller, single-purpose functions to improve clarity, reusability, and demonstrate best practices (e.g., `sample_19`, `sample_20`, `sample_21`).
- **Pedagogical Enhancements:** Systematically improved comments, docstrings, and console outputs across all samples to make the code more educational and easier to follow for beginners.
- **Robustness:** Introduced and standardized robust input validation and error handling patterns where appropriate (e.g., `sample_16`, `sample_22`).
- **Consistency:** Improved alignment with project code style and naming conventions across refactored samples.

### Fixed
- **Documentation Synchronization:** Corrected inconsistencies between code examples (`.py`) and their corresponding documentation (`.md`), updating twin guides to match the refactored code.

## [1.1.0] - Quality and Pedagogy Refactor

### Changed
- Systematic refactoring and improvement of the first 11 code samples (`00` to `10`) to enhance code quality, modularity, and pedagogical value.
- Restructured monolithic scripts into multiple, single-purpose functions to improve clarity and demonstrate best practices.
- Enhanced `print()` statements to be more descriptive, making the program flow easier for beginners to follow.
- Added pedagogical comments to warn about common errors (e.g., `ValueError` on `int(input())`) and to explain specific parameters (e.g., `sep=""`).

### Added
- Introduced and explained the DRY (Don't Repeat Yourself) principle in `sample_08`.
- Added explanatory notes on key concepts directly within the documentation, such as raw strings, mutability, and type hinting previews.

### Fixed
- Corrected inconsistencies between code examples (`.py`) and their corresponding documentation (`.md`).

## [1.0.4]

### Added
- New intermediate example `sample_18_exception_handling.py` and its documentation (`sample_18_exception_handling.md`) demonstrating robust input validation using `try-except` blocks.

### Changed
- Renumbered advanced examples from `sample_18`–`sample_22` to `sample_19`–`sample_23` to accommodate new intermediate examples and maintain sequential order.
- Added PEP 484 type hints across advanced examples (`sample_19` through `sample_23`).
- Refactored long lines in `sample_03_strings_operations.py`, `sample_06` (later `sample_06_fundamentals.py`), and `sample_20_solution_approximation_algorithm.py`.
- Restructured `sample_01_hello_world.py` to include a `main` function and an `if __name__ == "__main__":` guard for better code organization.
- Added a detailed explanation of `if __name__ == "__main__":` in `sample_01_hello_world.py` and its corresponding documentation (`sample_01_hello_world.md`).

## [1.0.3]

### Added
- New advanced example `sample_22_robust_input_validation.py` to teach robust user input handling.
- New advanced example `sample_23_type_hinting.py` to explain the use and benefits of Type Hinting (PEP 484).
- Cross-reference comments in advanced examples (`19` to `22`) pointing to the Type Hinting explanation.

### Changed
- Improved advanced examples (`19`, `20`, `21`) by adding robust input validation and Type Hinting.
- Improved intermediate example `sample_16_recursive_functions.py` to correctly handle the `n=0` edge case for factorials.
- Updated documentation for all modified examples (`.md` files) to ensure code and explanations remain synchronized.

## [1.0.2]

### Added
- Detailed documentation for each code example.

### Fixed
- Minor corrections in documentation for clarity.

## [1.0.1]

### Added
- New Python code examples for basic, intermediate, and advanced levels.

### Changed
- Updated `README.md` to include a more comprehensive list of examples.
- Refined the project structure to improve navigation.

### Fixed
- Minor corrections in documentation for clarity.

## [1.0.0] - Initial Release

### Added
- Initial project structure and documentation.
