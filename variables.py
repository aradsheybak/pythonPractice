# this class build for variables practice
# variables like Integer,String,Boolean and etc...

#1 string variable:


# in Python we can use single quotation or double quotation for String and both of them is right

#double quotation example
first_name = "Arad"
last_name = "Sheybak"

print("I'm "+first_name + " "+last_name)

#single quotation example
first_name2 = 'Arad'
last_name2 = 'Sheybak'

print("I'm "+first_name2 + " "+last_name2)

#######################################################################
#2 Integer variabels:

age = 27
height = 183

#for showing an integer varibale with string variable, we must converting integer variable to string,
# in python for converting an integer variable to string we use str(integerVariable)
print("im "+str(age)+" years old and "+str(height)+"cm height")

######################################################################

#3: Boolean variables:
human = True
print("Are you a human? "+str(human))

######################################################################

#4: multiple assignment

name, color, nationalCode = "Arad", "blue", 1234567890

print(name)
print(color)
print(nationalCode)
######################################################################
#5: set same  value to many variable name

# aradAge = 27
# aliAge = 27
# rickyAge = 27
# elonAge = 27
#we can set same value to different variableName
aradAge = aliAge = rickyAge = elonAge = 27

print(aradAge)
print(aliAge)
print(rickyAge)
print(elonAge)

########################################################################

