# Integer

apples = 10
bananas = 5

fruits = apples + bananas

print(f"Fruits: {fruits}")


milk_litres = 10
servings = 7

milk_per_serving = milk_litres / servings

print(f"Milk per serving is {milk_per_serving}")


bottles = 7
bags = 4

bottles_per_bag = bottles // bags

print(f"Bottles per bag: {bottles_per_bag}")


left_bottles = bottles % bags

print(f"Bottles left: {left_bottles}")


base = 2
power = 3
answer = base ** power

print(f"Answer: {answer}")


billion = 1_000_000_000 # improves readability
print(f"Billion: {billion}")




# Boolean

answerTrue = True
count = 5

new_number = count + answerTrue # upcasting

print(f"New Number: {new_number}")


present = 0
print(f"Are you present? {bool(present)}")

# 0 - False
# 1 - True
# 12 - True
# "Raman" - True
# None - False



isTrue = 1
isFalse = 0

logicAnd = isTrue and isFalse
print(f"And: {logicAnd}")

logicOr = isTrue or isFalse
print(f"Or: {logicOr}")

logicNot = not isTrue
print(f"Not: {logicNot}")




# Floating

temp1 = 95.7
temp2 = 95.69
print(f"Temperature 1: {temp1}")
print(f"Temperature 2: {temp2}")
print(f"Temperature Difference: {temp1 - temp2}")