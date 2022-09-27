import pandas

data = pandas.read_csv("./Day_26/NATO_Alphabet/nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for index, row in data.iterrows()}

def generate_phonetic():
    name = input("Enter your name: ").upper()
    try:
        phonetic_list = [phonetic_dict[letter] for letter in name]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(phonetic_list)

generate_phonetic()