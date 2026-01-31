# try except else and finally

menu = {"Burger":40, "Wrap":100}

try:
    menu["Pizza"]
except KeyError:
    print("Key that you're trying to access does not exists")

print("Hello World!")



def serve_chai(flavor):
    try:
        print(f"Preparing {flavor} chai...")
        if flavor == "unknown":
            raise ValueError("We don't know that flavor")
    except ValueError as e:
        print("Error", e)
    else:
        print(f"{flavor} chai is served!")
    finally:
        print("Next Customer Please..!!")

serve_chai("Masala")
serve_chai("unknown")