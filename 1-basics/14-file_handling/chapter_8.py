# p1: count words in file

# with open("14-file_handling/file2.txt", "r") as f:
#     content = f.read()
#     words = content.split()
#     print("Total words:", len(words))



# p2: count lines

# with open("14-file_handling/file2.txt", "r") as f:
#     lines = f.readlines()
#     print("Total lines:", len(lines))



# p3: copy one file to another

with open("14-file_handling/file2.txt", "r") as source:
    data = source.read()

with open("14-file_handling/file3.txt", "w") as target:
    target.write(data)
