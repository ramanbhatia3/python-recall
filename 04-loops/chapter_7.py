# walrus operator :=

# value = 13

# remainder = value % 5

# if remainder:
#     print(f"Not Divisible, Remainder is {remainder}")



value = 13

if (remainder := value % 7):
    print(f"Not Divisible, Remainder is {remainder}")


sizes = ["small", "medium", "large"]

if (requested_size := input("Enter your shirt size: ").lower()) in sizes:
    print(f"{requested_size} size shirt is available")
else:
    print(f"{requested_size} size shirt is not available")



flavors = ["mango", "litchi", "lemon", "masala"]

print("Avaialable Flavours: ",flavors)

while (flavor := input("Enter a flavor: ").lower()) not in flavors:
    print(f"Sorry! {flavor} is not available")


print(f"You choose {flavor} cold drink")