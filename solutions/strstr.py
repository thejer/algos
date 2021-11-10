# class Solution:
from builtins import range, len


def str_str(haystack, needle):
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i + len(needle)] == needle:
            return i
    return -1


print(str_str("mississippi", "issip"))
