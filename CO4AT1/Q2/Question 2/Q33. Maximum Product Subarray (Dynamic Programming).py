def max_product_subarray(arr):
    max_ending_here = arr[0]
    min_ending_here = arr[0]
    max_so_far = arr[0]

    for i in range(1, len(arr)):
        current = arr[i]

        if current < 0:
            max_ending_here, min_ending_here = min_ending_here, max_ending_here

        max_ending_here = max(current, max_ending_here * current)
        min_ending_here = min(current, min_ending_here * current)

        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


# Input
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter array elements: ").split()))

# Output
print("Max Product =", max_product_subarray(arr))
