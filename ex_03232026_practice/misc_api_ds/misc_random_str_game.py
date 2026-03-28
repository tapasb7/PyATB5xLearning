# Build a game where the computer generates a random number,
# and the user tries to guess it with hints.

import random

r = random.randint(1,100)
attempt = 0

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    attempt += 1
    if guess > 100 or guess < 1:
        print("Enter number between 1 and 100!")
        continue

    if guess > r:
        print("Sorry, the number is too high!")
    elif guess < r:
        print("Sorry, the number is too low!")
    else:
        print("Well done!")
        print('number of attempts:', attempt)
        break
