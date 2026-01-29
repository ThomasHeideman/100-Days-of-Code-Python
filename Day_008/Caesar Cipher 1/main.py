alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text,shift_amount):

    encrypted_text = ""
    for char in original_text:
        encrypt_index = (alphabet.index(char) + shift_amount) % len(alphabet)
        encrypted_char = alphabet[encrypt_index]
        encrypted_text += encrypted_char

    print("Here is the encoded message: ", encrypted_text)

encrypt(text,shift)
