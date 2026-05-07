from queue import PriorityQueue
from config import *

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_neighbors(grid, node):

    r, c = node

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    neighbors = []

    for dr, dc in directions:

        nr = r + dr
        nc = c + dc

        if 0 <= nr < ROWS and 0 <= nc < COLS:

            if grid[nr][nc] != 1:
                neighbors.append((nr, nc))

    return neighbors


def reconstruct_path(came_from, current, grid, draw):

    path_length = 0

    while current in came_from:

        current = came_from[current]

        if grid[current[0]][current[1]] not in [2, 3]:
            grid[current[0]][current[1]] = 5

        path_length += 1

        draw()

    print("\n===================")
    print("PATH FOUND")
    print("Path Length:", path_length)
    print("===================\n")


def a_star(grid, start, goal, draw):

    print("\n========== A* START ==========\n")

    open_set = PriorityQueue()
    open_set.put((0, start))

    came_from = {}

    g_score = {start: 0}

    step = 0

    while not open_set.empty():

        current = open_set.get()[1]

        current_g = g_score[current]
        current_h = heuristic(current, goal)
        current_f = current_g + current_h

        print(f"\nSTEP {step}")
        print("----------------------")
        print(f"CURRENT NODE : {current}")
        print(f"g(n) = {current_g}")
        print(f"h(n) = {current_h}")
        print(f"f(n) = {current_f}")

        step += 1

        if current == goal:

            print("\nGOAL REACHED!")

            reconstruct_path(
                came_from,
                goal,
                grid,
                draw
            )

            return True

        neighbors = get_neighbors(grid, current)

        print(f"NEIGHBORS : {neighbors}")

        for neighbor in neighbors:

            temp_g = g_score[current] + 1

            h = heuristic(neighbor, goal)

            f = temp_g + h

            print(f"\nChecking Neighbor: {neighbor}")
            print(f"g = {temp_g}")
            print(f"h = {h}")
            print(f"f = {f}")

            if neighbor not in g_score or temp_g < g_score[neighbor]:

                came_from[neighbor] = current
                g_score[neighbor] = temp_g

                open_set.put((f, neighbor))

                if grid[neighbor[0]][neighbor[1]] not in [2, 3]:
                    grid[neighbor[0]][neighbor[1]] = 4

        draw()

    print("\nNO PATH FOUND\n")

    return False