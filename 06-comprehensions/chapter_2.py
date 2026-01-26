# list comprehensions

heroes = [
    "ironman",
    "spiderman",
    "dc superman",
    "thor",
    "dc batman",
    "dc flash",
    "hulk"
]

dc_heroes = [hero for hero in heroes if "dc" in hero]

print(dc_heroes)