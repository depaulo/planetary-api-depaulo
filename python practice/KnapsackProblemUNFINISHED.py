def knapsack_problem(val_list, weight_list, w) :
    value_per_weight = []
    total_weight = 0
    total_value = 0
    for i in range(len(val_list)) :
        value_per_weight.append(val_list[i] / weight_list[i])

    print(value_per_weight)
    for i in range(len(val_list)) :
        total_value += val_list[value_per_weight.index(min(value_per_weight))]
        total_weight += weight_list[value_per_weight.index(min(value_per_weight))]
        print(total_value, total_weight, value_per_weight)
        if total_weight > w :
            total_value -= val_list[value_per_weight.index(min(value_per_weight))]
            total_weight -= weight_list[value_per_weight.index(min(value_per_weight))]
            break
        elif total_weight == w :
            break
        value_per_weight.pop(value_per_weight.index(min(value_per_weight)))

    return (total_value, total_weight)


if __name__ == '__main__' :
    val_list = [40, 100, 50, 60]
    weight_list = [20.0, 10.0, 40.0, 30.0]
    w = 60
    result = knapsack_problem(val_list, weight_list, w)
    print(result)