def min_max(int_list) :
    for i in range(len(int_list)) :
        for j in range(0, len(int_list) - i - 1) :
            if int_list[j] > int_list[j + 1] :
                int_list[j], int_list[j + 1] > int_list[j + 1], int_list[j]

    return int_list


if __name__ == '__main__' :
    int_list = [1, 2, 3, 4, 4, 5, 6, 2, 3, 4, 3, 9, 0, 0]
    result = min_max(int_list)
    print(result)