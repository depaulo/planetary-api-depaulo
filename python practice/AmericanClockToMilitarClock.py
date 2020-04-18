#!/bin/python3

import os
import sys


#
# Complete the timeConversion function below.
#
def timeConversion(s) :
    # Write your code here.
    s_list = list(s)
    if len(s_list) == 8 :
        hour = s_list[0 :2]
        minute = s_list[3 :5]
        seconds = s_list[6 :]
        for i in range(len(s)) :
            return ''

    elif len(s_list) == 10 :
        hour = s_list[0] + s_list[1]
        minute = s_list[3] + s_list[4]
        seconds = s_list[6] + s_list[7]
        day_or_night = s_list[8] + s_list[9]
        if day_or_night == 'PM' and hour == '12' :
            hour = hour
        elif day_or_night == 'PM' and hour < '12' :
            hour = list(str(int(hour) + 12))
        elif day_or_night == 'AM' and hour == '12' :
            hour = '00'
        elif day_or_night == 'AM' and hour < '12' :
            hour = hour
        seq = (''.join(hour) + ':' + ''.join(minute) + ':' + ''.join(seconds))
        return (seq)
    else :
        print('You typed it wront, try again.')
        return ''


if __name__ == '__main__' :
    s = ['07:05:45PM','12:15:55AM']
    for i in range(len(s)) :
        result = timeConversion(s[i])
        print(result + '\n')

