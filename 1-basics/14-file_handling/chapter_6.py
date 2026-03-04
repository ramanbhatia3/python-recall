f = open("14-file_handling/file2.txt", "r")

print(f.tell())

f.read(5)
print(f.tell())

f.seek(0)
print(f.read(5))

f.close()