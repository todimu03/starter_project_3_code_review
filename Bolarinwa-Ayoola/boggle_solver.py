"""
Name: Bolarinwa Ayoola
SID: 004002448
Boggle Solver Program
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        for word in words:
            self.insert(word.upper())

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True


class Boggle:
    """
    class that represents a boggle game and solver
    """

    def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = dictionary
        self.solutions = []
        self._solved = False
        self._solve()

    def setGrid(self, grid):
        self.grid = grid
        self._solved = False

    def setDictionary(self, dictionary):
        self.dictionary = dictionary
        self._solved = False

    def getSolution(self):
        if not self._solved:
            self._solve()
        return self.solutions

    def _solve(self):
        self.solutions = []
        self._solved = True

        if not self.grid or not self.dictionary:
            return

        if len(self.grid) == 0 or len(self.grid[0]) == 0:
            return

        rows = len(self.grid)

        trie = Trie(self.dictionary)
        found_words = set()

        for i in range(rows):
            for j in range(len(self.grid[i])):
                visited = [[False] * len(self.grid[r]) for r in range(rows)]
                self._dfs(i, j, trie.root, "", visited, found_words, trie)

        self.solutions = sorted(found_words)

    def _dfs(self, row, col, node, current_word, visited, found_words, trie):
        if row < 0 or row >= len(self.grid):
            return

        if col < 0 or col >= len(self.grid[row]):
            return

        if visited[row][col]:
            return

        tile = self.grid[row][col].upper()

        temp_node = node
        for char in tile:
            if char not in temp_node.children:
                return
            temp_node = temp_node.children[char]

        visited[row][col] = True
        new_word = current_word + tile

        if len(new_word) >= 3 and temp_node.is_word:
            found_words.add(new_word)

        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]

        for dr, dc in directions:
            self._dfs(row + dr, col + dc, temp_node,
                      new_word, visited, found_words, trie)

        visited[row][col] = False


def main():
    grid = [["A", "B", "C", "D"],
            ["E", "F", "G", "H"],
            ["IE", "J", "K", "L"],
            ["A", "B", "C", "D"]]

    dictionary = ["ABEF", "AFJIEEB", "DGKD", "DGKA"]

    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())


if __name__ == "__main__":
    main()
