def optimal_solution(s1, s2):
    map1 = {}
    map2 = {}

    for i, s in enumerate(s1):
        if s in map1:
            v = map1.get(s)
            map1[s] = v + 1
        else:
            map1[s] = 1

    for i, s in enumerate(s2):
        if s in map2:
            v = map2.get(s)
            map2[s] = v + 1
        else:
            map2[s] = 1

    total = 0
    keys1 = map1.keys()
    keys2 = map2.keys()

    keys_a = keys1 if len(keys1) > len(keys2) else keys2
    keys_b = keys2 if len(keys1) > len(keys2) else keys1

    for i in keys_a:
        if i in keys_b:
            total += map1[i] if map1[i] < map2[i] else map2[i]

    print(total)


def bad_solution(s1, s2):
    c = len(s1) if len(s1) < len(s2) else len(s2)
    total = 0
    for i in range(c):
        if s1[i] == s2[i]:
            total = total + 1
    print(total)


def solution():
    test_cases = int(input())
    for i in range(test_cases):
        s1 = input()
        s2 = input()
        bad_solution(s1, s2)


solution()