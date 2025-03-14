from art import logo
print(logo)
print("Welcome to secrete auction program.")


def compare_bidder(bidding_dict):
    winner=""
    max_bid = 0
    for bidder in bidding_dict:
        bid_amount = bidding_dict[bidder]
        if bid_amount > max_bid:
            max_bid=bid_amount
            winner=bidder

    print(f"The winner for Auction is {winner} with the bid of {max_bid}.")


bid={}
continue_bidding = True
while continue_bidding:
    name = input("what is your name?\n")
    bids = int(input("what's your bid?: $"))
    should_continue = input("Are there any other bidder? Type 'yes' to continue else type 'no'.\n").lower()
    bid[name] = bids
    if should_continue =="no":
        continue_bidding=False
        compare_bidder(bid)
    elif should_continue=="yes":
        print("\n" * 20 )
