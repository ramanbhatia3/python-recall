# if elif else

size = input("Enter your pizza size (small/medium/large): ").lower()

if size == "small":
    print("Price is 100 rupees")
elif size == "medium":
    print("Price is 250 rupees")
elif size == "large":
    print("Price is 500 rupees")
else:
    print("No such pizza!")