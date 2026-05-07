import pygame

from config import *
from grid import create_grid
from maze import generate_maze
from astar import a_star
from visualizer import init_screen, draw_grid

def main():

    screen = init_screen()

    grid = create_grid()
    generate_maze(grid)

    start = None
    goal = None

    running = True

    while running:

        draw_grid(screen, grid)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            # SOL TIK -> START
            if pygame.mouse.get_pressed()[0]:

                x, y = pygame.mouse.get_pos()

                r = y // CELL_SIZE
                c = x // CELL_SIZE

                # duvar değilse
                if grid[r][c] != 1:

                    # eski start temizle
                    if start:
                        grid[start[0]][start[1]] = 0

                    start = (r, c)
                    grid[r][c] = 2

            # SAĞ TIK -> GOAL
            if pygame.mouse.get_pressed()[2]:

                x, y = pygame.mouse.get_pos()

                r = y // CELL_SIZE
                c = x // CELL_SIZE

                if grid[r][c] != 1:

                    if goal:
                        grid[goal[0]][goal[1]] = 0

                    goal = (r, c)
                    grid[r][c] = 3

            if event.type == pygame.KEYDOWN:

                # A*
                if event.key == pygame.K_SPACE:

                    if start and goal:

                        a_star(
                            grid,
                            start,
                            goal,
                            lambda: draw_grid(screen, grid)
                        )

                # RESET
                if event.key == pygame.K_r:

                    grid = create_grid()
                    generate_maze(grid)

                    start = None
                    goal = None

    pygame.quit()

if __name__ == "__main__":
    main()