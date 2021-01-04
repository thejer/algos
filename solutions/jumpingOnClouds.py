#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    leng=len(c)
    steps=0
    index=0
    if leng <= 3:
        return 1
    while index!=leng-1:
        if index == leng-2:
            index+=1
            steps+=1
        elif c[index+2] == 0:
            index+=2
            steps+=1
        else:
            index+=1
            steps+=1
    return steps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
