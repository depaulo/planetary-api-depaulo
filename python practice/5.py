a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

overlapNums = []

for each in a :
    if each in b :
        overlapNums.append(each)

print(overlapNums)
