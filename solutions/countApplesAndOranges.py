def countApplesAndOranges(s, t, a, b, apples, oranges):
    newapples = sorted(apples)[::-1]
    neworanges = sorted(oranges)
    noap = 0
    noor = 0

    for i in newapples:
        if i < 0:
            break
        if i + a in range(s, t + 1):
            noap += 1


    for i in neworanges:
        if i > 0:
            break
        if i + b in range(s, t + 1):
            noor += 1

    print(noap)
    print(noor)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
