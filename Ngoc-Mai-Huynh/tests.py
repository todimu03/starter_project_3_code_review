import unittest
from boggle_solver import Boggle


class TestBoggleSolver(unittest.TestCase):
    """
    Test Frames (Category Partition style, summarized):
    1) Valid small grid, valid dictionary, at least one word found
    2) Valid grid, empty dictionary -> no words
    3) Valid grid, dictionary words < 3 letters -> no words
    4) Adjacency includes diagonals
    5) Cannot reuse the same tile in a single word path
    6) Multi-letter tiles (e.g., "Qu", "St", "Ie")
    7) Duplicate dictionary entries -> solution should not duplicate (set-like behavior)
    8) Different grid sizes (2x2, 4x4)
    9) Invalid grid shapes (non-square) -> []
    10) Invalid grid contents (non-strings / empty strings) -> []
    11) Dictionary is not a list -> []
    12) Using setters after construction works
    """


    def test_valid_2x2_finds_word(self):
        grid = [["A", "B"],
                ["C", "D"]]
        dictionary = ["A", "B", "AC", "ACA", "ACB", "DE"]
        game = Boggle(grid, dictionary)
        sol = game.getSolution()
        # Expect only "ACB" works (A->C->B via adjacency rules)
        self.assertEqual(sol, ["ACB"])


    def test_empty_dictionary_returns_empty(self):
        grid = [["A", "B"],
                ["C", "D"]]
        dictionary = []
        game = Boggle(grid, dictionary)
        self.assertEqual(game.getSolution(), [])


    def test_words_under_3_letters_ignored(self):
        grid = [["A", "B"],
                ["C", "D"]]
        dictionary = ["A", "AB", "BC", "CD", "DA"]  # all < 3
        game = Boggle(grid, dictionary)
        self.assertEqual(game.getSolution(), [])


    def test_diagonal_adjacency(self):

        grid = [["A", "X"],
                ["X", "D"]]
        dictionary = ["ADX"] 

        game = Boggle(grid, dictionary)
        self.assertEqual(game.getSolution(), ["ADX"])

    
    def test_cannot_reuse_tile(self):

        grid = [["A", "B"],
                ["C", "D"]]
        dictionary = ["AAA", "ABA", "ACA"]
        game = Boggle(grid, dictionary)
        
        self.assertEqual(game.getSolution(), [])


    def test_multi_letter_tile_qu(self):

        grid = [["Qu", "A"],
                ["R",  "T"]]
        dictionary = ["QUART", "QUA", "QAT", "QUAR"]  

        game = Boggle(grid, dictionary)
        sol = game.getSolution()
        self.assertIn("QUART", sol)
        self.assertIn("QUA", sol)
        self.assertIn("QUAR", sol)
        self.assertNotIn("QAT", sol)

    
    def test_multi_letter_tile_st(self):
        grid = [["St", "O"],
                ["N",  "T"]]
        dictionary = ["STONT", "STON", "STOT", "TONS"]

        game = Boggle(grid, dictionary)
        sol = game.getSolution()
        self.assertIn("STONT", sol)
        self.assertIn("STON", sol)
        self.assertIn("STOT", sol)
        self.assertNotIn("TONS", sol)

    
    def test_dictionary_duplicates(self):
        grid = [["A", "B"],
                ["C", "D"]]
        dictionary = ["ACB", "acb", "ACB", "AcB"]
        game = Boggle(grid, dictionary)
        sol = game.getSolution()
        # Should only contain one instance of ACB (solver normalizes to uppercase)
        self.assertEqual(sol, ["ACB"])

 
    def test_valid_4x4_examples(self):
        grid = [["A",  "B", "C", "D"],
                ["E",  "F", "G", "H"],
                ["IE", "J", "K", "L"],
                ["A",  "B", "C", "D"]]
        dictionary = ["ABEF", "AFJIEEB", "DGKD", "DGKA"]
        game = Boggle(grid, dictionary)
        sol = game.getSolution()
 
        self.assertIn("ABEF", sol)
        self.assertIn("AFJIEEB", sol)
        self.assertIn("DGKD", sol)
        self.assertNotIn("DGKA", sol)


    def test_invalid_grid_non_square(self):
        grid = [["A", "B", "C"],
                ["D", "E", "F"]]
        dictionary = ["ABC", "DEF"]
        game = Boggle(grid, dictionary)
        self.assertEqual(game.getSolution(), [])


    def test_invalid_grid_empty(self):
        grid = []
        dictionary = ["ANY"]
        game = Boggle(grid, dictionary)
        self.assertEqual(game.getSolution(), [])

 
    def test_invalid_grid_bad_cells(self):
        grid1 = [["A", ""],
                 ["C", "D"]]   
        grid2 = [["A", None],
                 ["C", "D"]] 
        dictionary = ["ACD"]
        self.assertEqual(Boggle(grid1, dictionary).getSolution(), [])
        self.assertEqual(Boggle(grid2, dictionary).getSolution(), [])


    def test_invalid_dictionary_type(self):
        grid = [["A", "B"],
                ["C", "D"]]
        dictionary = "ABCD" 
        game = Boggle(grid, dictionary)
        self.assertEqual(game.getSolution(), [])


    def test_setters_update_game(self):
        game = Boggle([["A"]], ["AAA"])
        # Now set to a valid grid and dictionary that should find something
        game.setGrid([["A", "B"],
                      ["C", "D"]])
        game.setDictionary(["ACB"])
        self.assertEqual(game.getSolution(), ["ACB"])


if __name__ == "__main__":
    unittest.main()