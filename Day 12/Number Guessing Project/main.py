from random import randint
from art import logo
continue_playing = True
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty():
    """
        Prompts the user to select a difficulty level and determines the starting number of attempts.
        :return: The value of either EASY_LEVEL_TURNS or HARD_LEVEL_TURNS based on user input.
    """
    print("welcome to the Number Guessing game.\nI'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'hard':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def guess_function(guess_input,secret):
    """
        Runs the main game loop where the user makes guesses until they win or run out of turns.
        :param guess_input: The initial number of attempts based on difficulty.
        :param secret: The random target number the user needs to guess.
        """
    while guess_input > 0:
        guess = int(input(f'You have {guess_input} attempts remaining to guess the number.\nMake a guess: '))
        guess_input -= 1
        if guess == secret:
            print('You won! 🏆')
            return
        elif guess < secret:
            print("Too low.\nGuess again.")
        else:
            print("Too high.\nGuess again.")
    print("You've run out of guesses.")


def play_game():
    """
        Initializes a single round of the Number Guessing game, including the logo and secret number generation.
        """
    print(logo)

    secret_number = randint(1, 100)
    num_guesses = set_difficulty()

    guess_function(num_guesses,secret_number)

while continue_playing == True:
    play_game()
    if input("Do you want to play again? 'y' or 'n': ") != 'y':
        continue_playing = False
    else:
        print("\n" * 25)

