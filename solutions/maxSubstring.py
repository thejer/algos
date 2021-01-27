def max_substring(s):
    n = len(s)
    maximum = ""
    for i in range(n):
        maximum = max(maximum, s[i:])
    return maximum


print(max_substring("a"))
