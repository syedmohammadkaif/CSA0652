def string_match(text, pattern):   
    n = len(text)
    m = len(pattern)
    if m == 0:
        return []
    matches = []
    for i in range(n - m + 1):
        for j in range(m):
            if text[i + j] != pattern[j]:
                break
        else:
            matches.append(i)
    return matches
text = input("Enter text: ")
pattern = input("Enter pattern: ")
result = string_match(text, pattern)
if result:
    print("Pattern found at positions:", result)
else:
    print("Pattern not found")