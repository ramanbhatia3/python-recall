# scopes

def serve_chai():
    chai_type = "Masala" # local scope
    print(f"Inside Function: {chai_type} Chai")

chai_type = "Lemon"
serve_chai()
print(f"Outside Function: {chai_type} Chai")



def flavor():
    fruit = "Mango"
    def get_juice():
        fruit = "Lemon"
        print(f"Serving {fruit} juice (INSIDE)")
    get_juice()
    print(f"Serving {fruit} juice (OUTSIDE)")

flavor()

fruit = "Pineapple"
print(f"Serving {fruit} juice (GLOBAL)")


# nonlocal -> looks for variable just in the upper function

def order_juice():
    juice = "Orange"
    def another_juice():
        nonlocal juice
        juice = "Kiwi"
    another_juice()
    print(f"Serving {juice} juice")

order_juice()

# global -> looks for variable in the whole code

burger = "Veg"

def order_burger():
    def another_burger():
        global burger
        burger = "Cheese"
    another_burger()
    print(f"Serving {burger} burger")

order_burger()