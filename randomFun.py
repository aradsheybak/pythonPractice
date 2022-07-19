import random

# pick a random integer from a range of integer
x = random.randint(1, 10)
print(x)

##################################################

# pick a random item from a list items

food = ["pizza", "meet", "sushi", "kebab", "chicken"]
print(random.choice(food))
########################################################

# rearrange a list in shuffle
cards = [2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"]
random.shuffle(cards)

print(cards)
