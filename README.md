# GameOfLife
An optimised implementation of Conway's Game of Life.

The Algorithm uses scipy's fast vectorised convolutions approach to calculate the next state.

The final video is compiled using the ffmpeg library.

# Usage
The board can be initialized with a user defined image or a random sequence. This image can then be used as is if it's binary valued
or a gradient based preprocessing is applied to binarize it.

Import the main class which will initialize a random map with the specified parameters:

`board_size`: Controls the size of the 2 dimesional grid

`initial_probability`: The probability of the alive cells in the grid

`random_seed`: A seed integer for the random generator

`file_name`: The name of the resulting file where the simulation is saved

`input_file`: The name of the input image to read as board map

`gradient_mag`: The threshold of binarization for gradient-based preprocessing, values between 0 and 1. Must be greater than 0 in order to perform
binarization

```python
game_round = GameOfLife(
    board_size=128,
    initial_probability=0.1,
    random_seed=1,
    file_name='movie.mp4',
    input_file='your_picture.jpg',
    gradient_mag=0.2
)
```

Then run the simulation with a specified number of generations:

`n_generations`: Select the number of generations in the run (loops)

```python
game_round.run_simulation(n_generations=500)
```
