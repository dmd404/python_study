from replit import clear
from art import logo

print(logo)


auction = {}

another = True

def find_highest_bid(bid):
  high_bid = 0
  winner = ''
  for i in bid:
    if bid[i] > high_bid:
      high_bid = bid[i]
      winner = i
  print(f'{winner}, highest bid is {high_bid}')

while another:
  name = input('your name: ')
  bid_price = int(input('your bid: '))
  auction[name] = bid_price
  bid_continue = input('other bid? Type "yes" or "no": ').lower()
  if bid_continue == 'no':
    another = False
    print(auction)
    find_highest_bid(auction)
    
  elif bid_continue == 'yes':
    clear()
    
