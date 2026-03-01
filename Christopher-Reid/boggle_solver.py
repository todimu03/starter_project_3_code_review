# Boggle Solver
import re

class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = None
        self.words = set()
        self.prefixes = set()
        self.solutions = set()

        self.setGrid(grid)
        self.setDictionary(dictionary)

    def setGrid(self, grid):
        """Validates and normalizes the Boggle grid into a 2D lowercase list."""
        if not grid or not isinstance(grid, list):
            raise ValueError("Grid must be a non-empty list of lists.")

        rows = len(grid)

        if not isinstance(grid[0], list):
            raise ValueError("Grid must be a 2D list.")

        cols = len(grid[0])
        normalized_grid = []

        for row in grid:
            # Check for regular consistency
            if not isinstance(row, list) or len(row) != cols:
                raise ValueError("Grid must be rectangular (all rows must have the same length).")

            new_row = []
            for cell in row:
                # Validate that each tile is a string and purely alphabetic ('A', 'Qu', etc.)
                if not isinstance(cell, str) or not cell.isalpha():
                    raise ValueError(f"Invalid cell content '{cell}': Only alphabetic strings allowed.")
                new_row.append(cell.lower())
            normalized_grid.append(new_row)

        self.grid = normalized_grid

    def setDictionary(self, dictionary):
        """Normalizes the dictionary and pre-calculates a prefix set for pruning."""
        if not isinstance(dictionary, list):
            raise TypeError("Dictionary must be provided as a list of strings.")

        # Resetting sets to ensure clean state if setDictionary is called multiple times
        self.words = set()
        self.prefixes = set()

        for word in dictionary:
            if isinstance(word, str):
                clean_word = word.lower()
                # Boggle requirement of at least 3 letters
                if len(clean_word) >= 3:
                    self.words.add(clean_word)
                    # Pre-calculate prefixes to optimize the DFS search
                    for i in range(1, len(clean_word) + 1):
                        self.prefixes.add(clean_word[:i])

    def getSolution(self):
        """Initiates the search from every cell in the grid and returns sorted results."""
        # Fail-fast if grid or dictionary wasn't initialized correctly
        if not self.grid or not self.words:
            return []

        rows = len(self.grid)
        cols = len(self.grid[0])
        self.solutions = set()
        
        # Track visited cells to prevent reusing the same tile in a single word
        visited = [[False] * cols for _ in range(rows)]

        # Starts a new search path from every single tile on the grid
        for r in range(rows):
            for c in range(cols):
                self._dfs(r, c, visited, "")

        return sorted(list(self.solutions))
    
    def _dfs(self, r, c, visited, current):
        # Base case boundary check 
        if r < 0 or r >= len(self.grid) or c < 0 or c >= len(self.grid[0]):
            return

        # Base case check to see if a tile has already been used in the current path
        if visited[r][c]:
            return

        # Build the word with the current tile
        new_word = current + self.grid[r][c]

        # Pruning: If the current string isn't a prefix of any word, stop searching this path
        if new_word not in self.prefixes:
            return

        # Mark cells as visited before recursing
        visited[r][c] = True
        
        # If path is a valid word, add it to results
        if new_word in self.words:
            self.solutions.add(new_word)

        # Explore all 8 neighbors
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr != 0 or dc != 0:
                    self._dfs(r + dr, c + dc, visited, new_word)

        # Backtrack: Unmark this cell for other potential word paths
        visited[r][c] = False


def main():
    grid = [
      ["T", "W", "Y", "R"], 
      ["E", "N", "P", "H"],
      ["G", "St", "Qu", "R"],
      ["O", "N", "T", "A"]
      ]
    
    dictionary = [
      "art", "ego", "gent", "get", 
      "net", "new", "newt", "prat", 
      "pry", "qua", "quart", "rat", 
      "tar", "tarp", "ten", "went", 
      "wet", "stont", "not", "quar", 
      "nest", "west", "test", "gest",  
      ]
    
    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())

if __name__ == "__main__":
    main()