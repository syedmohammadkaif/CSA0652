# Smart Public Transport Scheduling Optimization
# Greedy + Dijkstra Graph Algorithm

import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(
                    pq,
                    (distance, neighbor)
                )

    return distances


# Input
n = int(input("Enter number of stations/stops: "))
e = int(input("Enter number of routes: "))

graph = {}

for i in range(n):
    station = input(f"Enter station {i+1}: ")
    graph[station] = []

print("\nEnter Route Information")
print("Format: Source Destination Travel_Time")

for i in range(e):
    u, v, w = input(f"Route {i+1}: ").split()
    w = int(w)

    graph[u].append((v, w))
    graph[v].append((u, w))

start = input("\nEnter starting station: ")

distances = dijkstra(graph, start)

print("\nShortest Travel Times:")

for station, dist in distances.items():
    print(f"{start} -> {station} = {dist}")

# Greedy Scheduling
demand_routes = []

m = int(input("\nEnter number of route demands: "))

print("Format: Route_Name Passenger_Demand")

for i in range(m):
    route, demand = input(f"Demand {i+1}: ").split()
    demand = int(demand)

    demand_routes.append((route, demand))

demand_routes.sort(key=lambda x: x[1], reverse=True)

print("\nPriority Scheduling (Greedy):")

for route, demand in demand_routes:
    print(f"{route} : {demand} passengers")
