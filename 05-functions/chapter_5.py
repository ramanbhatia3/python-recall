# types of functions

# pure function
def pure_chai(cups):
    return cups*10


# impure functions (modifies something)

total_chai = 0

# not recommended
def impure_chai(cups):
    global total_chai
    total_chai += cups


# recursive function

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fact(n-1)
    
fact_of_5 = fact(5)

print(f"Factorial of 5 is {fact_of_5}")



# lambdas (anonymous function)
chai_types = ["light", "kadak", "masala", "kadak"]

strong_chai = list(filter(lambda chai: chai != "kadak", chai_types))

print(strong_chai)