def solution(N, A):
    # write your code in Python 3.6
    counters = [0] * N
    maxi = 0
    last_update = 0

    for i in range(len(A)):
        if A[i] <= N:
            position = A[i] - 1
            if counters[position] < last_update:
                counters[position] = last_update+1
            else:
                counters[position] += 1
            if counters[position] > maxi:
                maxi = counters[position]
        elif A[i] == N + 1:
            last_update = maxi

    for i in range(N):
        if counters[i] < last_update:
            counters[i] = last_update

    return counters

print(solution(5, [3,4,4,6,1,4,4]))