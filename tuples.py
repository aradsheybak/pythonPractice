# tuple = collection which is ordered and unchangeable used to group together  related data

developer = ("Arad", 27, "Android and Python Developer")

print(developer)
print(developer.count("Arad"))
print(developer.index(27))

if "Arad" in developer:
    print("Arad is a Developer!")
