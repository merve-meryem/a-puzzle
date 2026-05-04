import heapq
from grid import get_neighbors

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, goal, draw_callback):
    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_score = {start: 0}

    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == goal:
            reconstruct_path(came_from, current, grid, draw_callback)
            return True

        for neighbor in get_neighbors(current, grid):
            temp_g = g_score[current] + 1

            if neighbor not in g_score or temp_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g

                f = temp_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f, neighbor))

                if grid[neighbor[0]][neighbor[1]] not in (2,3):
                    grid[neighbor[0]][neighbor[1]] = 4

        draw_callback()

    return False

def reconstruct_path(came_from, current, grid, draw_callback):
    while current in came_from:
        current = came_from[current]
        if grid[current[0]][current[1]] not in (2,3):
            grid[current[0]][current[1]] = 5
        draw_callback()