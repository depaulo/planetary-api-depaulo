#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the staircase function below.
def staircase(n) :
    arr = ['']
    for i in range(n) :
        arr.append([])
    for i in range(n) :
        arr[i] += (' ' * (n - (i + 1)))
        arr[i] += ('#' * (i + 1))
    for i in range(n) :
        print(''.join(arr[i]))


if __name__ == '__main__' :
    n = int(input().strip())

    staircase(n)