import time

def print_maze(maze, path=None):
    """
    Print the maze in the console in a clear way.
    maze: 2D list (0=path, 1=wall).
    path: list of coordinates (row, col) representing the solution path.
    """
    for i, row in enumerate(maze):
        line = ""
        for j, cell in enumerate(row):
            if path and (i, j) in path:
                line += "🟩"  # Path location
            elif cell == 1:
                line += "⬛"  # Wall
            else:
                line += "⬜"  # Path
        print(line)

def path_to_coords(path):
    """
    Converts a list of Cell objects to a list of coordinates (row, col).
    Each cell must have row and col attributes.
    """
    return [(cell.row, cell.col) for cell in path]

def time_it(func):
    """
    Decorator to measure the execution time of a function.
    Usage:
    @time_it
    def some_function(...):
        ...
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.4f} seconds")
        return result
    return wrapper