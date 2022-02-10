from art import logo
import os

print(logo)

bids = {}
biddingFinished = False

def findHighestBidder(biddingRecord):
    highestBid = 0
    for bidder in biddingRecord: 
    #When looping through a dictionary it loops the keys not the value
        bidAmmount = biddingRecord[bidder]
        if bidAmmount > highestBid:
            highestBid = bidAmmount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highestBid}")    

while not biddingFinished:
    name = input("What is your name: ")
    price = int(input("What is your bid: $"))
    bids[name] = price
    shouldContinue = input("Are their any other bidders? Type 'yes' or 'no'\n")
    if shouldContinue == "no":
        biddingFinished = True
        findHighestBidder(bids)
    elif shouldContinue == "Yes":
        os.system("clear||cls")

