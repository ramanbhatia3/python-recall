# Tuples - immutable

heroes = ("batman", "superman", "flash")

(hero1, hero2, hero3) = heroes

# print(heroes)
print(f"Heroes: {hero1}, {hero2}, {hero3}")

mathMarks, physicsMarks = 70, 87
print(f"Maths in Maths: {mathMarks} and in Physics: {physicsMarks}")

mathMarks, physicsMarks = physicsMarks, mathMarks
print(f"Maths in Maths: {mathMarks} and in Physics: {physicsMarks}")


# membership testing

print(f"Is flash a hero? {'flash' in heroes}")




# lists - mutable

marvelHeroes = ["ironman", "spiderman", "thor"]

marvelHeroes.append("antman")
print(f"Marvel Heroes are {marvelHeroes}")

marvelHeroes.remove("spiderman")
print(f"Marvel Heroes are {marvelHeroes}")

moreHeroes = ["hulk", "hawkeye", "falcon"]

marvelHeroes.extend(moreHeroes)
print(f"Marvel Heroes are {marvelHeroes}")

marvelHeroes.insert(0,"captain america")
print(f"Marvel Heroes are {marvelHeroes}")

last_added = marvelHeroes.pop()
print(f"Removed {last_added}")
print(f"Marvel Heroes are {marvelHeroes}")

marvelHeroes.reverse()
print(f"Reversed: {marvelHeroes}")

marvelHeroes.sort()
print(f"Sorted: {marvelHeroes}")


levels = [1,2,3,4,5]
print(f"Max Level: {max(levels)}")
print(f"Min Level: {min(levels)}")


# operator overloading

list1 = [1,2,3,4,5]
list2 = ["a","b"]

list3 = list1 + list2

print(f"List 3: {list3}")


list4 = ["thanos"]
list5 = list4 * 3
print(f"List 5: {list5}")

list6 = list2 * 3
print(f"List 6: {list6}")


raw_data = bytearray(b"Raw Data")

print(f"Raw Data is: {raw_data}") # Raw Data is: bytearray(b'Raw Data')

raw_data = raw_data.replace(b"Raw",b"Modified")
print(f"Raw Data is: {raw_data}") # Raw Data is: bytearray(b'Modified Data')