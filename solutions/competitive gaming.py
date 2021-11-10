def numPlayers(k, scores):
    num = 1
    scores = sorted(scores)[::-1]
    print(scores)
    for i in range(1, len(scores)):
        if scores[i - 1] == scores[i] or num < k:
            num += 1
        else:
            return num
    return num


# print(numPlayers(4, [2,2,3,4,5]))


def segment(x, space):
    # Write your code here
    segments = []
    for i in range(0, len(space)):
        if x > len(space):
            break
        segments.append(space[i:(x+1)])
        print(segments)
    minimums = {}
    for i in range(len(segments)):
        print(segments[i])
    return max(minimums)

skills = []

print(segment(1, [1,2,3,1,2]))
