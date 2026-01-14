import random
from art import logo

def calculate_cards(hand_of_cards):
    if sum(hand_of_cards) == 21  and  len(hand_of_cards) == 2:
        return  0
    if sum(hand_of_cards) > 21 and 11 in hand_of_cards:
        hand_of_cards.remove(11)
        hand_of_cards.append(1)
    return sum(hand_of_cards)

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def play_game():
    keep_playing = True
    player_hand = []
    dealer_hand = []

    for _ in range(2):
        player_hand.append(deal_card())
        dealer_hand.append(deal_card())

    player_score = calculate_cards(player_hand)
    dealer_score = calculate_cards(dealer_hand)

    print(f"Your cards: {player_hand}, current score = {calculate_cards(player_hand)}")
    print(f"The dealer's first card: {dealer_hand[0]}")

    while keep_playing:

            if player_score == 0 or dealer_score== 0 or player_score > 21:
                keep_playing = False
            else:
                another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                if another_card == 'y':
                    keep_playing = True
                    player_hand.append(deal_card())
                    player_score = calculate_cards(player_hand)
                    print(f"Your cards: {player_hand}, current score = {calculate_cards(player_hand)}")
                    print(f"The dealer's first card: {dealer_hand[0]}")
                else:
                    keep_playing = False

    while dealer_score !=0 and dealer_score < 17:
            dealer_hand.append(deal_card())
            dealer_score = calculate_cards(dealer_hand)

        # calculate score
    score_player = calculate_cards(player_hand)
    score_dealer = calculate_cards(dealer_hand)

    print(f"Your final hand: {player_hand},final score: {score_player} ")
    print(f"The dealer's final hand: {dealer_hand}, final score = {score_dealer}")
    if dealer_score == 0:
        print(f"Your cards: {player_hand}, final score = {calculate_cards(player_hand)}")
        print(f"Dealer has blackjack ({dealer_hand}). You lose! 💀")
    elif player_score == 0 and dealer_score != 0:
        print(f"Dealer has {calculate_cards(dealer_hand)}, you have 21! You win! 🎉")
    elif player_score == 0 and dealer_score == 0:
        print(f"Dealer has 21, you have 21. It's a push 🙄")
    elif score_player > 21:
        print(f"Bust, you have {calculate_cards(player_hand)}! You lose! 💀")
    elif score_player == score_dealer:
        print(f"Dealer has {calculate_cards(dealer_hand)}, you have {calculate_cards(player_hand)}. It's a push 🙄")
    elif score_player < 21 and score_dealer > 21:
        print(f"Dealer is bust with {score_dealer}, you have {score_player}. You win! 🎉")
    elif score_player == 21 or score_player > score_dealer:
        print(f"Dealer has {score_dealer}, you have {score_player}. You win! 🎉")
    elif score_player < score_dealer:
        print( f"Dealer has {calculate_cards(dealer_hand)}, you have {calculate_cards(player_hand)}. You lose! 💀")

    if input("Play again? 'y' or 'n': ") == "y":
        print("\n" * 25)
        play_game()
print(logo)
play_or_not = input("Do yo want to play a game of Blackjack? Type 'y' or 'n' ").lower()
if play_or_not == 'y':
    play_game()
