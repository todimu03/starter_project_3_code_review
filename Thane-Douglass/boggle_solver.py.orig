"""
Name: Thane Douglass
SID: 003104892
"""

class TrieNode:
    """Node for Trie data structure"""
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    """Trie data structure for fast prefix lookups"""
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
        """Check if word exists in trie"""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word
    
    def starts_with(self, prefix):
        """Check if any word starts with prefix"""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


class Boggle:
    def __init__(self, grid, dictionary):
        """
        Initialize the Boggle game
        
        Args:
            grid: 2D array of strings representing the board
            dictionary: list of valid words
        """
        self.grid = grid
        self.rows = len(grid) if grid else 0
        self.cols = len(grid[0]) if grid and len(grid[0]) > 0 else 0
        
        # Build trie from dictionary for fast prefix lookup
        self.trie = Trie()
        for word in dictionary:
            # Store all words in lowercase for case-insensitive comparison
            # Filter out words shorter than 3 letters
            if len(word) >= 3:
                self.trie.insert(word.lower())
        
        self.solution = set()
        
    def setGrid(self, grid):
        """Set a new grid"""
        self.grid = grid
        self.rows = len(grid) if grid else 0
        self.cols = len(grid[0]) if grid and len(grid[0]) > 0 else 0
        self.solution = set()
        
    def setDictionary(self, dictionary):
        """Set a new dictionary"""
        self.trie = Trie()
        for word in dictionary:
            if len(word) >= 3:
                self.trie.insert(word.lower())
        self.solution = set()
    
    def getSolution(self):
        """
        Find all valid words in the Boggle grid
        
        Returns:
            List of valid words found (in uppercase)
        """
        self.solution = set()
        
        # Handle empty grid
        if self.rows == 0 or self.cols == 0:
            return []
        
        # Start DFS from each cell in the grid
        for i in range(self.rows):
            for j in range(self.cols):
                visited = [[False] * self.cols for _ in range(self.rows)]
                self._dfs(i, j, "", visited)
        
        # Convert to uppercase and sort for consistent output
        return sorted([word.upper() for word in self.solution])

    def find_words(self):
        """
        Find all valid words in the Boggle grid
        
        Returns:
            List of valid words found (in uppercase)
        """
        self.solution = set()
        
        # Handle empty grid
        if self.rows == 0 or self.cols == 0:
            return []
        
        # Start DFS from each cell in the grid
        for i in range(self.rows):
            for j in range(self.cols):
                visited = [[False] * self.cols for _ in range(self.rows)]
                self._dfs(i, j, "", visited)
        
        # Convert to uppercase and sort for consistent output
        return sorted([word.upper() for word in self.solution])
    
    def _dfs(self, row, col, current_word, visited):
        """
        Depth-first search to find words starting from (row, col)
        
        Args:
            row: Current row position
            col: Current column position
            current_word: Word built so far (lowercase)
            visited: 2D array tracking visited cells
        """
        # Check bounds
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return
        
        # Check if already visited
        if visited[row][col]:
            return
        
        # Add current cell's letters to word
        cell_value = self.grid[row][col].lower()
        
        # Handle "Qu" tile - treat as "qu"
        if cell_value == "qu":
            current_word += "qu"
        else:
            current_word += cell_value
        
        # PRUNE: If no word starts with this prefix, stop searching
        if not self.trie.starts_with(current_word):
            return
        
        # Check if current word is a valid word (≥ 3 letters)
        if len(current_word) >= 3 and self.trie.search(current_word):
            self.solution.add(current_word)
        
        # Mark as visited
        visited[row][col] = True
        
        # Explore all 8 adjacent neighbors (including diagonals)
        directions = [
            (-1, -1), (-1, 0), (-1, 1),  # Top row
            (0, -1),           (0, 1),    # Middle row (left and right)
            (1, -1),  (1, 0),  (1, 1)     # Bottom row
        ]
        
        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc
            self._dfs(new_row, new_col, current_word, visited)
        
        # Backtrack: unmark as visited
        visited[row][col] = False


def main():
    grid = [["A", "B", "C", "D"],
            ["E", "F", "G", "H"], 
            ["IE", "J", "K", "L"], 
            ["A", "B", "C", "D"]]

    dictionary = ["ABEF", "AFJIEEB", "DGKD", "DGKA"]

    mygame = Boggle(grid, dictionary)
    print(mygame.find_words())


if __name__ == "__main__":
    main()
