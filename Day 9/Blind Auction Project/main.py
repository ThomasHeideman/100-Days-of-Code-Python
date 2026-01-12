from art import logo
print(logo)

bids = {}
winner = ''
should_continue = True


def find_highest_bidder(bidding_dictionary):
    highest_bid = ['', 0]

    for bid in bidding_dictionary:
        if bidding_dictionary[bid] > highest_bid[1]:
            highest_bid = [bid, bidding_dictionary[bid]]

    winner = f"{highest_bid[0]} has the highest bid, with €{highest_bid[1]}, {highest_bid[0]} wins the auction!"
    print(winner)


while should_continue:
    name = input("Enter your name:")
    bid = int(input("Enter your bid: €"))
    bids[name] = bid
    new_bidder = input("Are there any other bidders? Type 'yes' or 'no':").lower()
    if new_bidder == "no":
        should_continue = False
        find_highest_bidder(bids)
    else: print("\n" * 25)

