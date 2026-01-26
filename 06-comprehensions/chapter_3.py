# set comprehensions

heroes = [
    "ironman",
    "spiderman",
    "dc superman",
    "thor",
    "spiderman",
    "thor",
    "dc batman",
    "dc flash",
    "hulk",
    "hulk"
]

dc_heroes = {hero for hero in heroes if len(hero) > 7}

print(dc_heroes)



recepies = {
    "Masala Chai": ["ginger","cardamom","clove"],
    "Elaichi Chai": ["cardamom","milk"],
    "Spicy Chai": ["ginger","black pepper","clove"]
}

unique_spices = {spice for ingredients in recepies.values() for spice in ingredients }

print(unique_spices)