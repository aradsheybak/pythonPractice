# dictionary = a changeable, unordered, collection of uniqe key:value pairs
# fast because they use hashing , allow us to access a value quickly

capitals = {'Iran': 'Tehran',
            'India': 'New Delhi',
            'China': 'Beijing',
            'Russia': 'Moscoww'}

# access to a value of dictionary bt key
print(capitals["Iran"])

# get a value from dictionary who it doesn't  exist in dictionary without carsh program
print(capitals.get('Germany'))

# access to all key's of dictionary
print(capitals.keys())

# access to all values of dictionary
print(capitals.values())

# access to all items of dictionary with key values
print(capitals.items())

# add an item to dictionary
capitals.update({'Germany': 'Berlin'})

# update value of a key in dictionary
capitals.update({"Iran": "Gorgan"})

# remove item from dictionary
capitals.pop('China')

# clear a dictionary -> remove all items
# capitals.clear()


for key, values in capitals.items():
    print(key, values)
