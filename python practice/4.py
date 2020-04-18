inNumber = int(input("Enter a number"))

myList = range(1, inNumber)

for each in myList:
    if inNumber % each == 0:
        print("Your number is divisible for " + str(each))
