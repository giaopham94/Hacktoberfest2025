import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))

def bellman_ford(graph, src):
    V = graph.V
    dist = [float('inf')] * V
    dist[src] = 0
    for _ in range(V - 1):
        for u in range(V):
            for v, w in graph.graph[u]:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
    for u in range(V):
        for v, w in graph.graph[u]:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                return None
    return dist

def dijkstra(graph, src):
    V = graph.V
    dist = [float('inf')] * V
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph.graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist

def johnsons_algorithm(graph):
    V = graph.V
    new_graph = Graph(V + 1)
    for u in range(V):
        for v, w in graph.graph[u]:
            new_graph.add_edge(u, v, w)
    for v in range(V):
        new_graph.add_edge(V, v, 0)
    h = bellman_ford(new_graph, V)
    if h is None:
        return None
    reweighted_graph = Graph(V)
    for u in range(V):
        for v, w in graph.graph[u]:
            reweighted_graph.add_edge(u, v, w + h[u] - h[v])
    result = []
    for u in range(V):
        d = dijkstra(reweighted_graph, u)
        for v in range(V):
            d[v] += h[v] - h[u]
        result.append(d)
    return result

# Example usage
g = Graph(4)
g.add_edge(0, 1, 1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, -3)
g.add_edge(1, 3, 2)
g.add_edge(2, 3, 3)

distances = johnsons_algorithm(g)
for row in distances:
    print(row)
