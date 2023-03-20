import random
from hangman_art import logo, stages
from hangman_words import word_list
import os


def clear():
   os.system('clear')

print(logo)
end_of_game = False
chosen_word = random.choice(word_list)

lives = 6

#create blanks
display = []
for letter in chosen_word:
    display.append('_')

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()

    if guess in display:
        print("You've already guessed this letter.")
    # check guessed letter
    for i, letter in enumerate(chosen_word):
        if letter == guess:
            display[i] = letter

    # If guess is not a letter in the chosen_word, then reduce 'lives' by 1.
    if guess not in chosen_word:
        print(f'{guess} is not in the word. You lose a life.')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('You lose')

    print(display)
    print(f'lives: {lives}')

    # check if the user has got all letters
    if "_" not in display:
        end_of_game = True
        print('You win')

    print(stages[lives])
