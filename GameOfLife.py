import numpy as np
from scipy.signal import convolve2d

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class GameOfLife:
    def __init__(self, board_size, initial_probability, file_name, random_seed=1):
        self.board_size = board_size
        self.initial_probability = initial_probability
        self.random_seed = random_seed
        self.file_name = file_name
        
    def generate_board(self):
        np.random.seed(self.random_seed)
        return np.random.choice(
            a=[0, 1], 
            size=(self.board_size, self.board_size), 
            p=[1-self.initial_probability, self.initial_probability]
        )

    @staticmethod
    def alive_neighbors(board_map):
        kernel = np.array([[1, 1, 1],
                           [1, 0, 1],
                           [1, 1, 1]])
        return convolve2d(board_map, kernel, mode='same', boundary='wrap')

    def update_board(self, board_map):
        n_neighbors = self.alive_neighbors(board_map)

        # Applying the rules to the entire board
        born = (n_neighbors == 3) & (board_map == 0)
        survive = ((n_neighbors == 2) | (n_neighbors == 3)) & (board_map == 1)
        new_board = born | survive

        return new_board.astype(int)

    def run_simulation(self, n_generations):
        board_map = self.generate_board()

        # Initialize a figure for plotting
        fig, ax = plt.subplots()
        img = ax.imshow(board_map, vmin=0, vmax=1, animated=True)

        def init():
            img.set_data(board_map)
            return [img]

        def update(frame):
            nonlocal board_map
            board_map = self.update_board(board_map)
            img.set_data(board_map)
            return [img]

        print("Compiling the frames to video format...")
        animated_board = FuncAnimation(
            fig,
            update,
            init_func=init,
            frames=n_generations,
            blit=True,
            interval=100,
            repeat_delay=1000
        )
        plt.close()

        print(f"Saving animation as: {self.file_name}")
        animated_board.save(self.file_name)
