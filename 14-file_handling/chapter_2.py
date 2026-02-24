# write

f = open('14-file_handling/file2.txt','w')

f.write("This is a file\n")

f.write("Data is written")

f.close()

f = open('14-file_handling/file2.txt','r')

content = f.read()

print(content)

