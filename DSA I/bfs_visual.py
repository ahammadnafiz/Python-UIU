import queue
import networkx as nx
import matplotlib.pyplot as plt


def order_bfs(graph, start_node):
    visited = set()
    q = queue.Queue()
    q.put(start_node)
    order = []

    while not q.empty():
        vertex = q.get()
        if vertex not in visited:
            order.append(vertex)
            visited.add(vertex)

            for node in graph[vertex]:
                if node not in visited:
                    q.put(node)
