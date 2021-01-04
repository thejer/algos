
def badSegment(badNumbers, lower, upper):
    a = badNumbers
    a.sort()
    i = 0
    while a[i] <= lower:
        i += 1

    l = lower
    diff = float('-inf')
    while i < len(a) and a[i] <= upper:
        diff = max((a[i] - l), diff)
        l = a[i] + 1
        i += 1

    if a[-1] < upper:
        diff = max((upper - (a[-1])), diff)

    return diff