import pygame
from config import *

def init_screen():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("A* Visualizer")
    return screen

def draw_grid(screen, grid):
    screen.fill(WHITE)

    for r in range(ROWS):
        for c in range(COLS):
            rect = (c*CELL_SIZE, r*CELL_SIZE, CELL_SIZE, CELL_SIZE)

            color = WHITE
            if grid[r][c] == 1:
                color = BLACK
            elif grid[r][c] == 2:
                color = GREEN
            elif grid[r][c] == 3:
                color = RED
            elif grid[r][c] == 4:
                color = BLUE
            elif grid[r][c] == 5:
                color = YELLOW

            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, (200,200,200), rect, 1)

    pygame.display.update()