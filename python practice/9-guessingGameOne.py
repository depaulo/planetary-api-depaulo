import random

def playGame(number):
    numberGuessed = int(input("Guess a number between 1 and 9\n"))
    if numberGuessed < number :
        print("The number you guessed is smaller than the right number.")
        return 0
    elif numberGuessed > number :
        print("The number you guessed is bigger than the right number.")
        return 0
    elif numberGuessed == number :
        return 1



def main() :
    number = random.randint(1,9)
    answer = 'yes'
    numberOfTries = 0

    while answer == 'yes' or answer == 'y' :
        result = playGame(number)
        numberOfTries+=1
        if result==1 :
            print("You Won!!!! CONGRATULATION")
            return
        else :
            answer = input("You didn't guess it. \n You already tried " + str(numberOfTries) + " time(s)\nWant to try again? (type yes or y)\n",)


if __name__ == "__main__" :
    main()