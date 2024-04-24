from replit import clear

from art import logo
print(logo)

bids = {}
bid_continue = True

def highest_bid(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid amount of ${highest_bid}")
    

while bid_continue:
  name = input("What is your name?")
  price = int(input("What is your Bid? $"))
  bids[name] = price
  more_bidder = input("Are there any other bidders? Type 'yes' or 'no' : ")
  if more_bidder == "yes":
    clear()
    print(logo)
  else:
    bid_continue = False
    highest_bid(bids)
