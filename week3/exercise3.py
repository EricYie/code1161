"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""


from exercise1 import not_number_rejector
from exercise1 import super_asker
import random


def advancedGuessingGame():
     

    print("\nwelcome to the guessing game!")
    lowerBound = not_number_rejector("Enter a lower bound: ") 
    upperBound = not_number_rejector("Enter an upper bound: ")
    while lowerBound >= upperBound:
        print("{} is too high".format(lowerBound))
        upperBound = not_number_rejector("Enter an upper bound: ")
    
    print("OK then, a number between {} and {} ?".format(lowerBound,upperBound))
    lowerBound = int(lowerBound)
    upperBound = int(upperBound)

    actualNumber = random.randint(lowerBound, upperBound)

    guessed = False

    while not guessed:
        try:
          guessedNumber = int(input("Guess a NUmber: "))
          print("{} is the number".format(guessedNumber))
        except Exception as e:
          print("{} is not a number, please enter a number only".format(e))
          continue
        if guessedNumber < lowerBound or guessedNumber > upperBound:
          print("{} is outside the bound".format(guessedNumber))
        else: 
          print("you guessed {},".format(guessedNumber),)
        if guessedNumber == actualNumber:
            print("you got it!! It was {}".format(actualNumber))
            guessed = True
        elif guessedNumber < actualNumber:
            print("too small, try again ")
        else:
            print("too big, try again   ")
    return "You got it!"

if __name__ == "__main__":
    advancedGuessingGame()
