import sys


def hourglassSum(arr):
    maxim = -sys.maxsize - 1
    for i in range(len(arr) - 2):
        for j in range(len(arr) - 2):
            # print(i, ",", j)
            sums = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i+2][j + 2]
            # print(f"{arr[i][j]} + {arr[i][j + 1]} + {arr[i][j + 2]} + {arr[i + 1][j + 1]} + {arr[i + 2][j]} + {arr[i + 2][j + 1]} + {arr[i+2][j + 2]}")
            # print(sums)
            if sums > maxim:
                maxim = sums
    # print(maxim)
    return maxim


hourglassSum(
    [[-9, -9, -9, 1, 1, 1],
     [0, -9, 0, 4, 3, 2],
     [-9, -9, -9, 1, 2, 3],
     [0, 0, 8, 6, 6, 0],
     [0, 0, 0, -2, 0, 0],
     [0, 0, 1, 2, 4, 0]])
