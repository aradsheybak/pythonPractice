# lists = used to store multiple variables in a single variable

family = ["Ali", "Sareh", "Negar", "Asieh", "Arad", "Hossein"]
for i in range(len(family)):
    print(family[i])
##############################################################

# replace a vlue with an item of list, for this operation we need to index of list item
print("################################")
family[4] = "Abolfazl"
print(family)
#############################################################

# add an item to end of list

family.append("Javad")
print(family)
#############################################################

# remove an item from list
family.remove("Javad")
print(family)
#############################################################

# remove last item from list
family.pop()
print(family)
############################################################

# add an item to specific position
family.insert(5, "Hossein")
print(family)
############################################################

# sort a list according alphabet
family.sort()
print(family)
############################################################

# clear all of list
family.clear()
print(family)
