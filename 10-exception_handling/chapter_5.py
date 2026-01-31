# mini project

class InvalidChaiError(Exception): pass

def bill(flavor, cups):
    menu = {"Masala":20, "Ginger":25}
    try:
        if flavor not in menu:
            raise InvalidChaiError("That chai is not available")
        if not isinstance(cups, int):
            raise TypeError("Number of cups must be in integer")
        total = menu[flavor] * cups
        print(f"Your bill for {cups} cups of {flavor} chai is Rs.{total}")
    except Exception as e:
        print("Error: ",e)
    finally:
        print("Thank You For Visiting")

bill("Mint", 2)
bill("Masala", "three")
bill("Ginger", 3)