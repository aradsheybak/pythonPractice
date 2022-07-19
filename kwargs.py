# **kwargs= parameter that will pack all arguments into a dictionary, useful so that a function can accept a varying amount of keyword arguments

# without **kwargs
def sayHello(first, last):
    print("hello " + first + " " + last)


sayHello(first="arad", last="sheybak")


# with **kwargs:
def Hello(**kwargs):
    print(
        "hello " + kwargs['first'] + " " + kwargs['last'] + " your phone number is : " + kwargs[
            'phone'] + " and you are " +
        kwargs['age'] + " years old.")


Hello(first="Arad", last="Sheybak", age="27", phone="9123456789")


##############################################################################
# **kwargs cast to dictionary, so dictionary have key and value
# access to all key and values
def get_Key_value(**values):
    for k, v in values.items():
        print(k + ":", end="")
        print(v)

    print(
        "hello " + values['first'] + " " + values['last'] + " your phone number is : " + values[
            'phone'] + " and you are " +
        values['age'] + " years old.")


get_Key_value(first="Arad", last="Sheybak", age="27", phone="9123456789")
