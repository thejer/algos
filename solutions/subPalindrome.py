
def palindrome(s):
    palindromes = set()
    s = s.strip()
    if not s.isalnum():
        return 0
    else:
        for pivot in range(len(s)):
            print(pivot)
            find_palindromes(s, pivot, pivot, palindromes)
            find_palindromes(s, pivot, pivot + 1, palindromes)
    return palindromes


def find_palindromes(string, i, j, palindromes):
    while i >= 0 and j < len(string) and string[i] == string[j]:
        palindromes.add(string[i: j + 1])
        i -= 1
        j += 1


print(palindrome("aabbaa"))