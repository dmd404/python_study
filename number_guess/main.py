from random import randint

EASY_LEVEL = 10
HARD_LEVEL = 5


# Function to check user's guess against actual answer.
def check_answer(user_guess, real_answer, turns):
    """Checks answer against guess. Returns the number of turns remaining."""
    if user_guess > real_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < real_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"Correct! The answer was {real_answer}")


def set_difficulty():
    level = input("Choose difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL


def game():
    print("Welcome to number guess game!")
    print('Guess a number between 1 and 100.')
    answer= randint(1, 100)
    turns = set_difficulty()

    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("YOu've run out of guesses. YOu lose,")
            return
        elif guess != answer:
            print("guess again. \n")


game()