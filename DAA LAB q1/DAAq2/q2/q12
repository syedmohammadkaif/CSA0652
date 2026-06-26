def binary_search(arr, key):
    arr.sort()   

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid + 1   
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


arr = [3, 4, 6, -9, 10, 8, 9, 30]
key = int(input("Enter key: "))

pos = binary_search(arr, key)

if pos != -1:
    print(f"Element {key} is found at position {pos}")
else:
    print(f"Element {key} is not found")
