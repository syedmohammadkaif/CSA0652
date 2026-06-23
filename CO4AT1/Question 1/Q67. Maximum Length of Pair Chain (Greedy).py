def max_chain_length(pairs):
    # Sort pairs based on second element
    pairs.sort(key=lambda x: x[1])

    count = 1
    last_end = pairs[0][1]

    for i in range(1, len(pairs)):
        if pairs[i][0] > last_end:
            count += 1
            last_end = pairs[i][1]

    return count


# Input
n = int(input("Enter number of pairs: "))

pairs = []
print("Enter pairs (a b):")
for _ in range(n):
    a, b = map(int, input().split())
    pairs.append((a, b))

# Output
print("Max Chain =", max_chain_length(pairs))
