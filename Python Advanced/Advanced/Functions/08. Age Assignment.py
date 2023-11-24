#todo 9.Recursion palindrome

def palindrome(word,idx):
    word1=list(reversed(word))
    if word==word1:
        return f"{word} is a palindrome"
    return f"{word} is not a palindrome"

print(palindrome("abcba", 0))