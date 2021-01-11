def twoStrings(s1, s2):
    s1_dict = {}
    for i in s1:
        s1_dict[i] = 1
    for i in s2:
        if i in s1_dict:
            return "YES"
    return "NO"

# Problem https://www.hackerrank.com/challenges/two-strings/problem
