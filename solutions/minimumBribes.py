def minimumBribes(q):
    bribes_count = 0
    for i in range(len(q)):
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return
        for j in range(max(q[i] - 2, 0), i):
            if q[j] > q[i]:
                bribes_count += 1
    print(bribes_count)


minimumBribes([1, 2, 5, 3, 7, 8, 6, 9, 4])
