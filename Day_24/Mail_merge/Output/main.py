PLACEHOLDER = "[name]"

with open("./100DaysOfCode/Day_24/Mail_merge/Input/Names/names.txt") as names_file:
    names = names_file.readlines()

with open("./100DaysOfCode/Day_24/Mail_merge/Input/Letter/letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./100DaysOfCode/Day_24/Mail_merge/Output/ReadyToSend/letter_to_{stripped_name}.txt", "w") as complete_letter:
            complete_letter.write(new_letter)

