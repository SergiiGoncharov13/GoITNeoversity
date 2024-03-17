import heapq

def dijkstra(graph, source):
    # Initialize distance array
    n = len(graph)
    distance = [float('inf')] * n
    distance[source] = 0
    
    # Initialize priority queue (binary heap)
    pq = [(0, source)]
    
    while pq:
        dist_u, u = heapq.heappop(pq)
        
        # Check if the current distance is already outdated
        if dist_u > distance[u]:
            continue
        
        # Relax edges
        for v, weight in graph[u]:
            if distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                heapq.heappush(pq, (distance[v], v))
    
    return distance

# Example usage:
# Create a graph as an adjacency list (vertex: [(adjacent vertex, weight), ...])
graph = {
    0: [(1, 4), (2, 2)],
    1: [(2, 5), (3, 10)],
    2: [(3, 3)],
    3: [(4, 7)],
    4: []
}
source_vertex = 0
shortest_distances = dijkstra(graph, source_vertex)
print("Shortest distances from source vertex to all other vertices:")
print(shortest_distances)
