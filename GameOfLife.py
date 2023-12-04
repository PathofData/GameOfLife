import numpy as np
from scipy.signal import convolve2d

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from PIL import Image


class GameOfLife:
    def __init__(self, board_size, initial_probability, file_name, input_file=None, gradient_mag=0.2, random_seed=1):
        self.board_size = board_size
        self.initial_probability = initial_probability
        self.random_seed = random_seed
        self.input_file = input_file
        self.gradient_mag = gradient_mag
        self.file_name = file_name

    def read_image(self):
        # Read the image
        image = Image.open(self.input_file).convert('L')
        width, height = image.size

        # Resize the image if it's bigger than the specified dimensions
        if (width > self.board_size) or (height > self.board_size):
            image.thumbnail((self.board_size, self.board_size))

        image_array = np.asarray(image)

        # Initialize a gradient kernel
        scharr = np.array([[-3 - 3j, 0 - 10j, +3 - 3j],
                           [-10 + 0j, 0 + 0j, +10 + 0j],
                           [-3 + 3j, 0 + 10j, +3 + 3j]])  # Gx + j*Gy
        grad = convolve2d(image_array, scharr, boundary='symm', mode='same')

        # Compute the Magnitude
        grad = np.absolute(grad)

        # Scale the gradients to [0, 1]
        grad /= grad.max()

        # Threshold values to binary outcomes
        grad = np.where(grad >= self.gradient_mag, 1, 0)

        return grad
        
    def generate_board(self):
        if self.input_file:
            return self.read_image()
        else:
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

        def update(frame):
            nonlocal board_map
            if frame > 0:
                board_map = self.update_board(board_map)
            img.set_data(board_map)
            return [img]

        print("Compiling the frames to video format...")
        animated_board = FuncAnimation(
            fig,
            update,
            frames=n_generations,
            blit=True,
            interval=100,
            repeat_delay=1000
        )
        plt.close()

        print(f"Saving animation as: {self.file_name}")
        animated_board.save(self.file_name)
