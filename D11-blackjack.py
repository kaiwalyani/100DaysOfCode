
import random 
from art import logo

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)
  

def compare(user_score, computer_score):
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
  comp_cards = []
  game_over = False 
  
  for i in range(2):
    user_cards.append(deal_card())
    comp_cards.append(deal_card())
  
  while not game_over:
    user_score = calculate_score(user_cards)
    comp_score = calculate_score(comp_cards)
    print(f"   Your Cards: {user_cards}, current score: {user_score}")
    print(f"   Computer Cards : {comp_cards[0]}")
    if user_score == 0 or comp_score == 0 or user_score > 21:
      game_over = True
    else:
      replay = input(f"Do you want to draw another card? Type 'y' or 'n' : ")
      if replay == 'y':
        user_cards.append(deal_card())
      else:
        game_over = True
  
  while comp_score != 0 and comp_score < 17:
    comp_cards.append(deal_card())
    comp_score = calculate_score(comp_cards)

  print(f" Your final hand: {user_cards}, final score: {user_score}")
  print(f" Computer's final hand: {comp_cards}, final score: {comp_score}")
  print(compare(user_score, comp_score))

while input(" Do you want to play a game of Blackjack? Type 'y' or 'n' :") == 'y':
  play_game()
  
