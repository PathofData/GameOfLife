import unittest
import numpy as np
from game_of_life import GameOfLife  # Assuming your class is in game_of_life.py


class TestGameOfLife(unittest.TestCase):
    def setUp(self):
        self.board_size = 10
        self.initial_probability = 0.5
        self.file_name = "test_output.mp4"
        self.game = GameOfLife(self.board_size, self.initial_probability, self.file_name)

    def test_initialization(self):
        self.assertEqual(self.game.board_size, 10)
        self.assertEqual(self.game.initial_probability, 0.5)
        self.assertEqual(self.game.file_name, "test_output.mp4")

    def test_generate_board(self):
        board = self.game.generate_board()
        self.assertEqual(board.shape, (self.board_size, self.board_size))
        # Further tests can include checking the proportion of 1s and 0s based on initial_probability

    def test_alive_neighbors(self):
        test_board = np.array([[0, 1, 0],
                               [1, 1, 1],
                               [0, 1, 0]])
        neighbors = self.game.alive_neighbors(test_board)
        expected_neighbors = np.array([[5, 4, 5],
                                       [4, 4, 4],
                                       [5, 4, 5]])
        np.testing.assert_array_equal(neighbors, expected_neighbors)

    def test_update_board(self):
        test_board = np.array([[0, 0, 1],
                               [1, 0, 0],
                               [0, 0, 1]])
        updated_board = self.game.update_board(test_board)
        expected_board = np.array([[1, 1, 1],
                                   [1, 1, 1],
                                   [1, 1, 1]])
        np.testing.assert_array_equal(updated_board, expected_board)
        

if __name__ == "__main__":
    unittest.main()
