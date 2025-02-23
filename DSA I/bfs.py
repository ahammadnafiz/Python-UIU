class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)

    def bfs(self, start_vertex):
        visited = set()

        queue = Queue()

        visited.add(start_vertex)
        queue.enqueue(start_vertex)

        traversal = []

        while not queue.is_empty():
            current_vertex = queue.dequeue()
            traversal.append(current_vertex)

            for neighbor in self.graph.get(current_vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.enqueue(neighbor)

        return traversal

def main():
    # Create a sample graph
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    
    print("BFS starting from vertex 0:")
    result = g.bfs(0)
    print(result)

if __name__ == "__main__":
    main()
