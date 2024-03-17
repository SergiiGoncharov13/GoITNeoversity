import uuid
import heapq

import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Additional argument to store the color of the node
        self.id = str(uuid.uuid4())  #  Unique identifier for each node

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  #  Using id and saving the value of a node
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def build_heap_tree(arr, i, n):
    if i < n:
        node = Node(arr[i])
        if 2 * i + 1 < n:
            node.left = build_heap_tree(arr, 2 * i + 1, n)
        if 2 * i + 2 < n:
            node.right = build_heap_tree(arr, 2 * i + 2, n)
        return node
    return None


def draw_heap(heap_root):
    heap = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    heap = add_edges(heap, heap_root, pos)

    colors = [node[1]['color'] for node in heap.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in heap.nodes(data=True)}  # Use node values for labels

    plt.figure(figsize=(8, 5))
    nx.draw(heap, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


if __name__ == "__main__":
    # Create heap
    arr = [9, 2, 4, 6, 22, 11, 7, 9, 4, 2, 1, 3, 14, 17, 13]
    heapq.heapify(arr)
    heap_root = build_heap_tree(arr, 0, len(arr))

    # Show heap
    draw_heap(heap_root)