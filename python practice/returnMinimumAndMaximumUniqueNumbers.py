def min_max(int_list) :
    d = {}
    res = []
    for i in int_list :
        if i not in d :
            d[i] = 1
        else :
            d[i] += 1
    for x, y in d.items() :
        if y == 1 :
            print(x)
            res.append(x)
    min_value = min(res)
    max_value = max(res)
    return (min_value, max_value)


if __name__ == '__main__' :
    int_list = [1, 2, 3, 4, 4, 5, 6, 2, 3, 4, 3, 9, 0, 0]
    result = min_max(int_list)
    print(result)


    def min_max(int_list) :
        int_list.sort()
        result = []
        for i in int_list :
            if int_list.count(i) == 1 :
                result.append(i)
        return (min(result), max(result))


    if __name__ == '__main__' :
        int_list = [1, 2, 3, 4, 4, 5, 6, 2, 3, 4, 3, 9, 0, 0]
        result = min_max(int_list)
        print(result)