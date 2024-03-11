import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def dfs_iterative(graph, start_vertex):
    visited = set()
    stack = [start_vertex]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            stack.extend(reversed(graph[vertex]))


def bfs_iterative(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            queue.extend(set(graph[vertex]) - visited)

    return visited


def dijkstra_algorithm(graph, start_node):
    distances = {node: float('inf') for node in graph.nodes}
    distances[start_node] = 0
    visited = set()

    while len(visited) < len(graph.nodes):
        current_node = min(
            (node for node in graph.nodes if node not in visited), key=lambda x: distances[x])
        visited.add(current_node)

        for neighbor, weight in graph[current_node].items():
            potential_distance = distances[current_node] + weight['weight']
            if potential_distance < distances[neighbor]:
                distances[neighbor] = potential_distance

    return distances


G = nx.DiGraph()

G.add_node("Akademmistechko")
G.add_node("Zhytomyrska")
G.add_node("Sviatoshyn|")
G.add_node("Nyvky|")
G.add_node("Beresteiska")
G.add_node("Shuliavskal")
G.add_node("Politekhnichnyi Instytut")
G.add_node("Vokzalna")
G.add_node("Universytet")
G.add_node("Teatralna")
G.add_node("Khreschatyk")
G.add_node("Arsenalna")
G.add_node("Dnipro")
G.add_node("Hidropark")
G.add_node("Livoberezhna")
G.add_node("Darnytsia")
G.add_node("Chernihivska")
G.add_node("Lisoval")

G.add_edge("Akademmistechko", "Zhytomyrska", weight=1)
G.add_edge("Zhytomyrska", "Sviatoshyn", weight=1)
G.add_edge("Sviatoshyn", "Nyvky", weight=1)
G.add_edge("Nyvky", "Beresteiska", weight=1)
G.add_edge("Beresteiska", "Shuliavskal", weight=1)
G.add_edge("Shuliavskal", "Politekhnichnyi Instytut", weight=1)
G.add_edge("Politekhnichnyi Instytut", "Vokzalna", weight=1)
G.add_edge("Vokzalna", "Universytet", weight=1)
G.add_edge("Universytet", "Teatralna", weight=2)
G.add_edge("Teatralna", "Khreschatyk", weight=2)
G.add_edge("Khreschatyk", "Arsenalna", weight=1)
G.add_edge("Arsenalna", "Dnipro", weight=1)
G.add_edge("Dnipro", "Hidropark", weight=1)
G.add_edge("Hidropark", "Livoberezhna", weight=1)
G.add_edge("Livoberezhna", "Darnytsia", weight=1)
G.add_edge("Darnytsia", "Chernihivska", weight=1)
G.add_edge("Chernihivska", "Lisoval", weight=1)


pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()


# About Graph

# Кількість вершин і ребер
number_of_nodes = G.number_of_nodes()
number_of_edges = G.number_of_edges()

print(f"Кількість вершин: {number_of_nodes}")
print(f"Кількість ребер: {number_of_edges}")

# Ступінь вершин
degree_sequence = [G.degree(node) for node in G.nodes]
average_degree = sum(degree_sequence) / number_of_nodes

print(f"Ступінь вершин: {degree_sequence}")
print(f"Середній ступінь вершин: {average_degree}")

# DFS
dfs_paths = list(nx.dfs_edges(G, source="Akademmistechko"))

print("Алгоритм DFS:")
for path in dfs_paths:
    print(path)

# BFS 
bfs_paths = list(nx.bfs_edges(G, source="Akademmistechko"))

print("Алгоритм BFS:")
for path in bfs_paths:
    print(path)

# Виведення найкоротших шляхів між всіма вершинами
shortest_paths = nx.single_source_dijkstra_path(G, source="Akademmistechko")

print(f"Найкоротші шляхи між всіма вершинами: {shortest_paths}")