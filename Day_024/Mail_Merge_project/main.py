with open('./Input/Names/invited_names.txt') as names:

    with open("./Input/Letters/starting_letter.txt", mode="r") as file:
        txt = file.read()
    for line in names:
            name = line.strip("\n")
            x = txt.replace("[name]", name)
            with open(f"./Output/ReadyToSend/Letter_To_{name.replace(' ', '_')}", mode="w") as new_file:
                new_file.write(x)







