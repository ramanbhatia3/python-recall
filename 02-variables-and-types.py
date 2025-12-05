"""Python is completely object oriented, and not "statically typed". You do not need to declare variables before using them, or declare their type. Every variable in Python is an object."""

myint = 7
print(myint)

myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

mystring = "Don't worry about apostrophes"
print(mystring)

one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
# print(helloworld) -----------------------> error

# Assignments can be done on more than one variable "simultaneously" on the same line like this
a, b = 3, 4
print(a, b)

# Mixing operators between numbers and strings is not supported:
one = 1
two = 2
hello = "hello"

# print(one + two + hello)  # This will give an error