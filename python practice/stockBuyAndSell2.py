def BuyAndSell(prices):
    intervalplus = []
    for each in range(len(prices)) :
        print(each)
        if prices[each]-prices[each+1] > 0 :
            intervalplus.append(i)
        print(intervalplus)
    print(intervalplus)

    range_start = previous_number = intervalplus[0]
    for number in intervalplus[1 :] :
        if number == previous_number + 1 :
            previous_number = number
        else :
            yield [range_start, previous_number]
            range_start = previous_number = number
    yield [range_start, previous_number]


def PrintFunction(results: list):
    for i in range(0, len(results), 2) :
        print('('+str(results[i]),str(results[i+1])+')')
    print('\n')


if __name__ == '__main__' :
    number_of_sets = int(input())
    number_of_results = 0
    for i in range(number_of_sets) :
        results = []
        input()
        results.append(BuyAndSell(str(input()).split()))
        print(results)
    for i in range(number_of_sets) :
        PrintFunction(results[i])

for i in range(2) :
    print(i)
