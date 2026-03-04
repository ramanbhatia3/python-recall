# generators

def getName():
    yield "Name 1"
    yield "Name 2"
    yield "Name 3"

names = getName()

for name in names:
    print(name)



def get_name_fn():
    return ["Aditya", "Hitesh", "Saurav"]

def get_name_gen():
    yield "Aman"
    yield "Mohit"
    yield "Naman"

name_gen = get_name_gen()

print(next(name_gen))
print(next(name_gen))
print(next(name_gen))
print(next(name_gen)) # gives error