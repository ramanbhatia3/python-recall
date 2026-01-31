# file handling with try except and with

# try:
#     file = open("order.txt","w")
# finally:
#     file.write("Masala Chai - 2 Cups")

with open("order.txt","w") as file:
    file.write("Ginger Tea - 4 Cups")


# file.__enter__()
# file.__exit__()