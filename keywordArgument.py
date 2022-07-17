def sayHello(name, age, job):
    print("Hello " + name + "! You are " + str(age) + " years old and you are " + job)


my_name = input("What's your name?")
my_age = input("How old are you?")
my_job = input("what is your job?")

sayHello(name=my_name, job=my_job, age=my_age)
