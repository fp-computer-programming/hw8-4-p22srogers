# Author: SMR (AMDG) 12/10/21
import random
random_number = random.randint(0, 50)
while True:
    guess = int(input(" Guess a number within 0-50. "))
    if(guess > random_number):
        print("Too high keep going!")
        continue
    elif(guess < random_number):
        print("Too low keep going!")
        continue
    else:
        print("You guessed it!")
    break
