# Online Advertisement Ranking using Quick Sort

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]["rank_score"]

    left = [x for x in arr if x["rank_score"] > pivot]
    equal = [x for x in arr if x["rank_score"] == pivot]
    right = [x for x in arr if x["rank_score"] < pivot]

    return quick_sort(left) + equal + quick_sort(right)

# Advertisement dataset
ads = [
    {"ad": "Laptop Sale", "rank_score": 85},
    {"ad": "Mobile Offer", "rank_score": 95},
    {"ad": "Online Course", "rank_score": 78},
    {"ad": "Insurance Plan", "rank_score": 92},
    {"ad": "Travel Package", "rank_score": 88},
]

print("Original Advertisement Rankings:")
for ad in ads:
    print(ad)

sorted_ads = quick_sort(ads)

print("\nRanked Advertisements:")
for ad in sorted_ads:
    print(ad)
