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

    #  feedback: incorporate checks for potental empty rows within the grid
    def getSolution(self):
        if not self.grid:
            return []

        if not self.dictionary:
            return []

    # validate rows
        for row in self.grid:
            if not row or not all(cell for cell in row):
                return []
        
        # formats the grid and dictionary 
        #  feedback: also account for any empty rows and we could also check that each row has the right number of columns
        format_grid = self.format_grid(self.grid)

        # Check if grid is empty after formatting
        if not format_grid:
            return []

        size = len(format_grid)

        # Validate rows: no empty rows + correct number of columns
        for row in format_grid:
            if not row or len(row) != size:
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
    # needs to handle edge cases such as non-string entries and empty strings in the dictionary; include a check for non alphabetical characters
    @staticmethod
    def format_grid(grid):
        formatted = [
            [str(cell).strip().upper() for cell in row if str(cell).strip().isalpha()]
            for row in grid if row
        ]
        return formatted if all(formatted) else []

    # feedback: same issue as format_grid, needs to handle edge cases such as non-string entries and empty strings in the dictionary; include a check for non alphabetical characters
    @staticmethod
    def format_dictionary(dictionary):
        return {
            word.strip().upper()
            for word in dictionary
            if isinstance(word, str)
            and word.strip()
            and word.strip().isalpha()
        }

    # helper method to create sets of words and prefixes
    def prefix_sets(self, words):
        words_set = set()
        prefix_set = set()
        for word in words:
            words_set.add(word)
            #double check the feedback for this
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
        for next_y, next_x in self.neighboring_cells(y, x, len(grid)):
            self.find_all_words(next_y, next_x, grid, words_set, prefix_set, next_word, visited, solutions)

        visited[y][x] = False

    # helper method to calculate neighboring cells according to Boggle rules
    # rename dy and dx to more descriptive names 
    @staticmethod
    def neighboring_cells(y, x, size):
        neighbors = []
        # loops through all possible directions
        for delta_y in (-1, 0, 1):
            for delta_x in (-1, 0, 1):
                # skips the current cell
                if delta_y == 0 and delta_x == 0:
                    continue
                # calculates new coordinates
                next_y, next_x = y + delta_y, x + delta_x
                # checks if the new coordinates are within bounds and handles edge cases
                if 0 <= next_y < size and 0 <= next_x < size:
                    neighbors.append((next_y, next_x))
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