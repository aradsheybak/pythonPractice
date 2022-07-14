# loops -> block of code who execute until a condition is true

#######################################################################
# 1: while
# count = int(input("Enter a number:"))
#
# while count > 0:
#     print(count)
#     count -= 1
########################################################################

# 2: for

# for index in range(10, 101):
#     print(index)
#
# list_names = ["Arad", "Ali", "Roham", "niloufar"]
#
# for i in range(len(list_names)):
#     print(list_names[i])
########################################################################
# 3: nested loops
# row = int(input("How many row:"))
# columns = int(input("How many columns:"))
#
# for i in range(row):
#     for j in range(columns):
#         print("*", end="")
#     print()
#######################################################################

# 4: control loops -> break , continue, pass

#break:

while True:
    name = str(input("Enter your name:"))
    if name != "":
        break


#continue:

phoneNumber = "123-456-789-0"
for i in phoneNumber:
    if i=="-":
        continue
    print(i,end="")


