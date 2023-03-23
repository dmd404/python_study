import random
import os
from art import logo

def deal_card():
    """
    :return:
    random card from the deck.
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    """
    :param cards:
    :return:
    take a list of cards and return the score calculated from the cards
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(player_score, computer_score):
    if player_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Dealer has Blackjack. YOu lose."
    elif player_score == 0:
        return "YOu have a Blackjack. YOu win!"
    elif computer_score > 21:
        return "Dealer went over. You win!"
    elif player_score > 21:
        return "YOu went over. You lose."
    elif player_score > computer_score:
        return "you win!"
    else:
        return "you lose."


def play_game():
    print(logo)

    player_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
                          player_cards.append(deal_card())
                          computer_cards.append(deal_card())

    while not is_game_over:

       player_score = calculate_score(player_cards)
       computer_score = calculate_score(computer_cards)
       print(f" Your hand: {player_cards}, current score: {player_score}")
       print(f" Computer's first card: {computer_cards[0]}")

       if player_score == 0 or computer_score == 0 or player_score > 21:
           is_game_over = True
       else:
           another_card = input("Type 'y' for another card, 'n' to pass: ")
       if another_card == 'y':
           player_cards.append(deal_card())
       else:
           is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"YOur final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(player_score, computer_score))

while input("Do you want to play game of Blackjack? Type 'y' or 'no': ") == 'y':
    os.system('clear')
    play_game()
