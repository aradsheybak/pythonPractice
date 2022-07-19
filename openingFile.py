try:
    with open('test.tx') as file:
        print(file.read())
except FileNotFoundError:
    print("File not found!")
