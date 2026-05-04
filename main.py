import pygame
from config import *
from grid import create_grid
from astar import a_star
from visualizer import init_screen, draw_grid

def main():
    screen = init_screen()
    grid = create_grid()

    start = None
    goal = None

    running = True

    while running:
        draw_grid(screen, grid)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                r, c = y // CELL_SIZE, x // CELL_SIZE

                if not start:
                    start = (r,c)
                    grid[r][c] = 2
                elif not goal:
                    goal = (r,c)
                    grid[r][c] = 3
                else:
                    grid[r][c] = 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and goal:
                    a_star(grid, start, goal,
                           lambda: draw_grid(screen, grid))

                if event.key == pygame.K_r:
                    grid = create_grid()
                    start, goal = None, None

    pygame.quit()

if __name__ == "__main__":
    main()