import random
from game_data import data
from art import logo, vs


def format_data(account):
  acc_nm = account["name"]
  acc_desc = account["description"]
  acc_cunt = account["country"]
  return f"{acc_nm} a {acc_desc}, from {acc_cunt}. "

def check_count(guess, foll_a, foll_b):
  if foll_a > foll_b:
    return guess == "a"
  else:
    return guess == "b"

print(logo)
score = 0

game_should_continue = True
acc_b = random.choice(data)

while game_should_continue:
  acc_a = acc_b
  acc_b = random.choice(data)
  if acc_a == acc_b:
    acc_b = random.choice(data)
  
  print(f"Compare A: {format_data(acc_a)}")
  print(vs)
  print(f"Compare B: {format_data(acc_b)}")
  
  
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()

  af_count = acc_a["follower_count"]
  bf_count = acc_b["follower_count"]
  is_correct = check_count(guess, af_count, bf_count)
  
  if is_correct:
    score += 1
    print(f"You're right! Current score: {score}.")
  else:
    game_should_continue = False
    print(f"Sorry, that's wrong. Final score: {score}.")
    
