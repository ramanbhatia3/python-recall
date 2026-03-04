# infinite generators

def infinite_names():
    count = 1
    while True:
        yield f"Name #{count}"
        count += 1

name = infinite_names()

name2 = infinite_names()

for _ in range(10):
    print(next(name))

for _ in range(5):
    print(next(name2))