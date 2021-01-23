from collections import Counter

"""
Problem: https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?
PS: This problem made me question my existence
"""


def sherlockAndAnagrams(s):
    anagram_dict = (Counter("".join(sorted(s[i: j])) for i in range(len(s))
                            for j in range(i + 1, len(s) + 1)))
    anagram_dict = {k: v for k, v in anagram_dict.items() if v > 1}
    return sum(sum(range(i)) for i in anagram_dict.values())


print(sherlockAndAnagrams("##(($*!@)"))
