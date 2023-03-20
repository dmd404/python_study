import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#For each letter in the chosen_word, add a "_" to 'display'.
display = []
for letter in chosen_word:
    display.append('_')

# Use a while loop to let the user guess again.
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for i, letter in enumerate(chosen_word):
        if letter == guess:
            display[i] = letter

    print(display)

    if "_" not in display:
        end_of_game = True
        print('You win')
