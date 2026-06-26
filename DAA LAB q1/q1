def first_palindrome(words):
    for word in words:
        if word == word[::-1]:
            return word
    return ""

n = int(input("Enter number of words: "))

words = []
for i in range(n):
    words.append(input(f"Enter word {i + 1}: "))

result = first_palindrome(words)
print("First palindromic string:", result)
