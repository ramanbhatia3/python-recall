# binary files

with open("14-file_handling/image.jpg", "rb") as f:
    data = f.read()
    print(data)

with open("copy.jpg", "wb") as f:
    f.write(data)