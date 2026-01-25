# input parameters / handling arguments

def make_project(frontend, backend, database):
    print(f"Frontend: {frontend}")
    print(f"Backend: {backend}")
    print(f"Database: {database}")

make_project("html","node","mongodb") # positional

make_project(backend="springboot",database="mongodb",frontend="react") # keywords



def special_chai(*ingredients, **extras):  # (*args,**kwargs)
    print(f"Ingredients: {ingredients}")
    print(f"Extras: {extras}")

special_chai("Masala","Ginger",sweetner="Honey",foam="Yes")




# def chai_order(order=[]):
#     order.append("Masala Chai")
#     print(order)

def chai_order(order=None):
    if order is None:
        order = []
    print(order)

chai_order()
chai_order()