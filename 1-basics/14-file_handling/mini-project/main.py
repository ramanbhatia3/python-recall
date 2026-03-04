from pathlib import Path

def reafFileAndFolder():
    path = Path("")
    items = list(path.rglob("*"))
    for i, items in enumerate(items):
        print(f"{i+1}: {items}")

def createFile():
    try:
        reafFileAndFolder()
        name = input("Enter the name of the file to be created: ")
        p = Path(name)
        if not p.exists() or p.is_file():
            with open(p, "w") as fs:
                data = input("What do you want to write in the file?: ")
                fs.write(data)
            print("File created successfully!")
        else:
            print("This file already exists!")

    except Exception as err:
        print(f"An error has occurred as {err}")


def readFile():
    try:
        reafFileAndFolder()
        name = input("Enter file name to read: ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,"r") as fs:
                data = fs.read()
                print(data)
            print("File reading successful")
        else:
            print("File does not exists!")

    except Exception as err:
        print(f"An error has occurred as {err}")


def updateFile():
    try:
        reafFileAndFolder()
        name = input("Enter file name to update: ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Press 1 for changing the name of file")
            print("Press 2 for overwritting the data of your file")
            print("Press 3 for appending some data in your file")

            response = int(input("Enter your choice for updation: "))

            if response == 1:
                f_name = input("Enter the new file name: ")
                p2 = Path(f_name)
                p.rename(p2)

            if response == 2:
                with open(p,"w") as fs:
                    data = input("Enter content to over-write into the file: ")
                    fs.write(data)

            if response == 3:
                with open(p,"a") as fs:
                    data = input("Enter content to append into the file: ")
                    fs.write(" " + data)

    except Exception as err:
        print(f"An error has occurred as {err}")

def deleteFile():
    try:
        reafFileAndFolder()
        name = input("Enter the name of the file you want to delete: ")
        p = Path(name)

        if p.exists() and p.is_file():
            p.unlink()
            print("File deleted successfully")
        else:
                print("File does not exist!")

    except Exception as err:
        print(f"An error has occurred as {err}")




print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file")

choice = int(input("Enter your choice: "))

if choice == 1:
    createFile()

if choice == 2:
    readFile()

if choice == 3:
    updateFile()

if choice == 4:
    deleteFile()