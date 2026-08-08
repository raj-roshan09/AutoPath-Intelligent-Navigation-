import numpy as np
import random

class ACO:
    def __init__(self, grid, ants=20, iterations=50, alpha=1, beta=2, evaporation=0.5):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.ants = ants
        self.iterations = iterations
        self.alpha = alpha
        self.beta = beta
        self.evaporation = evaporation

        self.pheromone = np.ones((self.rows, self.cols))

    def heuristic(self, x, y, goal):
        return 1.0 / (abs(goal[0]-x) + abs(goal[1]-y) + 1)

    def get_neighbors(self, x, y):
        moves = [(0,1),(1,0),(0,-1),(-1,0)]
        neighbors = []
        for dx, dy in moves:
            nx, ny = x+dx, y+dy
            if 0 <= nx < self.rows and 0 <= ny < self.cols:
                if self.grid[nx][ny] == 0:
                    neighbors.append((nx, ny))
        return neighbors

    def run(self, start, goal):
        best_path = None
        best_length = float('inf')

        for _ in range(self.iterations):
            all_paths = []

            for _ in range(self.ants):
                path = [start]
                visited = set([start])
                current = start

                while current != goal:
                    neighbors = self.get_neighbors(*current)
                    neighbors = [n for n in neighbors if n not in visited]

                    if not neighbors:
                        break

                    probs = []
                    for nx, ny in neighbors:
                        tau = self.pheromone[nx][ny] ** self.alpha
                        eta = self.heuristic(nx, ny, goal) ** self.beta
                        probs.append(tau * eta)

                    probs = np.array(probs)
                    probs /= probs.sum()

                    next_node = neighbors[np.random.choice(len(neighbors), p=probs)]
                    path.append(next_node)
                    visited.add(next_node)
                    current = next_node

                if current == goal:
                    all_paths.append(path)
                    if len(path) < best_length:
                        best_length = len(path)
                        best_path = path

            self.pheromone *= (1 - self.evaporation)

            for path in all_paths:
                for (x, y) in path:
                    self.pheromone[x][y] += 1.0 / len(path)

        return best_path
