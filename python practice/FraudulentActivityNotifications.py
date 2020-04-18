#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
def counting_sort(expenditure) :
    # The main function that sort the given string arr[] in
    # alphabetical order

        # The output character array that will have sorted arr
        output = [0 for i in range(2560)]

        # Create a count array to store count of inidividul
        # characters and initialize count array as 0
        count = [0 for i in range(2560)]

        # For storing the resulting answer since the
        # string is immutable
        ans = ["" for _ in expenditure]

        # Store count of each character
        for i in expenditure :
            count[i] += 1

        # Change count[i] so that count[i] now contains actual
        # position of this character in output array
        for i in range(2560) :
            count[i] += count[i - 1]

            # Build the output character array
        for i in range(len(expenditure)) :
            output[count[(expenditure[i])] - 1] = expenditure[i]
            count[(expenditure[i])] -= 1

        # Copy the output array to arr, so that arr now
        # contains sorted characters
        for i in range(len(expenditure)) :
            ans[i] = output[i]
        return ans

def mediana(expenditure, d, i) :
    middle = (float(d)/2)
    expenditure2=counting_sort(expenditure[(i-d+1):(i+1)])
    print(expenditure2)
    if middle % 2 != 0:
        return ((expenditure2[int(middle - 0.5)]))
    else:
        return ((expenditure2[int(middle)]+expenditure2[int(middle-1)])/2)


def activityNotifications(expenditure, d):
    notifications=0
    for i in range(len(expenditure)-2) :
        if (i+1 >= d) and (expenditure[i+1]>=((mediana(expenditure, d, i))*2)) :
            print(mediana(expenditure, d, i)*2)
            notifications+=1
    return notifications


if __name__ == '__main__':
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    expenditure = list(map(int, input().rstrip().split()))
    result = activityNotifications(expenditure, d)
    print(str(result) + '\n')