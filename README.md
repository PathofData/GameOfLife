# GameOfLife
An optimised implementation of Conway's Game of Life.

The Algorithm uses scipy's fast vectorised convolutions approach to calculate the next state.

The final video is compiled using the ffmpeg library.

# Usage
Import the main class which will initialize a random map with the specified parameters:

`board_size`: Controls the size of the 2 dimesional grid

`initial_probability`: The probability of the alive cells in the grid

`random_seed`: A seed integer for the random generator

`file_name`: The name of the resulting file where the simulation is saved

```python
game_round = GameOfLife(
    board_size=128,
    initial_probability=0.1,
    random_seed=1,
    file_name='movie.mp4'
)
```

Then run the simulation with a specified number of generations:

`n_generations`: Select the number of generations in the run (loops)

```python
game_round.run_simulation(n_generations=500)
```
