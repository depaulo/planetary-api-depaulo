#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the luckBalance function below.
def luckBalance(k, contests) :
    important_contests = []
    not_important_contests = []
    contests_won = []
    for x, y in contests :
        if y == 1 :
            important_contests.append(x)
        else :
            not_important_contests.append(x)

    for i in range(len(important_contests) - k) :
        contests_won.append(important_contests.pop(important_contests.index(min(important_contests))))

    return (sum(not_important_contests) + sum(important_contests) - sum(contests_won))


if __name__ == '__main__' :
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    contests = []
    for _ in range(n) :
        contests.append(list(map(int, input().rstrip().split())))
    result = luckBalance(k, contests)
    fptr.write(str(result) + '\n')
    fptr.close()
# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the luckBalance function below.
def luckBalance(k, contests) :
    important_contests = []
    not_important_contests = []
    contests_won = []
    for x, y in contests :#separate the contests in important and not important ones
        if y == 1 :
            important_contests.append(x)
        else :
            not_important_contests.append(x)

    for i in range(len(important_contests) - k) :#check the amount of times she needs to win, by subtracting total_important_contests from k
        contests_won.append(important_contests.pop(important_contests.index(min(important_contests))))

    return (sum(not_important_contests) + sum(important_contests) - sum(contests_won))


if __name__ == '__main__' :
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    contests = []
    for _ in range(n) :
        contests.append(list(map(int, input().rstrip().split())))
    result = luckBalance(k, contests)
    fptr.write(str(result) + '\n')
    fptr.close()
