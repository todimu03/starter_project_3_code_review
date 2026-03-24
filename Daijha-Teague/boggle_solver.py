
class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = dictionary
        self.solutions = []
        self.pre_word_hash = {}

    def is_word(self, word):
        return self.pre_word_hash.get(word) == 1

    def is_prefix_or_word(self, word):
        return word in self.pre_word_hash

    def getSolution(self):
     
      n = len(self.grid)

  # GRID VALIDATION
  
       # check if grid and dictionary are empty 
      if not self.grid or not self.dictionary:
        return []
        

       #check if grid is a list or not 
      if not isinstance(self.grid, list):
        return []

      # check if the grid is NxN 
      for  row in self.grid:
          if not isinstance(row,list) or len(row) != n:
            return []

      # convert elements to alphabets and lower case
      for idx, row in enumerate(self.grid) :
        for jdx, x in enumerate(row):
          
      # checks that element is a string
          if not isinstance(x, str):
            return []

      #check that element is a alphabet
          if not x.isalpha():
            return []
      
        # check that any element greater than 1 is only our acceptable one
          if len(x) > 1 :
            if x.lower() == "qu" or x.lower() == "st" or x.lower() == "ie":
              pass
            else :
              return []
      
        # check for raw s, i, and q 
          else:
            if x.lower() == "q" or x.lower() == "s" or x.lower() == "i":
              return []
          

        # makes every element lowercase
          self.grid[idx][jdx] = x.lower()
          


# DICTIONARY VALIDATION
      

      # check that dictionary is a list  
      if not isinstance(self.dictionary, list):
        return []

      # check that every element is a str
      for x in self.dictionary:
        if not isinstance(x, str):
          return []
      # check that every dic item is only alphabets
        if not x.isalpha():
          return []
        
      # lowercase all elements 
        w = x.lower()
        
      

      
# FAST DICTIONARY (still in loop^^) 
      
      # add all prefixes 
        # 0 - prefix 1 - word
        for k in range(1, len(w) + 1):
          prefix = w[:k]
          if k == len(w):
            self.pre_word_hash[prefix]= 1
          else : 
            self.pre_word_hash.setdefault(prefix, 0)

    

    # SEARCH FOR THE WORDS (loop already exited)
      
      found = set()
      found_confirmed = set()

      #goes over every tile
      for r in range(n):
          for c in range(n):
              visited = [[False] * n for _ in range(n)] # sets every tile in the grids status as False
              self.find_all_words(r, c, "", visited, found) #recursive function
     
      print(found)
      
      for x in found:
        if len(x) >= 3 :
          found_confirmed.add(x)

      return found_confirmed



    def find_all_words(self, r, c, current, visited, found):
      n = len(self.grid)

      # check if its out of bounds
      if r < 0 or r >= n or c < 0 or c >= n:
          return

      # check if tile was already used
      if visited[r][c]:
          return

      # make the new string
      new_current = current + self.grid[r][c]

      # if no word starts with the same letter, stop
      if not self.is_prefix_or_word(new_current):
          return

      # mark it as visitied
      visited[r][c] = True
    

      # if its a word, then save it to the set of found words
      if self.is_word(new_current):
          found.add(new_current)

      # explore ALL neighbors
      for dr in (-1, 0, 1):
          for dc in (-1, 0, 1):
              if dr == 0 and dc == 0:
                  continue
              self.find_all_words(r + dr, c + dc, new_current, visited, found)

      # mark visited as false for the next tile
      visited[r][c] = False
      

def main():

  grid = [["A", "B", "C"],["D", "E", "F"],["G", "H", "I"]]
  dictionary = ["abc", "abdhi", "abi", "ef", "cfi", "dea"]
  mygame = Boggle(grid, dictionary)
  print(mygame.getSolution())

  
if __name__ == "__main__":
  main()
