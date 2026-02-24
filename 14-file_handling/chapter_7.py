# Exception Handling in File Handling

# try:
#     f = open("data.txt", "r")
#     print(f.read())
# except FileNotFoundError:
#     print("File does not exist")



# better way

try:
    with open("data.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")