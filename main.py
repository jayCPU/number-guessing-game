import random
import math

#getting range
lower = int(input("Input lower bound: "))
upper = int(input("Input upper bound: "))

#number to guess
x = random.randint(lower, upper)

#amount of guesses
maxtries = round(math.log(upper - lower + 1, 2))
print("You only have", maxtries,"guesses! Good luck!")

tries = 0

while tries < maxtries:
    tries += 1
    
    guess = int(input("Guess the number: "))
    
    if guess == x:
        print("Congratulations, that's the correct number!")
        
        break
    elif guess < x:
        print("Too low")
    elif guess > x:
        print("Too high")
        
if tries >= maxtries:
    print("You've reached the max number of guesses")
    print("The correct number was", x ,".")
    print("Better luck next time!")