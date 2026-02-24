Starter Project 3 Code Review Report

Student: Ashley Petgrave
Project: Boggle Solver
Files: boggle_solver.py, boggle_solver.py.orig, tests.py

1. Goal of this assignment

The goal of this project was to improve code readability and maintainability through a code review workflow, then verify improvements using automated testing and linting. The final deliverables include an original snapshot of the solver (.orig), an improved solver, a test suite, and evidence of static analysis cleanup.

2. Starting point and major issues found

When I began working in Codio, the project did not have a working solver method implemented in the Boggle class. Tests also did not run initially due to a formatting issue in tests.py and a mismatch between the solver method name expected by the tests and the method(s) available in the class.

The main categories of issues I addressed were:
	•	Missing functionality needed for the tests to execute successfully
	•	Inconsistent indentation and tab/space mixing that prevented Python from running
	•	Lack of a clear public API method in the Boggle class
	•	Style and readability issues detected by pycodestyle

3. Functional improvements made

I implemented a complete Boggle solver inside the Boggle class and created a public method named getSolution() so the test suite could call it consistently.

Key functional decisions:
	•	The solver performs a depth-first search (DFS) starting from every grid position.
	•	It explores all 8 neighboring directions (including diagonals).
	•	It does not allow reusing the same cell in a single word path.
	•	It supports multi-letter grid tiles (example: "Qu") by treating each cell as a string segment that can be more than one character.
	•	It applies the classic Boggle rule that valid words must be at least length 3. This prevented short dictionary entries such as 1–2 letter words from being counted as solutions.

To improve performance and readability, I precomputed:
	•	word_set for fast dictionary membership checks.
	•	prefix_set to prune searches early when a partial string is not a prefix of any dictionary word.

4. Readability and maintainability improvements

To make the code easier to understand and modify later, I focused on:
	•	Clear separation of responsibilities:
	•	getSolution() handles setup, edge cases, and collecting results.
	•	_dfs() handles recursive search and pruning.
	•	Defensive checks for empty or malformed grids so the solver returns [] rather than failing.
	•	Consistent naming and formatting, avoiding overly nested logic where possible.
	•	Using sets (found, word_set, prefix_set) to make intent obvious and keep lookups efficient.

5. Testing approach and results

I used the provided test framework in tests.py to validate solver behavior. After fixing indentation issues in the test file, I ran:
	•	python tests.py

All tests passed successfully.

I also validated that the solver ran correctly in a demo execution with:
	•	python boggle_solver.py

This printed a reasonable list of found words from the sample grid/dictionary used in main().

6. Linting and static analysis (pycodestyle)

I ran the linter:
	•	pycodestyle boggle_solver.py tests.py

The initial lint output included:
	•	E501 line too long issues in boggle_solver.py
	•	E402 import ordering issues in tests.py
	•	W292/W391 newline formatting issues

Fixes applied:
	•	Wrapped long lines to meet the 79-character limit (E501).
	•	Used # noqa: E402 on the import in tests.py because the sys.path.append(...) line must occur before importing Boggle, and that ordering is required for the file to run correctly in Codio.
	•	Ensured files ended with exactly one newline and removed extra blank lines at EOF.

After these changes, pycodestyle produced no output, indicating a clean lint run.

7. Peer review status (documentation)

My code review partner, Langyia Ogoma Philemon, reviewed my pull request on February 20, 2026 and submitted an approving review. Their feedback confirmed that the solver structure, prefix pruning, and edge case handling were clear. 
They also noted that my grid validation assumed all rows had the same length. In response, I updated the solver to validate grid shape up front (empty grid, empty first row, non-list rows, and inconsistent row lengths) and return an empty list for malformed grids. 
After this change, the unit tests still passed and pycodestyle remained clean.

Review I completed

I also reviewed Langyia’s Boggle solver pull request and left inline comments and a summary review. My feedback focused on consistent indentation/style, reducing duplicated dictionary/prefix setup logic, clarifying handling of special tiles like Qu, and small readability improvements.
8. Summary

This project improved the solver from a non-functional skeleton to a working, tested, and lint-clean implementation. The final version is structured to be readable and maintainable, with clear responsibilities between methods, prefix pruning for efficiency, and full compliance with the linter. Tests pass in Codio and the solver behaves as expected on sample inputs.