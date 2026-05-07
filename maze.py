import random
from config import *

def generate_maze(grid):
    stack = []

    start_row = 1
    start_col = 1

    grid[start_row][start_col] = 0
    stack.append((start_row, start_col))

    directions = [
        (-2,0),
        (2,0),
        (0,-2),
        (0,2)
    ]

    while stack:
        r, c = stack[-1]

        neighbors = []

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            if 1 <= nr < ROWS-1 and 1 <= nc < COLS-1:
                if grid[nr][nc] == 1:
                    neighbors.append((nr,nc,dr,dc))

        if neighbors:
            nr, nc, dr, dc = random.choice(neighbors)

            wall_r = r + dr//2
            wall_c = c + dc//2

            grid[wall_r][wall_c] = 0
            grid[nr][nc] = 0

            stack.append((nr,nc))
        else:
            stack.pop()

    return grid