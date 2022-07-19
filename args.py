# *args = parameter that will pack all arguments into a tuple useful so that a function can accept a varying amount of arguments
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


print("first args output:")
print(add(10, 23, 56, 657))


############################################################
# *args pack all arguments to tuples and tuples are unchangeable
# if we want to change a argument from *args, first we must cast *args to a list, because list is changeable

def add2(*stuff):
    sum2 = 0
    # cast args to list with below code
    stuff = list(stuff)
    stuff[0] = 0
    for j in stuff:
        sum2 += j
    return sum2


print("second args output:")

print(add2(10, 23, 56, 657))
