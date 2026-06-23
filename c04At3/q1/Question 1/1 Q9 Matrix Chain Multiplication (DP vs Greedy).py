# Matrix Chain Multiplication (DP vs Greedy)

def matrix_chain_dp(dimensions):
    n = len(dimensions) - 1

    dp = [[0 for _ in range(n)] for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')

            for k in range(i, j):
                cost = (dp[i][k] +
                        dp[k + 1][j] +
                        dimensions[i] * dimensions[k + 1] * dimensions[j + 1])

                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[0][n - 1]


def matrix_chain_greedy(dimensions):
    dims = dimensions[:]
    total_cost = 0

    while len(dims) > 2:
        min_cost = float('inf')
        pos = 0

        for i in range(len(dims) - 2):
            cost = dims[i] * dims[i + 1] * dims[i + 2]

            if cost < min_cost:
                min_cost = cost
                pos = i

        total_cost += min_cost
        dims.pop(pos + 1)

    return total_cost


# Input
n = int(input("Enter number of matrices: "))

dimensions = []

print("Enter dimensions:")
for i in range(n):
    r = int(input(f"Rows of Matrix {i+1}: "))
    c = int(input(f"Columns of Matrix {i+1}: "))

    if i == 0:
        dimensions.append(r)

    dimensions.append(c)

# Processing
dp_cost = matrix_chain_dp(dimensions)
greedy_cost = matrix_chain_greedy(dimensions)

# Output
print("\n----- RESULT -----")
print("Dynamic Programming Cost =", dp_cost)
print("Greedy Cost =", greedy_cost)

if dp_cost == greedy_cost:
    print("Greedy matched the optimal solution for this input.")
else:
    print("Greedy failed to find the optimal solution.")
