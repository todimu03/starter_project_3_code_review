class Boggle:
    """
    Boggle solver class.

    Data Members (as required):
      - grid: NxN 2D array of strings
        (e.g., "A" or "Qu")
      - dictionary: list of words (strings)
      - solution: list of found words
    """

    def __init__(self, grid, dictionary):
        """Constructor: sets grid and dictionary.
        Prepares internal structures."""
        self.grid = None
        self.dictionary = None
        self.solution = []

        self._n = 0
        self._prefixes = {}    # set-like dict: prefix -> True
        self._dict_words = {}  # set-like dict: word -> True

        self.setGrid(grid)
        self.setDictionary(dictionary)

    def setGrid(self, grid):
        """Setter for the grid. Expects an NxN 2D list of strings."""
        self.grid = grid
        self._n = 0

        if not self._is_valid_grid(grid):
            return

        self._n = len(grid)

    def setDictionary(self, dictionary):
        """
        Setter for the dictionary.
        Builds:
          - _dict_words: fast lookup for full words
          - _prefixes: fast pruning during DFS
        """
        self.dictionary = dictionary
        self._dict_words = {}
        self._prefixes = {}

        if not self._is_valid_dictionary(dictionary):
            return

        for w in dictionary:
            if not isinstance(w, str):
                continue

            word = w.strip().upper()
            if len(word) == 0:
                continue

            self._dict_words[word] = True

            for i in range(1, len(word) + 1):
                self._prefixes[word[:i]] = True

    def getSolution(self):
        """Return found words (uppercase).
        Return [] if grid or dictionary invalid."""
        self.solution = []

        if (
            not self._is_valid_grid(self.grid)
            or not self._is_valid_dictionary(self.dictionary)
        ):
            return []

        if self._n == 0:
            return []

        found = {}

        for r in range(self._n):
            for c in range(self._n):
                visited = self._make_visited_matrix(self._n)
                self._dfs(r, c, "", visited, found)

        result = []
        for w in found:
            result.append(w)
        result.sort()

        self.solution = result
        return result

    def _dfs(self, r, c, current, visited, found):
        """
        Depth-first search from (r, c), building the string `current`.
        Uses `visited` to prevent reusing tiles and prefixes to prune.
        """
        visited[r][c] = True

        tile = self.grid[r][c]
        if tile is None:
            visited[r][c] = False
            return

        next_word = current + tile.upper()

        if next_word not in self._prefixes:
            visited[r][c] = False
            return

        if len(next_word) >= 3 and next_word in self._dict_words:
            found[next_word] = True

        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue

                nr = r + dr
                nc = c + dc

                if self._in_bounds(nr, nc) and not visited[nr][nc]:
                    self._dfs(nr, nc, next_word, visited, found)

        visited[r][c] = False

    def _in_bounds(self, r, c):
        """Check if (r, c) is inside the grid."""
        return 0 <= r < self._n and 0 <= c < self._n

    def _make_visited_matrix(self, n):
        """Create an NxN False matrix without imports."""
        visited = []
        for _ in range(n):
            row = []
            for _ in range(n):
                row.append(False)
            visited.append(row)
        return visited

    def _is_valid_grid(self, grid):
        """
        Grid rules:
          - Must be a non-empty 2D list
          - Must be square NxN
          - Every cell must be a non-empty string
        """
        if not isinstance(grid, list) or len(grid) == 0:
            return False

        n = len(grid)
        for row in grid:
            if not isinstance(row, list) or len(row) != n:
                return False
            for cell in row:
                if not isinstance(cell, str) or len(cell.strip()) == 0:
                    return False
        return True

    def _is_valid_dictionary(self, dictionary):
        """Dictionary must be a list.
        Items may be ignored if not strings."""
        if not isinstance(dictionary, list):
            return False
        return True


def main():
    grid = [
        ["T", "W", "Y", "R"],
        ["E", "N", "P", "H"],
        ["G", "Z", "Qu", "R"],
        ["O", "N", "T", "A"],
    ]

    dictionary = [
        "art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry",
        "qua", "quart", "quartz", "rat", "tar", "tarp", "ten", "went",
        "wet", "arty", "rhr", "not", "quar",
    ]

    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())


if __name__ == "__main__":
    main()
