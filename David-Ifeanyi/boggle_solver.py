# Boggle Solver
import re


class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = dictionary
        self.solutions = []

    def getSolution(self):
        self.solutions = []
        for word in self.dictionary:
            if self._find_word(word):
                self.solutions.append(word)
        return self.solutions

    def _find_word(self, word):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self._dfs(word, row, col, visited=set()):
                    return True
        return False

    def _dfs(self, word, row, col, visited):
        if not word:
            return True

        if (row < 0 or row >= len(self.grid) or
                col < 0 or col >= len(self.grid[0])):
            return False

        if (row, col) in visited:
            return False

        cell = self.grid[row][col].upper()
        check = word[:len(cell)].upper()

        if cell != check:
            return False

        visited = visited | {(row, col)}
        remaining = word[len(cell):]

        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                if self._dfs(remaining, row + dr, col + dc, visited):
                    return True

        return False


def main():
    grid = [
        ["T", "W", "Y", "R"],
        ["E", "N", "P", "H"],
        ["G", "Z", "Qu", "R"],
        ["O", "N", "T", "A"]
    ]
    dictionary = [
        "art", "ego", "gent", "get", "net", "new", "newt", "prat",
        "pry", "qua", "quart", "quartz", "rat", "tar", "tarp",
        "ten", "went", "wet", "arty", "rhr", "not", "quar"
    ]

    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())


if __name__ == "__main__":
    main()
