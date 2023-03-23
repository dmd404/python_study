import random


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


player_cards = []
computer_cards = []
is_game_over = False

for _ in range(2):
    player_cards.append(deal_card())
    computer_cards.append(deal_card())

player_score = calculate_score(player_cards)
computer_score = calculate_score(computer_cards)
print(f" Your hand: {player_cards}, current score: {player_score}")
print(f" Computer's first card: {computer_cards[0]}")

if player_score == 0 or computer_score == 0 or player_score > 21:
    is_game_over = True




def score_check(player, computer):
    if computer_score == 21:
        print("dealer has blackjack. You lose")
    elif player_score == 21:
        print("it's a blackjack. you win!")
    elif player_score > 21:
        print("You went over. you lose")
        return False
    elif computer_score > 21:
        print("dealer went over. you win!")
        return False


for i in range(2):
    player_card.append(get_card())
    computer_card.append(get_card())

should_continue = True

while should_continue:

    for i in player_card:
        player_score += i
    for i in computer_card:
        computer_score += i

    print(f"your hand: {player_card}, your score: {player_score}")
    print(f"dealer's first card: {computer_card[0]}")
    should_continue = score_check(player_score, computer_score)

    extra_card = True
    while extra_card:
        another_card = input("Type 'y' for another card, 'n' to pass: ").lower()
        if another_card == 'y':
            player_card.append(get_card())
            player_score += player_card[-1]
            print(f"your hand: {player_card}, your score: {player_score}")
            print(f"dealer's first card: {computer_card[0]}")
            extra_card = score_check(player_score, computer_score)
        else:
            print(f"Your final hand: {player_card}, final_score: {player_score}")
            print(f"Computer's final hand: {computer_card}, final_score: {computer_score}")
            extra_card = score_check(player_score, computer_score, )
