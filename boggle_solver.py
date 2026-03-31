class Boggle:
  def __init__(self, grid, dictionary):
      self.grid = grid
      self.dictionary = dictionary
      self.solutions = []

  def getSolution(self):
  # Check input parameters are not empty
    if not self.grid:
      return []

    if not self.dictionary and len(self.grid) != 1:
      return []

  # Check if dictionary is valid
    if not isinstance(self.dictionary, list):
      return []

  # Check grid is NxN
    n = len(self.grid)
    for row in self.grid:
    # Check if row is a list and matches the height (n)
      if not isinstance(row, list) or len(row) != n:
        return []

  # Setup Data
    self.n = n
    self.upper_grid = [[str(cell).upper() for cell in row] for row in self.grid]
    self.dict_set = set(word.upper() for word in self.dictionary)

  # Create prefix set for efficiency
    self.prefixes = set()
    for word in self.dict_set:
      for i in range(len(word)):
        self.prefixes.add(word[:i+1])
        
    self.solution_set = set()

  # Iterate over the grid
    for y in range(n):
      for x in range(n):
        visited = [[False for _ in range(n)] for _ in range(n)]
        self.find_all_words(y, x, "", visited)

  # Get solution from Solution set
    return sorted(list(self.solution_set))    

  def find_all_words(self, y, x, current_word, visited):
    # Check Base Case
    if y < 0 or y >= self.n or x < 0 or x >= self.n or visited[y][x]:
      return

    new_word = current_word + self.upper_grid[y][x]

    # Check if the new word is a prefix for any word in the fast dictionary****
    if new_word not in self.prefixes:
      return
      
    # If Word in Dictionary, save to solution set
    if new_word in self.dict_set and len(new_word) >= 3:
      self.solution_set.add(new_word)

    #Continue searching using the adjacent tiles
    #Unmark location y, x as visited
    visited[y][x] = True
    for dy in [-1, 0, 1]:
      for dx in [-1, 0, 1]:
        if dy == 0 and dx == 0: continue
        self.find_all_words(y + dy, x + dx, new_word, visited)
    visited[y][x] = False
  

def main():
    grid = [["T", "W", "Y", "R"], 
            ["E", "N", "P", "H"],
            ["G", "Z", "Qu", "R"],
            ["O", "N", "T", "A"]]

    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry", "qua", "quart", "quartz", "rat", "tar", "tarp", "ten", "went", "wet", "arty", "rhr", "not", "quar"]
    
    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())

if __name__ == "__main__":
  main()