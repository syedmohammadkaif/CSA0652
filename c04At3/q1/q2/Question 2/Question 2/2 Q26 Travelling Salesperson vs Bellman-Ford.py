# TSP using Dynamic Programming (Held-Karp)
# Bellman-Ford Shortest Path

def tsp_dp(graph):
    n = len(graph)

    memo = {}

    def solve(mask, pos):

        if mask == (1 << n) - 1:
            return graph[pos][0]

        if (mask, pos) in memo:
            return memo[(mask, pos)]

        ans = float('inf')

        for city in range(n):
            if (mask & (1 << city)) == 0:
                new_cost = graph[pos][city] + solve(mask | (1 << city), city)
                ans = min(ans, new_cost)

        memo[(mask, pos)] = ans
        return ans

    return solve(1, 0)


def bellman_ford(vertices, edges, source):

    dist = [float('inf')] * vertices
    dist[source] = 0

    for _ in range(vertices - 1):
        for u, v, w in edges:

            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    return dist


# Input for TSP
n = int(input("Enter number of cities: "))

print("Enter adjacency matrix:")

graph = []
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

# Input for Bellman Ford
v = int(input("\nEnter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []

print("Enter edges (u v weight):")
for _ in range(e):
    u, vv, w = map(int, input().split())
    edges.append((u, vv, w))

source = int(input("Enter source vertex: "))

# Processing
tsp_result = tsp_dp(graph)
bf_result = bellman_ford(v, edges, source)

# Output
print("\n----- RESULT -----")
print("TSP Minimum Tour Cost =", tsp_result)

print("\nBellman-Ford Shortest Distances:")
for i in range(v):
    print(f"Vertex {i} -> {bf_result[i]}")
