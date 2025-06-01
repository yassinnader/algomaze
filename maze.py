class Cell:
    def __init__(self, row, col, is_wall=False):
        self.row = row
        self.col = col
        self.is_wall = is_wall

    def __lt__(self, other):
        if self.row == other.row:
            return self.col < other.col
        return self.row < other.row

    def __eq__(self, other):
        return isinstance(other, Cell) and self.row == other.row and self.col == other.col

    def __hash__(self):
        return hash((self.row, self.col))


class Maze:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[Cell(r, c) for c in range(cols)] for r in range(rows)]
        self.start = self.grid[0][0]
        self.end = self.grid[rows - 1][cols - 1]

    def generate_random_maze(self, wall_prob=0.3):
        from random import random
        for row in self.grid:
            for cell in row:
                if cell != self.start and cell != self.end:
                    cell.is_wall = random() < wall_prob

    def generate_maze(self, wall_prob=0.3):
        # Alias for compatibility with GUI code
        self.generate_random_maze(wall_prob)

    def display(self):
        for row in self.grid:
            line = ""
            for cell in row:
                if cell == self.start:
                    line += "S "
                elif cell == self.end:
                    line += "E "
                elif cell.is_wall:
                    line += "# "
                else:
                    line += ". "
            print(line)

    def get_neighbors(self, cell):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = []
        for dr, dc in directions:
            r, c = cell.row + dr, cell.col + dc
            if 0 <= r < self.rows and 0 <= c < self.cols:
                neighbors.append(self.grid[r][c])
        return neighbors