import random
from art import logo
from replit import clear

############### Blackjack Project #####################
### Second attempt at coding, this time on "Normal" difficulty (e.g. w/ hints).###

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
 
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  #Bug fix. If you and the computer are both over, you lose.
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"
  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():
  print(logo)
  user_cards = []
  computer_cards = []
  is_game_over = False

  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:
   
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'h' to hit, type 's' to stand: ").lower()
      if user_should_deal == "h":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
  clear()
  play_game()

# ###First attempt to code on "Very Hard" difficulty.  Works around 95% but, it has a few bugs that I don't know how to fix (as of day 11.)  ###
# end_of_game = False
# while not end_of_game:
#     def deal_em():
#         print(logo)
#         cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#         human_cards = []
#         comp_cards = []
#         # "deal" 2 random cards to human & computer
#         for i in range(2):
#             card = random.choice(cards)
#             human_cards.append(card)
#             comp_cards.append(card)
#         #check for blackjack on "opening deal"
#         if sum(human_cards) == 21 and sum(comp_cards) == 21:
#             print(f"You {human_cards} and Computer {comp_cards} both have Blackjack!  It's a Draw!")
#             another_game()
#         elif sum(comp_cards) == 21 and len(comp_cards) == 2:
#             print(f"You have {human_cards}. Computer has blackjack {comp_cards}, You lose.")
#             another_game()
#         elif sum(human_cards) == 21 and len(human_cards) == 2:
#             print(f"Computer has {comp_cards}. You have blackjack {human_cards},  You Win!")
#             another_game()
#         else:
#             print(f"Computer is showing a {comp_cards[0]}.")
            
#         def human_turn():
#             human_hand = sum(human_cards)
#             print(f"You have {human_hand} with {human_cards}")
#             if human_hand > 21:
#                 if 11 not in human_cards:
#                     print("You went Bust.")
#                     another_game()
#                 else:
#                     if human_hand - 10 > 21:
#                         print("You lose.")
#                         another_game()
#                     else:
#                         human_cards.remove(11)
#                         human_cards.append(1)
#                         human_turn()     
#             else:
#                 another_card = input("Would you like to hit 'h' or stand 's'? ").lower()
#                 if another_card == "h":
#                     hit_me = random.choice(cards)
#                     human_cards.append(hit_me)
#                     human_turn()
#                 else:
#                     comp_turn()
        
#         def comp_turn():
#             human_hand = sum(human_cards)
#             comp_hand = sum(comp_cards)
#             if comp_hand < 17:
#                 hit_me = random.choice(cards)
#                 comp_cards.append(hit_me)
#                 comp_turn()
#             elif comp_hand > 21:
#                 print(f"Computer bust with {comp_hand} {comp_cards}, You win!")
#                 another_game()
#             else:
#                 print(f"You have {human_hand} with {human_cards}, Computer has {comp_hand} with {comp_cards}.")
#                 if human_hand > comp_hand:
#                     print("You Win!")
#                     another_game()
#                 elif human_hand < comp_hand:
#                     print("Computer Wins.")
#                     another_game()
#                 else:
#                     print("It's a Draw!")
#                     another_game()

#         def another_game():
#             if input("Would you like to play again? 'y' or 'n' ").lower() == 'y':
#                 clear()
#                 deal_em()
#             else:
#                 end_of_game = True
#                 clear()

#         human_turn()
#         comp_turn()
#         another_game()
#     deal_em()
