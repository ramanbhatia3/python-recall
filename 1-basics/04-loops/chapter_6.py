# for else

staff = [("Amit", 17), ("Rahul",17),("Ridhima",15)]

for name,age in staff:
    if age >= 18:
        print(f"{name} is eligible to manage the staff")
        break
else:
    print("No one is eligible to manage the staff")