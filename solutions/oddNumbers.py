def oddNumbers(l, r):
    oddities = []
    for i in range(l, r + 1):
        if i % 2 != 0:
            oddities.append(i)
    return oddities


print(oddNumbers(3, 9))
