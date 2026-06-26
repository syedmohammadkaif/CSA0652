def find_paths(m, n, N, i, j):
    memo = {}

    def dfs(x, y, steps):
        if x < 0 or x >= m or y < 0 or y >= n:
            return 1

        if steps == 0:
            return 0

        if (x, y, steps) in memo:
            return memo[(x, y, steps)]

        memo[(x, y, steps)] = (
            dfs(x + 1, y, steps - 1) +
            dfs(x - 1, y, steps - 1) +
            dfs(x, y + 1, steps - 1) +
            dfs(x, y - 1, steps - 1)
        )

        return memo[(x, y, steps)]

    return dfs(i, j, N)


print(find_paths(2, 2, 2, 0, 0))

print(find_paths(1, 3, 3, 0, 1))
