import numpy as np

# Define vertices and initialize adjacency matrix
vertices = [1, 2, 3, 4, 5]
n = len(vertices)
adj_matrix = np.zeros((n, n), dtype=int)
print("Initial Adjacency Matrix:\n", adj_matrix)

# Map each vertex to an index
vertex_to_index = {vertex: idx for idx, vertex in enumerate(vertices)}
print("Vertex to Index Mapping:", vertex_to_index)

# Define the edges (no need to repeat undirected edges)
edges = [
    (1, 2),
    (1, 4),
    (2, 3),
    (2, 4),
    (3, 4),
    (3, 5),
    (4, 5)
]

# Create adjacency matrix
for edge in edges:
    i, j = vertex_to_index[edge[0]], vertex_to_index[edge[1]]
    adj_matrix[i][j] = 1
    adj_matrix[j][i] = 1  # Since the graph is undirected

print("Adjacency Matrix after adding edges:\n", adj_matrix)

# Create adjacency list
adj_list = {vertex: [] for vertex in vertices}
for edge in edges:
    # Add each edge only once for an undirected graph
    adj_list[edge[0]].append(edge[1])
    adj_list[edge[1]].append(edge[0])

# Print adjacency list
print("\nAdjacency List:")
for vertex, neighbors in sorted(adj_list.items()):
    print(f"{vertex}: {neighbors}")
