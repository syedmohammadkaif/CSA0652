# E-Learning Content Recommendation Optimization
# Graph + Ranking Algorithm

from collections import defaultdict

def page_rank(graph, iterations=20, damping=0.85):
    nodes = list(graph.keys())
    n = len(nodes)

    rank = {node: 1 / n for node in nodes}

    for _ in range(iterations):
        new_rank = {}

        for node in nodes:
            rank_sum = 0

            for other in nodes:
                if node in graph[other]:
                    rank_sum += rank[other] / len(graph[other])

            new_rank[node] = (1 - damping) / n + damping * rank_sum

        rank = new_rank

    return rank


# Input Section
students = int(input("Enter number of students: "))
contents = int(input("Enter number of learning contents: "))

graph = defaultdict(list)

print("\nEnter interactions (Student -> Content)")
print("Format: Student Content")

for i in range(students):
    s, c = input(f"Interaction {i+1}: ").split()
    graph[s].append(c)

# Ensure content nodes exist
for content in range(1, contents + 1):
    graph[f"C{content}"] = []

# Calculate ranking
ranks = page_rank(graph)

print("\nContent Ranking Scores:")
for node, score in sorted(ranks.items(),
                          key=lambda x: x[1],
                          reverse=True):
    print(f"{node} : {score:.4f}")

print("\nTop Recommended Contents:")
recommendations = [node for node in ranks if node.startswith("C")]
recommendations = sorted(recommendations,
                         key=lambda x: ranks[x],
                         reverse=True)

for rec in recommendations[:3]:
    print(rec)
