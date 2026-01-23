from game_data import data
from art import logo
from art import vs
from random import choice

def get_random_item(current_item=None):
    """
        Picks a random account from the dataset and ensures it's not the same as the current one.
        :param current_item: The account currently in position A to avoid duplicates.
        :return: A random dictionary from the game data.
        """
    new_item = choice(data)
    while new_item == current_item:
        new_item = choice(data)
    return new_item

def format_data(account):
    """
    Formats the account dictionary into a printable string.
    :param account: The dictionary containing account details.
    :return: A formatted string with name, description, and country.
    """
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(followers_a,followers_b):
    """
        Compares the follower counts and returns the winner's letter.
        :param followers_a: The number of followers for account A.
        :param followers_b: The number of followers for account B.
        :return: A string 'a' or 'b' based on who has more followers.
        """
    if followers_a > followers_b:
        return 'a'
    else:
        return 'b'

continue_game = True

def play_game():
    """
        Runs the main logic for a single game session.
        :return: None
        """
    print(logo)
    keep_playing = True
    score = 0
    item_a = get_random_item()
    item_b = get_random_item(item_a)


    while keep_playing:
        print(f"Compare A:" + format_data(item_a))
        print(vs)
        print(f"Against B:" + format_data(item_b))

        user_answer = input("Who has more followers? Type 'A', or 'B': ").lower()
        actual_answer = check_answer(item_a['follower_count'],item_b['follower_count'])

        if user_answer == actual_answer:
            if actual_answer == 'b':
                item_a = item_b
            item_b = get_random_item(item_a)
            score += 1
            print(f"You're right, current score: {score}\n")
        else:
            print(f"sorry, that's wrong. Final score: {score}\n")
            keep_playing = False


while continue_game == True:
    play_game()
    if input("Do you want to play again? 'y' or 'n': ") != 'y':
        continue_game = False
    else:
        print("\n" * 25)
