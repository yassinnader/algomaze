import tkinter as tk
from maze import Maze
from solver import Solver
from utils import path_to_coords

CELL_SIZE = 20

class MazeApp:
    def __init__(self, master):
        self.master = master
        master.title("Maze Solver")

        self.rows, self.cols = 15, 20
        self.maze = Maze(self.rows, self.cols)

        self.canvas = tk.Canvas(master, width=self.cols * CELL_SIZE, height=self.rows * CELL_SIZE, bg="white")
        self.canvas.pack()

        self.generate_btn = tk.Button(master, text="Generate Maze", command=self.generate_maze)
        self.generate_btn.pack(side=tk.LEFT, padx=5, pady=5)

        self.solve_btn = tk.Button(master, text="Solve Maze", command=self.solve_maze)
        self.solve_btn.pack(side=tk.LEFT, padx=5, pady=5)

        self.algorithm_var = tk.StringVar(master)
        self.algorithm_var.set("Dijkstra")
        algo_menu = tk.OptionMenu(master, self.algorithm_var, "Dijkstra", "DFS")
        algo_menu.pack(side=tk.LEFT, padx=5, pady=5)

        self.status_label = tk.Label(master, text="", fg="red")
        self.status_label.pack(side=tk.LEFT, padx=10)

        self.draw_maze()

    def draw_maze(self, path=None):
        self.canvas.delete("all")
        grid = self.maze.grid
        for i in range(self.rows):
            for j in range(self.cols):
                x1 = j * CELL_SIZE
                y1 = i * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                color = "black" if grid[i][j].is_wall else "white"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")
        if path:
            for (x, y) in path:
                x1 = y * CELL_SIZE
                y1 = x * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="green", outline="green")
        self._draw_start_goal()

    def _draw_start_goal(self):
        # Start cell (top-left)
        x1 = 0
        y1 = 0
        x2 = CELL_SIZE
        y2 = CELL_SIZE
        self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="blue")
        # Goal cell (bottom-right)
        x1 = (self.cols - 1) * CELL_SIZE
        y1 = (self.rows - 1) * CELL_SIZE
        x2 = x1 + CELL_SIZE
        y2 = y1 + CELL_SIZE
        self.canvas.create_rectangle(x1, y1, x2, y2, fill="red", outline="red")

    def generate_maze(self):
        self.maze.generate_maze()
        self.status_label.config(text="")
        self.draw_maze()

    def solve_maze(self):
        solver = Solver(self.maze)
        algo = self.algorithm_var.get()
        if algo == "Dijkstra":
            path = solver.solve_dijkstra()
        else:
            path = solver.solve_dfs()
        if path and len(path) > 0:
            coords = path_to_coords(path)
            self.status_label.config(text="Path found!", fg="green")
            self.draw_maze(path=coords)
        else:
            self.status_label.config(text="No path found!", fg="red")
            self.draw_maze()

if __name__ == "__main__":
    root = tk.Tk()
    app = MazeApp(root)
    root.mainloop()