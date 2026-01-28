# send value to generator

def names():
    print("Hey, What is your name? ")
    order = yield
    while True:
        print(f"Nice to meet you {order}")
        order = yield

name = names()
next(name) # start of generator

name.send("Mohit")

name.send("Bhupinder")