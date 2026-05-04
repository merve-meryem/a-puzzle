from config import ROWS, COLS

def create_grid():
    return [[0 for _ in range(COLS)] for _ in range(ROWS)]

def get_neighbors(node, grid):
    r, c = node
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    
    result = []
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        
        if 0 <= nr < ROWS and 0 <= nc < COLS:
            if grid[nr][nc] != 1:
                result.append((nr, nc))
    
    return result