import heapq
from collections import deque

class Solver:
    def __init__(self, maze):
        self.maze = maze
        self.start = maze.start
        self.end = maze.end

    def reconstruct_path(self, parents, current):
        """Reconstructs the path from start to end using the parent pointers."""
        path = []
        while current in parents:
            path.append(current)
            current = parents[current]
        path.append(current)  # Add the start node
        path.reverse()
        return path

    def solve_bfs(self):
        """Solves the maze using Breadth-First Search (BFS)."""
        queue = deque([self.start])
        visited = set()
        parents = {}

        while queue:
            current = queue.popleft()
            if current == self.end:
                return self.reconstruct_path(parents, current)
            if current in visited:
                continue
            visited.add(current)
            for neighbor in self.maze.get_neighbors(current):
                if neighbor not in visited and not neighbor.is_wall and neighbor not in parents:
                    queue.append(neighbor)
                    parents[neighbor] = current
        return []

    def solve_dfs(self):
        """Solves the maze using Depth-First Search (DFS)."""
        stack = [self.start]
        visited = set()
        parents = {}

        while stack:
            current = stack.pop()
            if current == self.end:
                return self.reconstruct_path(parents, current)
            if current in visited:
                continue
            visited.add(current)
            for neighbor in self.maze.get_neighbors(current):
                if neighbor not in visited and not neighbor.is_wall and neighbor not in parents:
                    stack.append(neighbor)
                    parents[neighbor] = current
        return []

    def solve_dijkstra(self):
        """Solves the maze using Dijkstra's algorithm."""
        heap = []
        heapq.heappush(heap, (0, self.start))
        distances = {self.start: 0}
        parents = {}
        visited = set()

        while heap:
            dist, current = heapq.heappop(heap)
            if current == self.end:
                return self.reconstruct_path(parents, current)
            if current in visited:
                continue
            visited.add(current)
            for neighbor in self.maze.get_neighbors(current):
                if neighbor.is_wall or neighbor in visited:
                    continue
                new_dist = dist + 1  # Constant weight for each step
                if neighbor not in distances or new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    parents[neighbor] = current
                    heapq.heappush(heap, (new_dist, neighbor))
        return []
    
    def solve_astar(self):
        """Solves the maze using the A* algorithm."""
        import heapq
        open_set = []
        heapq.heappush(open_set, (0, self.start))
        g_score = {self.start: 0}
        f_score = {self.start: self.heuristic(self.start, self.end)}
        parents = {}
        visited = set()

        while open_set:
            _, current = heapq.heappop(open_set)
            if current == self.end:
                return self.reconstruct_path(parents, current)
            visited.add(current)
            for neighbor in self.maze.get_neighbors(current):
                if neighbor.is_wall or neighbor in visited:
                    continue
                tentative_g = g_score[current] + 1
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + self.heuristic(neighbor, self.end)
                    parents[neighbor] = current
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
        return []

    def heuristic(self, cell1, cell2):
        # Manhattan distance
        return abs(cell1.row - cell2.row) + abs(cell1.col - cell2.col)