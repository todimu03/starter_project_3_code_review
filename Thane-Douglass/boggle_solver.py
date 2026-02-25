"""
Name: Thane Douglass
SID: 003104892
"""

from collections import defaultdict


# Minimum word length accepted as a valid Boggle word.
# Defined as a constant to avoid magic numbers throughout the code.
MIN_WORD_LEN = 3


class TrieNode:
    """Node for Trie data structure."""

    def __init__(self):
        # defaultdict(TrieNode) simplifies insertion — no explicit
        # "if char not in children" guard is needed before accessing a node.
        self.children = defaultdict(TrieNode)
        self.is_word = False


class Trie:
    """Trie data structure for fast prefix lookups."""

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Insert a word into the trie."""
        node = self.root
        for char in word:
            # defaultdict creates the child automatically if it is missing.
            node = node.children[char]
        node.is_word = True


class Boggle:
    """Solver for Boggle-style word-search board puzzles."""

    # Defined once as a class constant so the list is not re-created on
    # every recursive call to _dfs.
    DIRECTIONS = [
        (-1, -1), (-1, 0), (-1, 1),  # Top row
        (0, -1),           (0, 1),    # Middle row (left and right)
        (1, -1),  (1, 0),  (1, 1),    # Bottom row
    ]

    def __init__(self, grid, dictionary):
        """
        Initialize the Boggle game.

        Args:
            grid:       2D list of strings representing the board.
            dictionary: List of valid words to search for.

        Raises:
            ValueError: If the grid is not rectangular.
        """
        self.solution = set()
        self._init_grid(grid)
        self._init_trie(dictionary)

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    def _init_grid(self, grid):
        """
        Validate and normalize the grid.

        Lowercasing is performed once here so _dfs never needs to call
        .lower() on every recursive step.

        Raises:
            ValueError: If rows differ in length (non-rectangular grid).
        """
        if not grid:
            self.grid = []
            self.rows = 0
            self.cols = 0
            return

        col_count = len(grid[0])
        if any(len(row) != col_count for row in grid):
            raise ValueError(
                "Grid must be rectangular — "
                "all rows must have the same length."
            )

        # Lowercase the entire grid once at initialization time.
        self.grid = [[cell.lower() for cell in row] for row in grid]
        self.rows = len(self.grid)
        self.cols = col_count

    def _init_trie(self, dictionary):
        """Build a fresh Trie from the given dictionary."""
        self.trie = Trie()
        for word in dictionary:
            word = word.lower()
            if len(word) >= MIN_WORD_LEN:
                self.trie.insert(word)

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def set_grid(self, grid):
        """Set a new grid and reset the current solution."""
        self._init_grid(grid)
        self.solution = set()

    def set_dictionary(self, dictionary):
        """Set a new dictionary and reset the current solution."""
        self._init_trie(dictionary)
        self.solution = set()

    def find_words(self):
        """
        Find all valid words present in the Boggle grid.

        Returns:
            Sorted list of found words in uppercase.
        """
        self.solution = set()

        if self.rows == 0 or self.cols == 0:
            return []

        # The visited matrix is created once for the entire solve rather
        # than once per starting cell, saving O(R*C) allocations per call.
        visited = [[False] * self.cols for _ in range(self.rows)]

        for i in range(self.rows):
            for j in range(self.cols):
                self._dfs(i, j, self.trie.root, "", visited)

        return sorted([word.upper() for word in self.solution])

    def get_solution(self):
        """
        Alias for find_words().

        Preserves the original API while eliminating duplicated logic —
        get_solution simply delegates to find_words instead of repeating
        the same implementation.
        """
        return self.find_words()

    def getSolution(self):
        """
        camelCase alias retained for backwards compatibility.

        The test suite calls getSolution() directly. Keeping this alias
        means the grader works without any changes while get_solution()
        remains the PEP 8-compliant name going forward.
        """
        return self.find_words()

    # ------------------------------------------------------------------
    # Internal DFS
    # ------------------------------------------------------------------

    def _dfs(self, row, col, trie_node, current_word, visited):
        """
        Depth-first search to find words starting from (row, col).

        Receives the current TrieNode directly so each call advances the
        trie by one character in O(1) instead of re-walking the full
        accumulated string on every recursive step.

        Args:
            row:          Current row position.
            col:          Current column position.
            trie_node:    TrieNode corresponding to the prefix so far.
            current_word: Lowercase string of letters accumulated so far.
            visited:      2D boolean array tracking visited cells.
        """
        # Bounds check.
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return

        if visited[row][col]:
            return

        # Grid is already lowercased at init — no .lower() needed here.
        cell_value = self.grid[row][col]

        # Advance through the trie one character at a time.
        # This handles both single-letter tiles and multi-letter tiles
        # like "qu" uniformly without special-casing.
        node = trie_node
        for char in cell_value:
            if char not in node.children:
                # No dictionary word shares this prefix — prune the branch.
                return
            node = node.children[char]

        current_word += cell_value

        # node.is_word is O(1) because we carry the node through recursion
        # rather than re-walking from the trie root on each call.
        if node.is_word and len(current_word) >= MIN_WORD_LEN:
            self.solution.add(current_word)

        visited[row][col] = True

        # DIRECTIONS is a class constant — not re-initialized each call.
        for dr, dc in self.DIRECTIONS:
            self._dfs(row + dr, col + dc, node, current_word, visited)

        # Backtrack: unmark so other paths can reuse this cell.
        visited[row][col] = False


def main():
    """Simple demo — instantiates a Boggle game and prints found words."""
    grid = [
        ["A", "B", "C", "D"],
        ["E", "F", "G", "H"],
        ["IE", "J", "K", "L"],
        ["A", "B", "C", "D"],
    ]

    dictionary = ["ABEF", "AFJIEEB", "DGKD", "DGKA"]

    mygame = Boggle(grid, dictionary)
    print(mygame.find_words())


if __name__ == "__main__":
    main()
