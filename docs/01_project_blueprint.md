# Project Blueprint: Learn Python by Examples

## Vision & Objectives

### Central Vision
To be an essential and practical guide for anyone interested in learning Python, providing clear, robust, and well-structured code examples classified by difficulty level.

### Main Objectives
- **Comprehensive Collection:** Grow from the current 24 baseline examples (`sample_00`–`sample_23`) toward a curated collection of at least 100 Python code examples covering basic, intermediate, and advanced programming concepts.
- **Clear Classification:** Organize and categorize all code examples into well-defined difficulty tiers (`01_basic`, `02_intermediate`, `03_advanced`).
- **Granular Documentation:** Provide dedicated, synchronized markdown documentation alongside every individual code example.
- **Intuitive Architecture:** Maintain a clean, easy-to-navigate repository structure optimized for self-guided learning.
- **Educational Onboarding:** Deliver an authoritative root showcase guide (`README.md`) explaining the project layout, interactive sample index, quick-start output, and local execution instructions.

### Problem / Need Addressed
Beginning programmers and practitioners learning Python often struggle to find practical, standalone, and progressively challenging code examples that demonstrate engineering best practices, error handling, and idiomatic patterns with contextual explanations.

### General Description of the Solution
A curated repository of standalone Python code examples organized by difficulty tiers, accompanied 1:1 by twin markdown documentation for each script, demonstrating standard library capabilities, `Black`-formatted modern syntax, and progressive defensive programming patterns.

---

## Requirements

### Functional Requirements (FR)
- **FR-01:** The project must contain a collection of standalone and modular code examples written in modern Python (`3.10+`).
- **FR-02:** Code examples must be organized and classified into dedicated difficulty tiers: `01_basic`, `02_intermediate`, and `03_advanced`.
- **FR-03:** Each code example (`sample_XX_description.py`) must be accompanied by its corresponding twin documentation file (`sample_XX_description.md`).
- **FR-04:** Each documentation file must explain the code's pedagogical purpose, concepts illustrated, step-by-step workflow, and expected console output.
- **FR-05:** Users must be able to view and execute the source code of any example directly in a local Python environment.
- **FR-06:** Users must be able to access and read the documentation associated with each example alongside the code.
- **FR-07:** The repository architecture must support the addition of new examples and difficulty categories in an extensible manner.
- **FR-08:** The project must support continuous maintenance, formatting audits, and synchronization between existing examples and documentation.

### Non-Functional Requirements (NFR)
- **NFR-01 (Usability & Navigation):** The repository directory layout must be intuitive, predictable, and simple to browse across all operating systems.
- **NFR-02 (Pedagogical Clarity):** Documentation and in-code comments must be clear, concise, beginner-friendly, and written in English.
- **NFR-03 (Code Correctness & Robustness):** All provided code samples must be functional, free of syntax errors, formatted consistently (`Black`), and demonstrate progressive error handling appropriate to their tier.
- **NFR-04 (Public Showcase Availability):** The project is hosted in a public GitHub repository as a solo-authored technical showcase and open educational reference, welcoming questions and feedback via GitHub Issues.
- **NFR-05 (Zero-Friction Setup):** Local environment setup and script execution must require minimal steps and rely primarily on standard Python tooling.
- **NFR-06 (Consistent Difficulty Gradient):** The progression from `01_basic` through `02_intermediate` to `03_advanced` must follow a coherent pedagogical curve without overwhelming beginners with premature boilerplate.

---

## Product Features

### FEAT-01: Modular Collection of Python Code Examples
- **Description:** A progressive library of Python code samples covering syntax fundamentals, control flow, functions, defensive validation, algorithms, and static type hinting.
- **Associated Requirements:** FR-01, FR-02, FR-05, FR-07, NFR-03, NFR-06
- **Detailed Operation:** Users browse through categorized level folders (`/code/01_basic`, `/code/02_intermediate`, `/code/03_advanced`), pick an example, and execute it directly via CLI.
- **Edge Cases & Handling:**
  - *Invalid or Unexpected Inputs:* Introductory `01_basic` scripts (`sample_05`) highlight input risks with forward-reference notes, while `02_intermediate` (`sample_18`) and `03_advanced` (`sample_22`) enforce `try-except` validation loops.
  - *Null / Empty Values:* String and collection examples account for empty or whitespace inputs where applicable.
  - *Boundary & Extreme Values:* Algorithmic and recursive samples account for zero, negative numbers, recursion limits (`sample_17`), and numerical tolerances (`sample_19`–`sample_21`).
  - *Missing External Resources:* Upcoming File I/O and API examples handle missing paths, timeouts, and missing credentials defensively using `pathlib` and `try-except`.
- **Validation Rules:**
  - Every script must include a modular `main()` function and an `if __name__ == "__main__":` entry guard.
  - Progressive rules (PEP 484 type hints, shebang `#!/usr/bin/env python3`, explicit `sys.exit()` codes, `logging`, and `argparse`) are enforced according to the tier boundary table in `docs/02_engineering_guidelines.md`.

### FEAT-02: Synchronized Twin Documentation
- **Description:** Comprehensive markdown documentation paired 1:1 with each script (`sample_XX_description.md`) residing in the same directory.
- **Associated Requirements:** FR-03, FR-04, FR-06, FR-08, NFR-02
- **Detailed Operation:** Readers open the markdown twin to inspect the conceptual breakdown, code explanations, and expected output before or after running the Python script.
- **Edge Cases & Validation:**
  - *Documentation Drift:* Documentation must be updated synchronously whenever code logic or parameters change.
  - *Output Discrepancies:* Sample output blocks in documentation must match exact console execution output.

### FEAT-03: Structured & Predictable Repository Architecture
- **Description:** Standardized directory hierarchy and naming convention (`sample_00_description.py` / `sample_00_description.md`) enforcing consistency across all levels.
- **Associated Requirements:** FR-02, FR-05, NFR-01
- **Detailed Operation:** Tiered folder structure isolating `01_basic/`, `02_intermediate/`, and `03_advanced/` samples, `.github/assets/` for README visual assets, `/docs` for project architecture/roadmap documentation, and `/` for root entry files (`README.md`, `CHANGELOG.md`, `LICENSE`).
- **Edge Cases & Validation:**
  - All sample file and directory names must strictly use lowercase letters with underscore separators.
  - Numbering must maintain sequential two-digit zero-padding starting from zero (`sample_00_...`, `sample_01_...`, `sample_02_...`).

### FEAT-04: Progressive Error Handling & Defensive Patterns
- **Description:** Practical demonstrations of error prevention, graceful degradation, and exception handling introduced progressively from intermediate examples onward.
- **Associated Requirements:** FR-01, NFR-03
- **Detailed Operation:** Demonstrates `try-except-else-finally` blocks starting in `02_intermediate` (`sample_18`) and `03_advanced` (`sample_22`) for `ValueError` and bounds checks, extending to `FileNotFoundError`, `KeyError`, and API errors in upcoming expansion samples.
- **Validation Rules:**
  - Specific exception types must be caught (never use bare `except:`).
  - Diagnostic error feedback and structured logging (`sys.stderr` / `logging`) are applied in `03_advanced` and CLI-oriented samples per `docs/02_engineering_guidelines.md`.
