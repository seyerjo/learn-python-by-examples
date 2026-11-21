# Project Log: Learn Python by Examples

## To-Do List

### Active & Pending Tasks
- [ ] **TASK-00 (Priority: High):** Audit and format baseline examples (`sample_00` to `sample_23`) with `Black` (88-char line length), verify synchronization with their twin `.md` guides, and validate compliance with the pedagogical tier boundaries defined in `docs/02_engineering_guidelines.md` (consolidates former `TASK-06` where applicable to advanced/CLI samples).
- [ ] **TASK-01 (Priority: High):** Execute the expansion plan (detailed in [Expansion Roadmap (`sample_24` to `sample_65`)](#expansion-roadmap-sample_24-to-sample_65) below) to add new basic, intermediate, and advanced examples (`sample_24` to `sample_65`) toward the 100+ milestone:
  - *Phase 1 (Basic / `code/01_basic`):* Implement data structures (`sample_24` to `sample_32`: lists, tuples, dicts, sets, boolean logic, and f-string formatting).
  - *Phase 2 (Intermediate / `code/02_intermediate`):* Implement building blocks (`sample_33` to `sample_50`), prioritizing modern `pathlib` over legacy `os.path` for file I/O, OOP fundamentals, context managers, and packaging (`venv`/`pip`).
  - *Phase 3 (Advanced & AI / `code/03_advanced`):* Implement advanced systems and API series (`sample_51` to `sample_65`), enforcing strict credentials security via `python-dotenv` and `.env.example` (zero hardcoded secrets), async streaming, and LLM tool use / function calling.
- [ ] **TASK-02 (Priority: Medium):** Add dedicated examples for advanced collection data structures (tuples, dictionary operations, sets, list/dict comprehensions).
- [ ] **TASK-03 (Priority: Medium):** Add practical File I/O and data serialization samples (`pathlib`, JSON parsing, CSV handling, context managers).
- [ ] **TASK-04 (Priority: Medium):** Implement object-oriented programming (OOP) and class design patterns in `/code/02_intermediate` (classes, inheritance, polymorphism, dataclasses).
- [ ] **TASK-05 (Priority: Medium):** Add practical examples demonstrating popular Python Standard Library modules (`datetime`, `collections`, `itertools`, `argparse`, `logging`).
- [ ] **TASK-07 (Priority: Low):** Add automated test suites with `pytest` for advanced algorithmic samples to verify mathematical and computational correctness.

### Completed Tasks
- [x] **TASK-08:** Consolidate legacy 12-file documentation into a streamlined 4-anchor architecture (`/docs/01_project_blueprint.md`, `/docs/02_engineering_guidelines.md`, `/docs/03_project_log.md`, `CHANGELOG.md`).
- [x] **TASK-09:** Systematic code review, modular refactoring, and documentation synchronization for all baseline examples (`sample_00` to `sample_23`).
- [x] **TASK-10:** Standardize formatting, docstrings across all baseline samples, and PEP 484 type hinting in advanced samples (`sample_19`–`sample_23`).
- [x] **TASK-11:** Configure code formatting and linting standards (`Black`, `Prettier`).
- [x] **TASK-12:** Add repository license (`LICENSE`).
- [x] **TASK-13:** Refine and standardize exception handling (`sample_18_exception_handling.py` and `sample_22_robust_input_validation.py`).

### Expansion Roadmap (`sample_24` to `sample_65`)
Detailed example catalog merged from the former expansion plan to implement **TASK-01**. Each item must be created sequentially with both its `.py` script and twin `.md` documentation following `docs/02_engineering_guidelines.md`:

#### Basic Level (`code/01_basic`) — Focus on Fundamentals
- `sample_24_lists`: Basic list creation, indexing, and slicing.
- `sample_25_list_methods`: Appending, extending, removing, and popping elements.
- `sample_26_tuples`: Immutability, packing, and unpacking.
- `sample_27_dictionaries`: Key-value pairs, accessing, adding, and deleting items.
- `sample_28_dictionary_methods`: Using `.keys()`, `.values()`, and `.items()`.
- `sample_29_sets`: Uniqueness, set operations (union, intersection).
- `sample_30_boolean_logic`: `True`, `False`, and boolean operators in conditions.
- `sample_31_f-strings_formatting`: Advanced f-string formatting for numbers and alignment.
- `sample_32_user_input_recap`: Summary example combining input, type conversion, and f-strings.

#### Intermediate Level (`code/02_intermediate`) — Focus on Building Blocks
- `sample_33_slicing_extended`: Slicing with steps, reversing sequences.
- `sample_34_list_comprehensions`: Creating lists concisely from other lists.
- `sample_35_dict_comprehensions`: Creating dictionaries from other iterables.
- `sample_36_lambda_functions`: Simple, anonymous functions.
- `sample_37_map_filter_reduce`: Functional programming concepts.
- `sample_38_args_and_kwargs`: Functions with a variable number of arguments.
- `sample_39_working_with_files_read`: Reading from `.txt` and `.csv` files.
- `sample_40_working_with_files_write`: Writing and appending to `.txt` and `.csv` files.
- `sample_41_context_managers_with_statement`: Ensuring files are properly closed.
- `sample_42_os_module`: Interacting with the operating system (listing files, creating directories — prioritizing modern `pathlib` where appropriate per TASK-01).
- `sample_43_datetime_module`: Working with dates and times.
- `sample_44_json_basics`: Serializing Python objects to JSON and deserializing JSON to Python objects.
- `sample_45_pip_and_requirements`: Introduction to installing packages with `pip` and managing dependencies with `requirements.txt`.
- `sample_46_virtual_environments_venv`: Importance and usage of `venv`.
- `sample_47_classes_and_objects_intro`: Defining a simple class, `__init__` constructor, and instance methods.
- `sample_48_class_attributes_and_methods`: Differentiating between instance and class variables/methods.
- `sample_49_inheritance_basics`: Creating a subclass that inherits from a parent class.
- `sample_50_modules_and_imports`: Creating and importing from custom Python modules.

#### Advanced Level (`code/03_advanced`) — Focus on Applications and APIs
- `sample_51_decorators`: Introduction to decorators for modifying function behavior.
- `sample_52_generators_and_yield`: Memory-efficient data processing.
- `sample_53_threading_basics`: Running code concurrently for I/O-bound tasks.
- `sample_54_multiprocessing_basics`: Running code in parallel for CPU-bound tasks.
- `sample_55_asyncio_basics`: Introduction to asynchronous programming with `async`/`await`.
- `sample_56_regular_expressions_re`: Pattern matching in strings.
- `sample_57_web_scraping_requests_bs4`: Using `requests` to fetch a webpage and `BeautifulSoup4` to parse its HTML.
- `sample_58_building_a_simple_cli`: Creating a command-line interface with `argparse` or `click`.
- **API Interaction Series:**
  - `sample_59_api_get_requests`: Making GET requests to a public REST API (e.g., JSONPlaceholder) and processing the JSON response.
  - `sample_60_api_error_handling`: Handling potential API errors (e.g., 404 Not Found, 500 Server Error).
  - `sample_61_api_authentication_basics`: Using API keys or tokens in request headers.
- **AI API Series:**
  - `sample_62_ai_api_setup_and_auth`: Setting up an AI API client (e.g., OpenAI, Anthropic, Gemini) and handling authentication securely using environment variables (`python-dotenv` and `.env.example`, zero hardcoded secrets).
  - `sample_63_ai_api_text_generation`: Sending a simple prompt to a language model and printing the response.
  - `sample_64_ai_api_streaming_responses`: Handling streaming responses from a language model for real-time output.
  - `sample_65_ai_api_function_calling`: Conceptual example of how to define tools/functions that an AI model can use.

> **Milestone Target:** Implementing `sample_24` through `sample_65` brings the collection to **66 examples**. The remaining **34+ examples** toward the 100+ goal will cover complex data structures, design patterns, and additional API integrations.

---

## Development Log

### [Unreleased] - Public Showcase README Overhaul (2026-11-21)
- **Activity:** Redesigned `README.md` into a portfolio-oriented showcase layout featuring a custom local header banner (`.github/assets/banner.png`), emoji-free headings with 1:1 navigation anchors, collapsible difficulty-badged example tables, and an Author Card (`.github/assets/avatar.png`) with verified contact badges and a Star callout.
- **Key Decisions:**
  - Moved the workflow Mermaid diagram inside `## Architecture` so readers jump directly from the banner into `## Overview` and `## Quick Start`.
  - Replaced bulleted example listings with collapsible 4-column Markdown tables (`BASIC`, `INTERMEDIATE`, `ADVANCED`) to avoid line-wrapped links and scale cleanly toward the 100+ sample goal.
  - Focused `README.md` on technical showcase and feedback via Issues.

### [Unreleased] - Expansion Plan Integration & Archive Cleanup (2026-11-18)
- **Activity:** Merged the expansion roadmap (`sample_24` to `sample_65`) from `.archive/docs/plan_expansion.md` directly into `docs/03_project_log.md` and cleaned up obsolete `.archive` subdirectories.
- **Key Decisions:**
  - Consolidated `sample_24`–`sample_65` specifications into `docs/03_project_log.md` under `### Expansion Roadmap` and updated `TASK-01` to point internally to that section.
  - Removed `.archive/docs/` (`plan_expansion.md` after merging and obsolete `plan_review.md`), `.archive/code/`, `.archive/rules/`, and `.archive/mbank/` (retaining the empty `.archive/` folder locally).
  - Aligned `README.md` and updated cross-references across `/docs`.

### Milestone [1.2.5] - Streamlined Documentation Architecture & Structure Reorganization (2026-08-25)
- **Activity:** Migrated documentation from the legacy 12-file layout into the consolidated 4-anchor project documentation system and reorganized code difficulty folders.
- **Key Decisions:**
  - Standardized on 3 core documentation anchors in `/docs` (`01_project_blueprint.md`, `02_engineering_guidelines.md`, `03_project_log.md`) plus root `CHANGELOG.md`.
  - Reorganized code subdirectories into `01_basic/`, `02_intermediate/`, and `03_advanced/` to enforce natural pedagogical sorting in file trees and synchronized all cross-references.
  - Aligned root documentation (`README.md`) with official workflows.
  - Archived legacy memory bank and planning documentation to `.archive/mbank/` and `.archive/docs/` (both were subsequently merged/removed on 2026-11-18).
  - Enriched expansion task `TASK-01` with phase breakdowns, modern `pathlib` preference, and strict credentials security for the AI series.

### Milestone [1.2.0] - Project-Wide Refactoring & Synchronization (Samples 00-23)
- **Summary:** Completed comprehensive quality overhaul of all initial samples.
- **Key Decisions:**
  - *Modularity:* Refactored monolithic scripts into small, single-purpose functions demonstrating clean architecture.
  - *Pedagogical Clarity:* Enhanced console outputs and in-code comments, introducing warnings for common beginner errors (such as `ValueError` on unvalidated `int(input())`).
  - *Algorithmic Progression:* Structured advanced samples (`19`, `20`, `21`) into a clear progression (brute-force -> approximation -> binary search) with iteration telemetry.
  - *Robustness:* Standardized input validation and defensive `try-except` blocks across all interactive samples.

### Milestone [1.1.0] - Quality & Pedagogy Refactor (Samples 00-10)
- **Summary:** Systematic refactoring and improvement of basic samples (00 to 10).
- **Key Decisions:**
  - Introduced the DRY (Don't Repeat Yourself) principle in `sample_08`.
  - Enhanced docstrings and comments explaining raw strings, mutability, and type hinting fundamentals.

### Milestone [1.0.0] - Initial Release
- **Summary:** Initial project baseline creation with difficulty-categorized directories and starter examples.
