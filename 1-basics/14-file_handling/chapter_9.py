# Student Record System

while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")
    
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        with open("14-file_handling/students.txt", "a") as f:
            f.write(name + "\n")

    elif choice == "2":
        with open("14-file_handling/students.txt", "r") as f:
            print(f.read())

    elif choice == "3":
        break