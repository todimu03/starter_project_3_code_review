# Boggle Solver


class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = dictionary
        self.solutions = []

        # Precompute sets for fast membership checks
        self.word_set = set()
        self.prefix_set = set()
        for w in self.dictionary:
            if w is None:
                continue
            w = str(w).strip().lower()
            if w == "":
                continue
            self.word_set.add(w)
            for i in range(1, len(w) + 1):
                self.prefix_set.add(w[:i])

    def getSolution(self):
        # Handle empty or malformed grids safely
        if not self.grid or len(self.grid) == 0:
            self.solutions = []
            return []

        if len(self.grid) == 1 and len(self.grid[0]) == 0:
            self.solutions = []
            return []

        rows = len(self.grid)
        cols = len(self.grid[0])
        found = set()

        for r in range(rows):
            for c in range(cols):
                self._dfs(r, c, "", set(), found, rows, cols)

        self.solutions = sorted(found)
        return self.solutions

    def _dfs(self, r, c, current, visited, found, rows, cols):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if (r, c) in visited:
            return

        cell = self.grid[r][c]
        if cell is None:
            return

        # Support multi-letter tiles like "Qu"
        piece = str(cell).strip().lower()
        if piece == "":
            return

        new_word = current + piece

        # Prefix pruning
        if new_word not in self.prefix_set:
            return

        # Record valid word (classic Boggle rule: length >= 3)
        if len(new_word) >= 3 and new_word in self.word_set:
            found.add(new_word)

        # Continue exploring neighbors
        visited.add((r, c))
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                self._dfs(
                    r + dr,
                    c + dc,
                    new_word,
                    visited,
                    found,
                    rows,
                    cols,
                )
        visited.remove((r, c))


def main():
    grid = [
        ["T", "W", "Y", "R"],
        ["E", "N", "P", "H"],
        ["G", "Z", "Qu", "R"],
        ["O", "N", "T", "A"],
    ]
    dictionary = [
        "art",
        "ego",
        "gent",
        "get",
        "net",
        "new",
        "newt",
        "prat",
        "pry",
        "qua",
        "quart",
        "quartz",
        "rat",
        "tar",
        "tarp",
        "ten",
        "went",
        "wet",
        "arty",
        "rhr",
        "not",
        "quar",
    ]

    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())


if __name__ == "__main__":
    main()
