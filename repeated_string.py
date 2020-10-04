#!/bin/python3

import os


# Complete the repeatedString function below.
def repeated_string(s, n):
    c = s.count("a")
    size = len(s)
    ratio = int(n / size)
    r = n % size
    num = (c * ratio) + s[0:r].count("a")
    return num


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeated_string(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
