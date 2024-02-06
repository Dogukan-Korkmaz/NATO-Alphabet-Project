import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

new_nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word ").upper()

letters = [new_nato_dict[letter] for letter in word]
print(letters)

