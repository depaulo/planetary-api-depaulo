def reverseString(input_string) :
    reverseString = input_string.split()
    print(reverseString)
    return ' '.join(reverseString[::-1])


if __name__ == '__main__' :
    input_string = 'i love programming very much'
    Output = reverseString(input_string)
    print(Output)