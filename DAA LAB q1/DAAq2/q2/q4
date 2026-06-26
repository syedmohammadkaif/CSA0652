def rob_linear(nums):
    prev1 = 0
    prev2 = 0

    for money in nums:
        temp = max(prev1, prev2 + money)
        prev2 = prev1
        prev1 = temp

    return prev1


def rob(nums):
    if len(nums) == 1:
        return nums[0]

    return max(
        rob_linear(nums[:-1]),
        rob_linear(nums[1:])
    )


# Test Cases
print(rob([2, 3, 2]))
print(rob([1, 2, 3, 1]))
