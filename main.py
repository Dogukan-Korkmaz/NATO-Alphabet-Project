import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

new_nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}


# is_finished = False
# while not is_finished:
#     word = input("Enter a word ").upper()
#     try:
#         letters = [new_nato_dict[letter] for letter in word]
#     except:
#         print("Sorry, only letters in the alphabet please.😇")
#     else:
#         is_finished = True
#         print(letters)

def generate_phonetic():
    word = input("Enter a word ").upper()
    try:
        letters = [new_nato_dict[letter] for letter in word]
    except:
        print("Sorry, only letters in the alphabet please.😇")
        generate_phonetic()
    else:
        is_finished = True
        print(letters)

generate_phonetic()