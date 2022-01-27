# Blind Auction Challenge
# write a program that chooses the winner of a silent auction 

from blind_auction_art import logo
import os

def clear_console():
    os.system('clear')

print(logo)

bids = {}
done_bidding = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Lynn": 123, "John": 321}
  for i in bidding_record:
    bid_amount = bidding_record[i]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = i
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not done_bidding:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    done_bidding = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear_console()