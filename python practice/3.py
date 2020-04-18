a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newA = []
inNumber = input("Which number you want to know if the elements of a are smaller than?")
for each in a:
    if each < int(inNumber):
        newA.append(each)

print(newA)