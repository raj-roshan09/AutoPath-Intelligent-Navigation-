import random

def create_grid(rows, cols, obstacle_prob=0.2):
    grid = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if random.random() < obstacle_prob:
                grid[i][j] = 1  # obstacle

    grid[0][0] = 0
    grid[rows-1][cols-1] = 0

    return grid
