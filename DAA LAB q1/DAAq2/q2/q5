def find_intersection_values(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    answer1 = 0
    for num in nums1:
        if num in set2:
            answer1 += 1

    answer2 = 0
    for num in nums2:
        if num in set1:
            answer2 += 1

    return [answer1, answer2]


n = int(input("Enter size of nums1: "))
nums1 = list(map(int, input("Enter elements of nums1: ").split()))

m = int(input("Enter size of nums2: "))
nums2 = list(map(int, input("Enter elements of nums2: ").split()))

result = find_intersection_values(nums1, nums2)
print("Result:", result)
