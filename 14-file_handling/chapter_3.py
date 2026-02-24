# append

f = open('14-file_handling/file2.txt','a')

f.write("\nData has been updated")

f.write("\nAnother line added.")

f.close()

f = open('14-file_handling/file2.txt','r')

content = f.read()

print(content)