# yield from and close the generators

def niche():
    yield "Web Dev"
    yield "AI"

def languages():
    yield "JavaScript"
    yield "Python"

def skills():
    yield from niche()
    yield from languages()

for skill in skills():
    print(skill)


def bus_stand():
    try:
        while True:
            order = yield "Waiting for a bus"
    except:
        print("No more buses scheduled!")

bus = bus_stand()
print(next(bus))

bus.close() # cleanup