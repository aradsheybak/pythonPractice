import os

path = "C:\\Users\\Arad Sheybak\\Desktop\\folder"

if os.path.exists(path):
    print("file exist!")
    if os.path.isfile(path):
        print("this is a file")
    elif os.path.isdir(path):
        print("this is a directory!")
    else:
        print("it's not a file")
else:
    print("file doesn't exist!")
