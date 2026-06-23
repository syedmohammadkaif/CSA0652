# Educational Content Recommendation Sorting using Merge Sort

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        # Sort by recommendation score
        if left[i]["score"] >= right[j]["score"]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Course recommendation dataset
courses = [
    {"course": "Python Basics", "score": 92},
    {"course": "Machine Learning", "score": 98},
    {"course": "Data Structures", "score": 85},
    {"course": "AI Fundamentals", "score": 95},
    {"course": "Cloud Computing", "score": 88},
]

print("Original Course Rankings:")
for c in courses:
    print(c)

sorted_courses = merge_sort(courses)

print("\nRecommended Course Rankings:")
for c in sorted_courses:
    print(c)
