import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#For each letter in the chosen_word, add a "_" to 'display'.
display = []
for letter in chosen_word:
  display.append('_')

guess = input("Guess a letter: ").lower()


#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
for i, letter in enumerate(chosen_word):
  if letter == guess:
    display[i] = letter

#Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
print(display)