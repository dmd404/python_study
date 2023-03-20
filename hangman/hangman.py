import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
end_of_game = False
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

lives = 6
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#create blanks
display = []
for letter in chosen_word:
    display.append('_')

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    # check guessed letter
    for i, letter in enumerate(chosen_word):
        if letter == guess:
            display[i] = letter

    # If guess is not a letter in the chosen_word, then reduce 'lives' by 1.
    if guess not in chosen_word:
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
