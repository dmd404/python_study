import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_card = []
computer_card = []
player_score = 0
computer_score = 0


def get_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return cards[random.randint(0, 12)]

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
      extra_card = score_check(player_score, computer_score,)
