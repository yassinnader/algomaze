from maze import Maze
from solver import Solver
from utils import print_maze, path_to_coords, time_it


def main():
    print("Welcome to Maze Solver!")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    print("\n🧱 Generated Maze:\n")
    maze = Maze(rows, cols)
    maze.generate_random_maze()
    
    maze.display()

    print("\nChoose solving algorithm:")
    print("1. Solve using BFS")
    print("2. Solve using DFS")
    print("3. Solve using Dijkstra")

    choice = input("Choose option: ")

    solver = Solver(maze)
    if choice == "1":
        solver.solve_bfs()
    elif choice == "2":
        solver.solve_dfs()
    elif choice == "3":
        solver.solve_dijkstra()
    else:
        print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
