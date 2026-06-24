def approximate_max_cut(vertices, edges):

    A = set()
    B = set()

    adjacency = {v: [] for v in vertices}

    for u, v in edges:
        adjacency[u].append(v)
        adjacency[v].append(u)

    for v in vertices:

        edges_to_A = 0
        edges_to_B = 0

        for neighbor in adjacency[v]:

            if neighbor in A:
                edges_to_A += 1

            elif neighbor in B:
                edges_to_B += 1

        if edges_to_A > edges_to_B:
            B.add(v)
        else:
            A.add(v)

    cut_edges = []

    for u, v in edges:

        if (u in A and v in B) or (u in B and v in A):
            cut_edges.append((u, v))

    return A, B, cut_edges


# Input
n = int(input("Enter number of vertices: "))

vertices = list(range(1, n + 1))

m = int(input("Enter number of edges: "))

edges = []

print("Enter edges (u v):")

for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))

A, B, cut_edges = approximate_max_cut(vertices, edges)

print("\nPartition A =", A)
print("Partition B =", B)

print("\nCut Edges:")

for edge in cut_edges:
    print(edge)

print("\nApproximate Cut Size =", len(cut_edges))