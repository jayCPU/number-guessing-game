import random

name = str(input("Hello, what is your name?: "))

print("Good luck", name,"!")

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks', 'sigma', 'shit']

answer = random.choice(words)

print("Guess the CHARACTERS of the word! You'll have 12 guesses.")
turns = 12

guesses = ''

while turns > 0:
    
    failed = 0

    for char in answer:
        if char in guesses:
            print(char, end="\n")
            
        else:
            print("_")
            
            failed += 1
            
    if failed == 0:
        print("You win!")
        print("The word is:", answer)
        
        break
    
    print()
    guess = input("Guess a character: ")
    
    guesses += guess
    
    if guess not in answer:
        turns -= 1
        
        print("Incorrect, please try again.")
        print("You have", + turns, "guesses left")
        
    if turns == 0:
        print("You lose! Good luck next time!")
