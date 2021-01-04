import os

def rotLeft(a, d):
    n = len(a)
    if d > n:
        d = d % n
    newa = [0]*n
    for i in range(0, n):
        newi = (i - d)
        if newi < 0:
            newi = n + newi
        newa[newi] = a[i]
    return newa

print(rotLeft([3, 8, 9, 7, 6], 3))