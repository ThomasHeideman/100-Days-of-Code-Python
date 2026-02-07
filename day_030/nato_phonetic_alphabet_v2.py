import pandas

nato_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = { row.letter:row.code for (index,row) in nato_dataframe.iterrows()}

def convert():
    word = input("Type a word to convert to phonetic codeword: ").upper()
    try:
        phonetic_codewords= [nato_dict[letter] for letter in word]
    except KeyError as error_message:
        print(f"Sorry, {error_message} is not a word, please use letters in the alphabet only")
        convert()
    else:
        print(phonetic_codewords)

convert()
