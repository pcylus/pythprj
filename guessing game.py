"""Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low,
too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)
Extras:
Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out."""

import random
number = random.randint(1,9)
guess =0
count =0
print(number)
while number != guess and guess != 'exit' :
    guess = input('whats your guess\n')

    if guess == 'exit':
        break
    guess = int(guess)
    count+=1
    if(guess < number):
        print("The difference is too low")
    elif(guess > number):
        print('the difference is tooo high')
    else:
        print('You guesseed it right')
        print('it took you',count,'times to guess it right')

