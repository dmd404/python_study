from art import logo
import random


print(logo)
print("Welcome to Number Guess Game!")
print("Guess a number between 1 and 100")
difficulty = input("Choose a difficulty. 'easy' or 'hard': ").lower()


def set_difficulty(user_input):
    """
    :param user_input:
    :return:
    set difficulty based on user choice
    """
    if user_input == 'easy':
        return 10
    elif user_input == 'hard':
        return 5


def play_game():
    guess = int(input('Make a guess: '))
    if guess == rand_num:
        print("correct!")
        global attempts
        attempts = 0
    elif guess > rand_num:
        print("Too high\n")
    elif guess < rand_num:
        print("Too low\n")


attempts = set_difficulty(difficulty)
rand_num = random.randint(1, 100)
should_continue = True

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    play_game()
    attempts -= 1
