def maxDivide( a, b) :#checks for the mmc only for 2, 3, 5
    while a%b == 0 :
        a = a / b
    return a


def isUgly (no) : # function that uses the mmc to see if a number is ugly or not
    no = maxDivide(no, 2)
    no = maxDivide(no, 3)
    no = maxDivide(no, 5)
    return 1 if no == 1 else 0


def getNthUglyNo (number) :#function to count the number of ugly numbers
    i = 1
    count = 1 # ugly number count
    while number > count:
        i += 1
        if isUgly(i):
            count += 1
    return i


if __name__ == '__main__' :#main function to initialize the code
    nthNo = int(input())
    no = getNthUglyNo(nthNo)
    print("{0}th ugly no. is {1}".format(nthNo, no))


