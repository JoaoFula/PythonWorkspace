# Number guessing game

import random
 
# Defining variables

n = random.randint(1,99)
guess = int(input("Enter a number between 1 to 99: "))

# Variable inicialization to save min and maximum values to help the user
minGuess = 0
maxGuess = 99
numberOfTimes = 0

# Checking loop
while n != "guess":
    numberOfTimes = numberOfTimes + 1
    print
    if guess < n:
        if guess > minGuess:
            minGuess = guess
        guess = int(input("Guess was low, enter a higher number between "+ str(minGuess)+ " and "+ str(maxGuess)+": "))
    elif guess > n:    
        if guess < maxGuess:
            maxGuess = guess
        guess = int(input("Guess was high, enter a lower number between "+ str(minGuess)+ " and "+ str(maxGuess)+" : "))
    else:
        print("Congratulations, you entered the correct number!")
        break
    print

# Print number of times it took the user to guess the number
print("It took you "+ str(numberOfTimes) +" attempts to get the correct number.")
if numberOfTimes != 1:
    print("You can improve in " + str(numberOfTimes-1) + " attempts.")
