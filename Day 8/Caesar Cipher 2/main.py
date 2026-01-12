alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def start():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caesar(encode_or_decode, input_text,shift_amount):
        output_text = ""
        if encode_or_decode == "decode":
                shift_amount *= -1

        for letter in input_text:
            shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
            output_text += alphabet[shifted_position]
        print(f"Here is the {encode_or_decode}d result: {output_text}")
        start()


    caesar(encode_or_decode=direction,input_text=text,shift_amount=shift)
start()