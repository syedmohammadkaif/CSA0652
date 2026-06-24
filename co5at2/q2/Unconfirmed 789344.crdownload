def combination_sum(arr, k, target):
    result = []

    def backtrack(start, current, current_sum):

        # Pruning
        if current_sum > target:
            return

        if len(current) == k:
            if current_sum == target:
                result.append(current[:])
            return

        for i in range(start, len(arr)):
            current.append(arr[i])

            backtrack(
                i + 1,
                current,
                current_sum + arr[i]
            )

            current.pop()

    backtrack(0, [], 0)

    return result


# Input
n = int(input("Enter number of elements: "))

arr = list(map(int, input("Enter elements: ").split()))

k = int(input("Enter combination size k: "))

target = int(input("Enter target sum: "))

ans = combination_sum(arr, k, target)

print("\nValid Combinations:")

for comb in ans:
    print(comb)

print("\nTotal Combinations =", len(ans))