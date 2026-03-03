"""NAME: Joseph Neisen  SID: 004003010"""

class HashTable:
    def __init__(self, size):
        """Constructor"""
        self.size = size
        self.array = [None] * self.size
        self.amount_filled = 0

    def hashFunction(self, key, probe):
        """Hash function that uses quadratic probing, key is a string"""
        value = 0
        for char in key:
            value += ord(char)
        return (value + probe * probe) % self.size

    def add(self, key, value):
        """Adds a new value to the hash table, if this value already exists it keeps the greater of the two values"""
        if(float(self.amount_filled) / float(self.size) > 0.7):
            self.rehash(self.size * 2)

        # hash table preserves the greater value if given a duplicate key
        present = self.find(key)
        if(present is not None):
            if(present is not value and present < value):
                self.replace(key, value)
                return
        
        done = False
        place = self.hashFunction(key, 0)
        probe = 0
        
        while(not done):
            if(self.array[place] == None):
                self.array[place] = (key, value)
                self.amount_filled += 1
                return
            # use quadratic probing for collisions
            else:
                probe += 1
                place = self.hashFunction(key, probe)

    def rehash(self, new_size):
        """Rehashes the hash table with a new size"""
        # remake the array at the new size, then add all of the previous (key, value) pairs
        new_array = [None] * new_size
        temp = self.array
        self.array = new_array
        self.size = new_size
        for i in temp:
            if(i is not None):
                self.add(i[0], i[1])

    def find(self, key):
        """Finds the value to the given key"""
        place = self.hashFunction(key, 0)
        done = False
        probe = 0

        while(not done):
            if(self.array[place] is None):
                return None
            if(self.array[place][0] == key):
                return self.array[place][1]
            probe += 1
            place = self.hashFunction(key, probe)

    def replace(self, key, new_value):
        """Replaces the value of the given key with a new value"""
        place = self.hashFunction(key, 0)
        done = False
        probe = 0

        while(not done):
            if(self.array[place] is None):
                return
            if(self.array[place][0] == key):
                self.array[place] = (key, new_value)
                return
            probe += 1
            place = self.hashFunction(key, probe)

class Boggle:

    def __init__(self, grid, dictionary):
        """Constructor"""
        self.grid = grid
        self.hashTable = HashTable(10)
        self.initialize_hash_table(dictionary)

    def lowercase(self, word):
        """Returns lowercase word"""
        capital_letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        difference = ord('a') - ord('A')
        new_word = str()
        for i in range(len(word)):
            if(word[i] in capital_letters):
                new_word += chr(ord(word[i]) + difference)
            else:
                new_word += word[i]
        return new_word
    
    def initialize_hash_table(self, dictionary):
        """Initializes the hashTable off the given dictionary"""
        if not hasattr(dictionary, '__iter__'):
            self.hashTable = None
            return
        for i in dictionary:
            if(type(i) is not str):
                self.hashTable = None
                return
            if(len(i) < 3):
              continue
            word = self.lowercase(i)
            for j in range(1, len(word)):
                self.hashTable.add(word[:j], 0)
            self.hashTable.add(word, 1)

    def set_grid(self, new_grid):
        """set the Boggle grid"""
        self.grid = new_grid

    def set_dictionary(self, new_dictionary):
        """reset up the hashtable of possible words"""
        self.initializeHashTable(new_dictionary)

    def getSolution(self):
        """return the list of dictionary words in the grid"""
        # invalid types
        if(type(self.grid) is not list or type(self.grid[0]) is not list or self.hashTable == None):
            return []
        # turn every letter lowercase
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                self.grid[i][j] = self.lowercase(self.grid[i][j])
        
        solved_list = set()
        # check that the grid is valid
        if len(self.grid) == 0:
          return solved_list

        if len(self.grid) != len(self.grid[0]):
          return solved_list

        special_valid_cases = ['st', 'ie', 'qu']
        special_invalid_cases = ['s', 'i', 'q']
        a_to_z = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        for i in self.grid:
           for j in i:
               if (not j in a_to_z) and (not j in special_valid_cases) or (j in special_invalid_cases):
                   return solved_list  

        # solve the grid using the solve method
        current_word = ""
        # check every starting letter in the grid
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])) :
                self.solve(self.grid[i][j], (i, j), [(i, j)], solved_list)
        return solved_list
                
    def solve(self, word, last_place, used_tiles, solved_list):
        """recursive method to find words in the Boggle board using DFS"""
        adjacent_letters = self.get_adjacent_letters(last_place, used_tiles)

        # continue if there are possible words from the valid_words that it could still be
        if not self.check_substring(word, solved_list):
            return
        
        # if there are no unused adjacencies, abandon this path
        if(len(adjacent_letters) == 0):
           return
        
        # loop through all possible remaining paths
        for i in range(len(adjacent_letters)):
            next_letter = adjacent_letters[i]

            new_word = word + self.grid[next_letter[0]][next_letter[1]]

            # duplicate the used tiles without reference to have each part of the tree have its own bucket of used tiles
            temp_used_tiles = []
            for tile in used_tiles:
                temp_used_tiles.append(tile)
            
            temp_used_tiles.append(next_letter)

            self.solve(new_word, next_letter, temp_used_tiles, solved_list)

    def get_adjacent_letters(self, place, used_tiles):
        """get the coordinates of adjacent unused letters"""
        i = place[0]
        j = place[1]
        return_list = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                if(x == 0 and y == 0):
                    continue
                if( i + x < len(self.grid) and i + x >= 0
                and j + y < len(self.grid[0]) and j + y >= 0):
                    if(i + x, j + y) not in used_tiles:
                        return_list.append((i + x, j + y))
                    
        return return_list

    def check_substring(self, string, solved_list):
        """check if the string is a prefix of words in valid_words return true if valid prefix or actual word"""
        hash_table_value = self.hashTable.find(string)
        if hash_table_value == 1:
            # adds words that are in the dictionary
            solved_list.add(string)
            return True
        elif hash_table_value == 0:
            return True
        else:
            return False

def main():
    grid = [['A', 'B'], ['C', 'D']]
    dictionary = ['quest', 'stew', 'abd', 'strew', 'cbad']
    
    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())

if __name__ == "__main__":
    main()
