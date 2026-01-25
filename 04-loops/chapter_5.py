# break and continue

names = ["Raman", "Mohit", "No Name", "Amit", "Exit", "John"]

for name in names:
    if name == "No Name":
        continue
    if name == "Exit":
        break
    print(f"{name}'s turn")

print("Out of the loop")