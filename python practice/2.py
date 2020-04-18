while True :
    number = int(input("Enter a number"))
    if number % 4 == 0:
        print("This number can be divided by 4")
    elif number % 2.0 == 0:
        print("It is an even number")
    elif number == 99:
        break
    else:
        print("The number is odd")

