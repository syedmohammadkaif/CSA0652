import random
import time

# -----------------------------
# Lomuto Partition Quick Sort
# -----------------------------
lomuto_swaps = 0

def lomuto_partition(arr, low, high):
    global lomuto_swaps
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            lomuto_swaps += 1

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    lomuto_swaps += 1

    return i + 1

def quicksort_lomuto(arr, low, high):
    if low < high:
        pi = lomuto_partition(arr, low, high)
        quicksort_lomuto(arr, low, pi - 1)
        quicksort_lomuto(arr, pi + 1, high)

# -----------------------------
# Hoare Partition Quick Sort
# -----------------------------
hoare_swaps = 0

def hoare_partition(arr, low, high):
    global hoare_swaps

    pivot = arr[low]
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while arr[i] < pivot:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]
        hoare_swaps += 1

def quicksort_hoare(arr, low, high):
    if low < high:
        pi = hoare_partition(arr, low, high)
        quicksort_hoare(arr, low, pi)
        quicksort_hoare(arr, pi + 1, high)

# -----------------------------
# Performance Testing
# -----------------------------
sizes = [1000, 5000, 10000]

print("\nQUICK SORT PERFORMANCE ANALYSIS")
print("-" * 70)
print(f"{'Size':<10}{'Method':<15}{'Time(ms)':<15}{'Swaps':<15}")

for size in sizes:

    data = [random.randint(1, 100000) for _ in range(size)]

    arr1 = data.copy()
    lomuto_swaps = 0

    start = time.perf_counter()
    quicksort_lomuto(arr1, 0, len(arr1) - 1)
    lomuto_time = (time.perf_counter() - start) * 1000

    arr2 = data.copy()
    hoare_swaps = 0

    start = time.perf_counter()
    quicksort_hoare(arr2, 0, len(arr2) - 1)
    hoare_time = (time.perf_counter() - start) * 1000

    print(f"{size:<10}{'Lomuto':<15}{lomuto_time:<15.3f}{lomuto_swaps:<15}")
    print(f"{size:<10}{'Hoare':<15}{hoare_time:<15.3f}{hoare_swaps:<15}")

print("-" * 70)
