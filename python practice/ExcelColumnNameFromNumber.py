def fullRounds(input_number) :
    ALPHABET = 'ZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    full_rounds = input_number / 26
    #for i in ALPHABET[full_rounds:full_rounds+1] :
     #   print(ALPHABET[full_rounds])
        return ALPHABET[full_rounds]

def firstRound(input_number) :
    ALPHABET = 'ZABCDEFGHIJKLMNOPQRSTUVWXY'
    return ALPHABET[input_number]

def excelColumnNameGenerator(input_number) :
    answer = ''
    answer += firstRound(input_number % 26)
    if input_number > 26 :
        answer += fullRounds(input_number)
    return answer[::-1]

if __name__ == '__main__' :
    while True :
        input_number = int(input())
        ColumnName = excelColumnNameGenerator(input_number)
        print(ColumnName)