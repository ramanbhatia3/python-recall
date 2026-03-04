# custom exceptions

# def brew_chai(flavor):
#     if flavor not in ["masala", "ginger", "elaichi"]:
#         raise ValueError("Unsupported Chai Flavor")
#     print(f"Brewing {flavor} chai....")

# brew_chai("mint")


class OutOfIngredientsError(Exception):
    pass

def make_chai(milk, sugar):
    if milk == 0 or sugar == 0:
        raise OutOfIngredientsError("Missing Milk or Sugar")
    print("Chai is ready!")

make_chai(0,1)