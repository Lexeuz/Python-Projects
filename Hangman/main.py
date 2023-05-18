# Hangman Alexander Eraso

# Impports.
import random
import hangman_art
from hangman_words import word_list

# Word selection, lives tracking and stage counter.
chosen_word = random.choice(word_list)
stage = 0
lives = 7

print(hangman_art.logo)
print(f"Pssst, the solution is {chosen_word}.\n")

# Creating the blank spaces to show the amount of letters in the word.
display = []
for _ in range(len(chosen_word)): display.append("_")

# Printin the "Display" that shows the blank spaces.
print(f"{display} \n")

# Loop to let the user guess until the guesser runs out of lives.
while lives != 0:
    # Turns any letter into a lowercase one.
    guess = input("Guess a letter: \n").lower()

    # Checks if the letter is in the word and takes one live from the total and prints the stage.
    if guess not in chosen_word:
        lives -= 1
        print("The letter you guessed is not in the word.\n")
        print(hangman_art.stages[stage])
        stage += 1

        # Once lives counter gets to 0 it prints "You've lost" and the game is over!
        if lives == 0: print("You've lost!")

    # First checks if the letter has been already guessed or assigns the letter to its corresponding blank space.
    if guess in display: print(f"You've already tried with that one. {guess}\n")
    else:
        index = 0
        for letter in chosen_word:
            if letter == guess:
                display[index] = guess
            index += 1
    
    print(display)

    # Checks if the guesser has guessed all the letters.
    if "_" not in display:
        print("\nYou win!") 
        break


