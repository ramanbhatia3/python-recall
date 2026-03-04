# zip

names = ["Raman", "Mohit", "Amit", "John"]
fees = [75000, 60000, 120000, 80000]

for i in zip(names, fees):
    print(i)

for name, fee in zip(names, fees):
    print(f"{name} paid {fee} rupees")