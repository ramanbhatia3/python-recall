# attribute shadowing

class Chai:
    temperature = "Hot"
    strength = "Strong"

cutting = Chai()
print(cutting.temperature)

cutting.temperature = "Mild"

print(cutting.temperature)
print(Chai.temperature)

del cutting.temperature

print(cutting.temperature)

cutting.cup = "Small"

print(cutting.cup)

del cutting.cup

print(cutting.cup)