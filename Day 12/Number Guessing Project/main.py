import random
from art import logo
continue_playing = True

def set_difficulty():
    print("welcome to the Number Guessing game.\nI'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'hard':
        return 5
    else:
        return 10

def guess_function(guess_input,secret):
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
    print(logo)

    secret_number = random.randint(1, 100)
    num_guesses = set_difficulty()

    guess_function(num_guesses,secret_number)

while continue_playing == True:
    play_game()
    if input("Do you want to play again? 'y' or 'n': ") != 'y':
        continue_playing = False
    else:
        print("\n" * 25)

