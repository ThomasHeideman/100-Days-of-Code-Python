import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print(random.choice(letters))
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy version
simple_password = ""
#
for char in range(nr_letters): # or range(1, nr_letters + 1):
    simple_password += random.choice(letters)
for password_num in range(nr_numbers): # or range(1, nr_numbers + 1):
    simple_password += random.choice(numbers)
for password_sym in range(nr_symbols): # or range(1, nr_symbols + 1):
    simple_password += random.choice(symbols)
print(simple_password)

#Hard version
password = ''
password_length = nr_letters + nr_symbols + nr_numbers
password_characters = []
for password_letter in range(nr_letters):
    password_characters.append(random.choice(letters))

for password_num in range(nr_numbers):
    password_characters.append(random.choice(numbers))

for password_sym in range(nr_symbols):
    password_characters.append(random.choice(symbols))

random.shuffle(password_characters)
for password_character in password_characters:
    password += password_character
print(password)


# for letter in range(password_length):
#     password = password + str(password_characters.pop(random.choice(range(0, len(password_characters)))))
# print(password)



