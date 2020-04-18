#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr) :
    # Write your code here
    sum_diagonal1 = 0
    sum_diagonal2 = 0
    for i in range(len(arr)) :
        sum_diagonal1 += arr[i][i]
        sum_diagonal2 += arr[i][len(arr)-(i+1)]
    return abs(sum_diagonal1-sum_diagonal2)


if __name__ == '__main__' :
    n = int(input().strip())

    arr = []

    for _ in range(n) :
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(str(result) + '\n')

