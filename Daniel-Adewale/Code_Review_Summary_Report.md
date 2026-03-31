# Code Review Summary Report

**Course:** CSCI 375 – Software Engineering  
**Assignment:** Boggle Solver – Peer Code Review  
**Author:** Daniel Adewale  
**Review Partner:** Dionna Fleming  

---

## Overview

The assignment required implementing a Boggle solver in Python. Given an N×N grid of letter tiles and a dictionary of valid words, the program finds all dictionary words that can be formed by traversing adjacent cells (including diagonals) without reusing any cell in a single path. Words must be at least three characters long.

My approach centered on using a Trie (prefix tree) data structure for efficient word and prefix lookups, paired with a depth-first search (DFS) that explores all paths from every cell on the board. The Trie enables early termination during the DFS — if the current path does not match any prefix in the dictionary, the search backtracks immediately rather than continuing down a dead end. I also accounted for multi-character tiles like "Qu" and "St," converted all input to lowercase for consistency, and filtered the dictionary to only include valid alphabetic strings of three or more characters. The solution stores found words in a set to avoid duplicates and returns them as a sorted list.

## Feedback I Received

During the code review, Dionna and I discussed each other's implementations in a fairly informal back-and-forth. She did not raise any major structural or logical concerns about my code. Her primary suggestion was that I could benefit from adding more descriptive inline comments throughout my code. While I had docstrings on my classes and methods, some of the logic within the DFS traversal and the input validation sections could have used brief clarifying comments to make the intent clearer to someone reading the code for the first time.

## Feedback I Gave

When reviewing Dionna's code, I left a comment on her DFS method noting where she explores all eight neighboring cells using nested loops over `[-1, 0, 1]` for both `dy` and `dx`. I pointed out that this section handles horizontal, vertical, and diagonal adjacency, which is a core part of the Boggle traversal logic. Her implementation was functional and clean overall. One notable difference between our approaches was that she used a prefix set (storing all prefixes of every dictionary word in a Python set) for pruning, whereas I used a Trie. Both achieve early termination, but the Trie is generally more memory-efficient for large dictionaries. She also used a 2D boolean array for tracking visited cells, while I used a set of coordinate tuples. Neither approach is inherently better — they are just different design choices. Beyond that, I did not identify any critical bugs or issues in her code.

## Improvements I Implemented

Based on the feedback about inline comments, I reviewed my code and confirmed that my existing docstrings and comments were already fairly descriptive. I kept my commenting style consistent but made a mental note to be more deliberate about inline comments in future projects, especially within complex recursive logic.

The more substantial improvements I made came from running static analysis, which prompted me to clean up formatting issues like line length, spacing, and how I broke long conditional expressions across multiple lines. These changes improved readability without altering any logic.

## Static Analysis Results

I ran `pycodestyle` on my Boggle solver to check for PEP 8 compliance. The main issues flagged were related to line length and formatting rather than logic or structure. Specific fixes I made include:

- Breaking long list comprehensions and conditional statements across multiple lines to stay within the recommended line length. For example, the dictionary filtering comprehension in `__init__` and `setDictionary` was reformatted to place each condition on its own line.
- Reformatting the `directions` list in the DFS method into a visually structured 3×3-style layout, making the eight directional offsets easier to read at a glance.
- Splitting long `if` conditions in the neighbor-checking logic across multiple lines with proper indentation.
- Reformatting the `grid` and `dictionary` definitions in `main()` to span multiple lines instead of being packed onto single long lines.

After applying these fixes, `pycodestyle` returned no remaining warnings. The linted version of my code maintained identical functionality while being more readable and PEP 8 compliant.

## Regression Testing

After making the formatting and style changes, I verified correctness by running the existing test cases. The `main()` function includes a test grid with multi-character tiles ("St" and "Qu") and a dictionary of 22 words, including edge cases like the non-alphabetic string "rhr" and the short prefix "quar." I confirmed that the output matched the expected results — valid words like "art," "ego," "gent," "get," "net," "new," "newt," "ten," and "went" were found, while invalid entries were correctly excluded. I also linted my test code with `pycodestyle` to ensure consistency across all files. No regressions were introduced by the formatting changes.

## Reflection

This code review experience reinforced a few important lessons about professional software development. First, even when code is logically correct and well-structured, readability matters. PEP 8 is not just a style preference — it is a shared standard that makes Python code easier for anyone to read and maintain. Running `pycodestyle` caught issues I would not have noticed on my own, and the reformatted code is noticeably cleaner.

Second, peer review is valuable even when no bugs are found. Comparing my Trie-based approach with Dionna's prefix-set approach gave me a better understanding of the trade-offs between different data structures for the same problem. It also reminded me that there is rarely one "right" way to solve a problem — what matters is that the solution is correct, efficient, and readable.

Finally, the experience gave me a better appreciation for the kind of production-level code practices used in industry. Writing code that passes linting, survives peer review, and is backed by regression testing is the baseline expectation in professional environments. This assignment was a good step toward building those habits.
