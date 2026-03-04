# if else

snack = input("Enter your snack: ").lower()

# print(f"User asked for a {snack}")

if snack == "cookies" or snack == "samosa":
    print(f"great choice! We'll serve you a {snack}")
else:
    print(f"Sorry! {snack} is not available currently")