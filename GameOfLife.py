import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from tqdm import tqdm


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
    def alive_neighbors(board_map: np.ndarray, x: int, y: int) -> int:
        return np.sum(board_map[x-1:x+2, y-1:y+2] == 1) - np.sum(board_map[x, y] == 1)

    def update_board(self, board_map):
        new_board = board_map.copy()
        board_x_max, board_y_max = board_map.shape
        for i in range(board_x_max):
            for j in range(board_y_max):
                n_neighbors = self.alive_neighbors(board_map, i, j)
                
                # Rule 2
                if (board_map[i, j] == 1) and (n_neighbors in [2, 3]):
                    new_board[i, j] = 1
                
                # Rule 1,3
                if (board_map[i, j] == 1) and ((n_neighbors > 3) or (n_neighbors < 2)):
                    new_board[i, j] = 0
                # Rule 4
                if (board_map[i, j] == 0) and (n_neighbors == 3):
                    new_board[i, j] = 1
        return new_board

    def run_simulation(self, n_generations):
        board_map = self.generate_board()
        
        fig = plt.figure()
        frames = [[plt.imshow(board_map, vmin=0, vmax=1, animated=True)]]
        for _ in tqdm(range(n_generations)):
            board_map = self.update_board(board_map=board_map)
            frames.append([plt.imshow(board_map, vmin=0, vmax=1, animated=True)])
            
        plt.axis('off')
        plt.grid(None)
        animated_board = animation.ArtistAnimation(
            fig,
            frames,
            interval=100,
            blit=True,
            repeat_delay=1000
        )
        plt.close()
        animated_board.save(self.file_name)
