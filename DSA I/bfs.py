import numpy as np 
from collections import deque

vertices = ['R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']
n = len(vertices)
adj_matrix = np.zeros((n, n), dtype=int)
print("Initial Adjacency Matrix:\n", adj_matrix)

# map each vertex to an index 
vertex_to_index = {vertex:idx for idx, vertex in enumerate(vertices)}
print("Vertex to Index Mapping:", vertex_to_index)

# define the edges (only need to define one direction since it's undirected)
edges = [
    ('R', 'S'),
    ('R', 'V'),
    ('S', 'W'),
    ('W', 'T'),
    ('W', 'X'),
    ('T', 'X'),
    ('T', 'W'),
    ('T', 'U'),
    ('X', 'W'),
    ('X', 'T'),
    ('X', 'Y'),
    ('Y', 'X'),
    ('Y', 'U')

]

# Create adjacency matrix (undirected)
for edge in edges:
    i, j = vertex_to_index[edge[0]], vertex_to_index[edge[1]]
    adj_matrix[i][j] = 1
    adj_matrix[j][i] = 1  # Since the graph is undirected

print("Adjacency Matrix after adding edges:\n", adj_matrix)

# Creating adjacency lists (undirected)
adj_list = {vertex: [] for vertex in vertices}
for edge in edges:
    # Add both directions since the graph is undirected
    adj_list[edge[0]].append(edge[1])
    adj_list[edge[1]].append(edge[0])

print("\nAdjacency List:")
for vertex, neighbors in sorted(adj_list.items()):
    print(f"{vertex}: {neighbors}")

def bfs(adj_matrix, start_vertex, vertex_to_index):
    visited = [False] * len(vertices)
    queue = deque()

    # Initialize bfs
    start_index = vertex_to_index[start_vertex]
    visited[start_index] = True
    queue.append(start_index)

    bfs_order = []

    while queue:
        current_index = queue.popleft()
        current_vertex = vertices[current_index]
        bfs_order.append(current_vertex)
        print(f"Visited: {current_vertex}")

        # Iterate through neighbors
        for neighbor_index, is_connected in enumerate(adj_matrix[current_index]):
            if is_connected and not visited[neighbor_index]:
                visited[neighbor_index] = True
                queue.append(neighbor_index)
                print(f"Enqueued: {vertices[neighbor_index]}")

    return bfs_order

# Example usage
start_vertex = 'S'
print(f"\nPerforming BFS starting from vertex '{start_vertex}':")
bfs_result = bfs(adj_matrix, start_vertex, vertex_to_index)
print("\nBFS Traversal Order:", bfs_result)
