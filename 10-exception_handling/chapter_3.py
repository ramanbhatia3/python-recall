# catching multiple exception

def process_order(item, quantity):
    try:
        price = {"Masala": 20}[item]
        cost = price * quantity
        print(f"Total cost is {cost}")
    except KeyError as e:
        print("Sorry that chai is not on menu")
    except TypeError:
        print("Quantity must be in number")

# process_order("ginger",2)
process_order("Masala","two")