def count_pairs(nums, k):
    n = len(nums)
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j] and (i * j) % k == 0:
                count += 1

    return count


n = int(input("Enter the size of the array: "))
nums = list(map(int, input("Enter the elements: ").split()))
k = int(input("Enter the value of k: "))

result = count_pairs(nums, k)
print("Number of valid pairs:", result)
