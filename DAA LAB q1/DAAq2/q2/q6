def sum_counts(nums):
    n = len(nums)
    total_sum = 0

    for i in range(n):
        distinct_elements = set()

        for j in range(i, n):
            distinct_elements.add(nums[j])
            count = len(distinct_elements)
            total_sum += count * count

    return total_sum


n = int(input("Enter the size of the array: "))
nums = list(map(int, input("Enter the elements: ").split()))

result = sum_counts(nums)
print("Sum of squares of distinct counts:", result)
