def rotate_array(arr, num):
    new_arr = arr.copy()
    N = len(arr)
    if num > N:
        num = num - (N*(num//N))
    if num == N:
        return arr
    for i in range(N):
        new_index = -1 - ((N - 1) - (i + num))
        new_arr[new_index] = arr[i]
        print("{} is in {}".format(arr[i], new_index))
    return new_arr


print(rotate_array([3, 8, 9, 7, 6], 4))