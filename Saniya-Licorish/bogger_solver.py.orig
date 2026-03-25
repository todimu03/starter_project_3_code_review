class Boggle:

    # Constructor that initializes the grid, dictionary, and solutions list
    def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = dictionary
        self.solutions = []

    # setter methods for grid and dictionary
    def setGrid(self, grid):
        self.grid = grid

    def setDictionary(self, dictionary):
        self.dictionary = dictionary

    # Boggle method, has to be called specifically, unlike the constructor
    def Boggle(self, grid, dictionary):
        self.setGrid(grid)
        self.setDictionary(dictionary)

    def getSolution(self):
        # if the grid is empty
        if not self.grid:
            return []
        # if the dictionary is empty
        if not self.dictionary:
            return []
        
        # formats the grid and dictionary 
        format_grid = self.format_grid(self.grid)
        size = len(format_grid)

        if any(len(row) != size for row in format_grid):
            return []

        format_dictionary = self.format_dictionary(self.dictionary)
        if not format_dictionary:
            return []

        prefix_sets = self.prefix_sets(format_dictionary)
        words_set, prefix_set = prefix_sets
        # tracks visited cells and prevents reuse 
        visited = [[False] * size for i in range(size)]
        solutions = set()

        # loops through each cell in the grid
        for y in range(size):
            for x in range(size):
                self.find_all_words(y, x, format_grid, words_set, prefix_set, "", visited, solutions)

        self.solutions = sorted(solutions)
        return self.solutions

    # helper methods for formatting grid and dictionary
    @staticmethod
    def format_grid(grid):
        return [[str(cell).strip().upper() for cell in row] for row in grid]

    @staticmethod
    def format_dictionary(dictionary):
        return {word.strip().upper() for word in dictionary if isinstance(word, str) and word.strip()}

    # helper method to create sets of words and prefixes
    def prefix_sets(self, words):
        words_set = set()
        prefix_set = set()
        for word in words:
            words_set.add(word)
            for i in range(1, len(word) + 1):
                prefix_set.add(word[:i])
        return words_set, prefix_set

    # finds all valid words starting from a given cell
    def find_all_words(self, y, x, grid, words_set, prefix_set, word, visited, solutions):
        if visited[y][x]:  # Base case: can't reuse the same tile in the current path
            return
        
        # next word formed by adding the current cell's letter
        next_word = word + grid[y][x]
        # if the next word is not a valid prefix, backtrack
        if next_word not in prefix_set:
            return

        visited[y][x] = True

        # checks the next word is at least 3 letters and is in the dictionary before adding to solutions
        if len(next_word) >= 3 and next_word in words_set:
            solutions.add(next_word)

        # explores all neighboring cells
        for ny, nx in self.neighboring_cells(y, x, len(grid)):
            self.find_all_words(ny, nx, grid, words_set, prefix_set, next_word, visited, solutions)

        visited[y][x] = False

    # helper method to calculate neighboring cells according to Boggle rules
    @staticmethod
    def neighboring_cells(y, x, size):
        neighbors = []
        # loops through all possible directions
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                # skips the current cell
                if dy == 0 and dx == 0:
                    continue
                # calculates new coordinates
                ny, nx = y + dy, x + dx
                # checks if the new coordinates are within bounds and handles edge cases
                if 0 <= ny < size and 0 <= nx < size:
                    neighbors.append((ny, nx))
        return neighbors

def main():
    grid = [["A", "B", "C", "D"], ["E", "F", "G", "H"], ["Ie", "J", "K", "L"], ["A", "B", "C", "D"]]
    dictionary = ["ABEF", "AFJIEB", "DGKD", "DGKA"]

    mygame = Boggle(grid, dictionary)
    solutions = mygame.getSolution()

    print("Grid:\n",mygame.grid)
    print("Dictionary:\n",mygame.dictionary)
    print("Solutions:", solutions)

if __name__ == "__main__":
    main()
