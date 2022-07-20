import os

source = "letterToArad"
destination = "A:\\LetterToArad"
try:
    if os.path.exists(destination):
        print("file is exists")
    else:
        os.replace(source, destination)
        print(source + " was moved")

except FileNotFoundError:
    print(source + " not found! ")
