def cyclic_rotation(A, K):
    new_arr = A.copy()
    N = len(A)
    if N == 0:
        return A
    if K > N:
        K = K % N
    if K == N:
        return A
    for i in range(N):
        new_index = (-1 - ((N - 1) - (i + K)))
        if new_index < 0:
            new_index += N
        new_arr[new_index] = A[i]
    return new_arr


print(cyclic_rotation([3, 8, 9, 7, 6], 3))