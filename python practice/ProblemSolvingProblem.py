#!/bin/python3

import os
import sys

#
# Complete the problemSolving function below.
#
def problemSolving(k, v):
    # Write your code here.
    #v.sort()
    print (v, k)
    days=1
    i=0
    prev_number=(-1)
    while v!=[] :
        if i==0 and prev_number==(-1) :
            prev_number=v[i]
            v.pop(i)
        #elif i == 1 and len(v)==1 :
        elif i == len(v):
            i = 0
            prev_number = (-1)
            days += 1
        elif abs(v[i]-prev_number)>=k :
            prev_number = v[i]
            v.pop(i)
        else :
            i += 1
        #if v==[] :
            #count+=1
        print(v, prev_number)
        print('i'+str(i))
        print('lenV'+str(len(v)))
    print('count'+str(days))
    return days

if __name__ == '__main__':
    t = int(input())
    for i in range(t) :
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])
        v = list(map(int, input().rstrip().split()))
        result = problemSolving(k, v)
        print(str(result) + '\n')
