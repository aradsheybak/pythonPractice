text = "Hello Arad!\n if you want to be success!\n you must do hard work!!!"
text2 = "I know yo can!\n I know you are a HERO!"

# For write in a file
with open("letterToArad", 'w') as file:
    file.write(text)

# for appending a new text to a file
with open("letterToArad", 'a') as file:
    file.write(text2)
