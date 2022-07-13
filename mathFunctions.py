import math

pi = 3.14
x = 1
y = 2
z = 3

# round a float number:
print("round pi: " + str(round(pi)))

# rounding up a float number:
print("rounding up pi: " + str(math.ceil(pi)))

# rounding down a float number:
print("rounding down pi: " + str(math.floor(pi)))

# absoloute a value -> get a negative value and turn it to positive
negative_pi = -3.14
print("turn negative pi to positive pi: " + str(abs(negative_pi)))

# power a number -> x^2 -> 2^2 = 4
x = 2
print("power of x to 2 is: " + str(pow(x, 2)))

# square root of a number-> square root of 36 is 6
y = 36
print("square root of 36 is: " + str(math.sqrt(y)))

# max of many integer or float value
z = 12
print("max of 2,12,36,pi is: ", str(max(x, y, z, pi)))

# min of many integer or float value
print("min of 2,12,36,pi is: ", str(min(x, y, z, pi)))

