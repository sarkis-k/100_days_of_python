# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

data = []

with open("Input/Letters/starting_letter.txt") as letter:
    l_data = letter.read()

with open("Input/Names/invited_names.txt") as file:
    for x in file.readlines():
        data.append(x)
        file_name = "ready_" + x
        f = open(f"Output/ReadyToSend/{file_name}", "x")
        message = l_data.replace("[name]", x)
        if f:
            f.write(message)

