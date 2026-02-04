
import pandas

nato_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = { row.letter:row.code for (index,row) in nato_dataframe.iterrows()}

word = input("Type a word to convert to phonetic codeword: ").upper()
phonetic_codewords= [nato_dict[letter] for letter in word]
print(phonetic_codewords)




