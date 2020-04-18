def StringAnalysis(input_string) :
    test_string = list(input_string)
    test_string.sort() #sort computational cost O(n log n)
    print(test_string)
    for i in range(0, len(test_string)-1) : #2n
        if i == 0 and test_string[i] != test_string[i+1]:
            return test_string[i]
        elif test_string[i] != test_string[i+1] and test_string[i] != test_string[i-1] :
            return test_string[i]

if __name__ == '__main__' :
    input_string = 'GeeksforGeeks'
    input_string2 = 'GeeksQuiz'

    for i in (input_string, input_string2) :
        answer = StringAnalysis(i)
        print(answer)

