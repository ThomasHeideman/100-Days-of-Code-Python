import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
option_list = [rock,paper,scissors]

user_choice = int(input('What do you choose? type 0 for Rock, 1 for Paper, 2 for Scissors.\n '))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, try again!")
else:
    print(f'You chose: {option_list[user_choice]}')
    computer_choice = random.randint(0, 2)
    print(f'Computer chose: {option_list[computer_choice]}')

    if user_choice == computer_choice:
        print('its a tie!')
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print('You win!🏆')
    else:
        print('You lose!💀')




# random_0_to_2 = random.randint(0,2)
# user_choice = int(input('What do you choose? type 0 for Rock, 1 for Paper, 2 for Scissors.'))
# print(f'You chose\n{option_list[user_choice]}')
# print(f'computer chose\n{option_list[random_0_to_2]}')
# if user_choice == 0:
#     if random_0_to_2 == 1:
#         print('You lose!')
#     elif random_0_to_2 == 0:
#         print('It\'s a draw')
#     elif random_0_to_2 == 2:
#         print('You win')
#     else:
#         print('You chose a wrong number!')
# elif user_choice == 1:
#     if random_0_to_2 == 2:
#         print('You lose!')
#     elif random_0_to_2 == 1:
#         print('It\'s a draw')
#     elif random_0_to_2 == 0:
#         print('You win')
#     else:
#         print('You chose a wrong number!')
# elif user_choice == 2:
#     if random_0_to_2 == 0:
#         print('You lose!')
#     elif random_0_to_2 == 2:
#         print('It\'s a draw')
#     elif random_0_to_2 == 1:
#         print('You win')
#     else:
#         print('You chose a wrong number!')
