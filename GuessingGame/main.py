# Number Guessing Game Objectives:

from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
answer = random.randint(1, 101)
print("I;m thinking of a number between 1 and 100.")
print(f"Pssst, the correct answer is {answer}")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    lives = 10
else:
    lives = 5

print(f"You have {lives} attempts remaining to guess the number.")

while lives != 0:
    users_guess = int(input("Make a guess: "))
    if users_guess == answer:
        print(f"You got it! The answer was {answer}.")
        break
    elif users_guess < answer:
        print("Too low.")
        lives -= 1
    elif users_guess > answer:
        print("Too high.")
        lives -= 1
    if lives == 0:
        print("You've run out of guesses, you lose.")
    else:
        print(f"Guess again\nYou have {lives} attempts remaining to guess the number.")
