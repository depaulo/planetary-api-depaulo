def ArrayCompare(arr,arr2) :
    arr.sort()
    arr2.sort()
    if len(arr) != len(arr2) :
        return False
    for i in range(len(arr)) :
        if arr[i] != arr2[i] :
            return False
    else :
        return True

if __name__ == '__main__' :
    arr = [1, 2, 5, 4, 0]
    arr2 = [2, 4, 5, 0, 1]
    arr3= [1, 2, 5, 4, 0, 2, 1]
    arr4= [2, 4, 5, 0, 1, 1, 2]
    arr5= [1, 7, 1]
    arr6= [7, 7, 1]
    arr7= [2, 3, 4, 5]
    arr8= [2, 3, 4]

    for i in ((arr, arr2),(arr3, arr4),(arr5, arr6),(arr7, arr8)) :
        if ArrayCompare(*i) :
            print('yes')
        else :
            print ('no')
