# Daniel Adewale @03127159
def read_words_from_file(filename):
    """
    Opens a file and reads the contents as a list of words.

    Args:
        filename: The path to the file to read

    Returns:
        A list of words from the file
    """
    with open(filename, 'r') as file:
        words = file.read().split()
    return words


class TrieNode:
    """Node in a Trie data structure"""
    def __init__(self):
        self.children = {}  # Maps characters to TrieNode
        self.is_word = False  # True if this node represents end of a word


class Trie:
    """Trie (prefix tree) for efficient word and prefix lookup"""
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Insert a word into the trie"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word):
        """Check if a word exists in the trie"""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word

    def starts_with(self, prefix):
        """Check if any word in the trie starts with the given prefix"""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


class Boggle:
    def __init__(self, grid, dictionary):
        """
        Constructor for Boggle class

        Args:
            grid: 2D array of strings representing the game board
            dictionary: array of words to search for
        """
        # Store grid (handle None or empty gracefully)
        if grid and len(grid) > 0:
            # Convert grid to lowercase
            self.grid = [[cell.lower() for cell in row] for row in grid]
        else:
            self.grid = []

        # Store dictionary (handle None or empty gracefully)
        if dictionary and len(dictionary) > 0:
            # Convert dictionary to lowercase and filter valid words only
            # Valid words: strings, alphabetic only, at least 3 characters
            self.dictionary = [
                word.lower() for word in dictionary
                if isinstance(word, str) and word.isalpha() and len(word) >= 3
            ]
        else:
            self.dictionary = []

        # Build Trie from dictionary for fast prefix/word lookup
        self.trie = Trie()
        for word in self.dictionary:
            self.trie.insert(word)

        # Solution set to store found words (automatically handles duplicates)
        self.solution = set()

    def setGrid(self, grid):
        """
        Sets the grid to a 2D array of strings

        Args:
            grid: 2D array of strings
        """
        # Store grid (handle None or empty gracefully)
        if grid and len(grid) > 0:
            # Convert grid to lowercase
            self.grid = [[cell.lower() for cell in row] for row in grid]
        else:
            self.grid = []

    def setDictionary(self, dictionary):
        """
        Sets the dictionary to an array of words

        Args:
            dictionary: array of words
        """
        # Store dictionary (handle None or empty gracefully)
        if dictionary and len(dictionary) > 0:
            # Convert dictionary to lowercase and filter valid words only
            # Valid words: strings, alphabetic only, at least 3 characters
            self.dictionary = [
                word.lower() for word in dictionary
                if isinstance(word, str) and word.isalpha() and len(word) >= 3
            ]
        else:
            self.dictionary = []

        # Rebuild Trie with new dictionary
        self.trie = Trie()
        for word in self.dictionary:
            self.trie.insert(word)

    def _dfs(self, row, col, current_word, visited):
        """
        DFS helper method to explore words starting from a given position

        Args:
            row: current row position
            col: current column position
            current_word: word built so far
            visited: set of (row, col) tuples already used in current path
        """
        # Mark current cell as visited
        visited.add((row, col))

        # Get cell value (handles multi-character tiles)
        cell_value = self.grid[row][col]
        current_word += cell_value

        # Early termination: if prefix doesn't exist in trie, stop exploring
        if not self.trie.starts_with(current_word):
            visited.remove((row, col))
            return

        # If valid word (>= 3 chars) and exists in trie, add to solution
        if len(current_word) >= 3 and self.trie.search(current_word):
            self.solution.add(current_word)

        # Explore all 8 adjacent neighbors (including diagonals)
        n = len(self.grid)
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            # Check if neighbor is valid and not visited
            if (0 <= new_row < n and 0 <= new_col < n and
                (new_row, new_col) not in visited):
                self._dfs(new_row, new_col, current_word, visited)

        # Backtrack: remove current cell from visited
        visited.remove((row, col))

    def getSolution(self):
        """
        Returns the solution list of found words

        Returns:
            Sorted list of found words, or empty list if error or invalid input
        """
        try:
            # Reset solution set
            self.solution = set()

            # Check for invalid grid (empty or not set)
            if not self.grid or len(self.grid) == 0:
                return []

            # Check if grid is NxN (square)
            n = len(self.grid)
            for row in self.grid:
                if len(row) != n:
                    return []  # Not a square grid

            # Check for empty dictionary
            if not self.dictionary or len(self.dictionary) == 0:
                return []

            # Try starting from each cell in the grid
            for row in range(n):
                for col in range(n):
                    visited = set()
                    self._dfs(row, col, "", visited)

            # Return as sorted list
            return sorted(list(self.solution))

        except Exception:
            # Return empty array on any error per requirements
            return []

def main():
    grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"],["G", "St", "Qu", "R"],["O", "N", "T", "A"]]
    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry", "qua", "quart", "quartz", "rat", "tar", "tarp", "ten", "went", "wet", "arty", "rhr", "not", "quar"]
    
    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())

if __name__ == "__main__":
    main()
