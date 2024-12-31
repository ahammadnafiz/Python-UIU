import numpy as np 

vertices = ['A', 'B', 'C', 'D', 'E', 'F']
n = len(vertices)
adj_matrix = np.zeros((n, n), dtype=int)
print("Initial Adjacency Matrix:\n", adj_matrix)

# map each vertex to an index 
vertex_to_index = {vertex:idx for idx, vertex in enumerate(vertices)}
print("Vertex to Index Mapping:", vertex_to_index)

# define the edges (only need to define one direction since it's undirected)
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'C'),
    ('B', 'D'),
    ('C', 'F'),
    ('D', 'E'),
    ('E', 'F')
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
