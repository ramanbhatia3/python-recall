# class

class Tea:
    pass

class TeaTime:
    pass

print(type(Tea))  # <class 'type'>

ginger_tea = Tea()
print(type(ginger_tea)) # <class '__main__.Chai'>

print(type(ginger_tea) is Tea)

print(type(ginger_tea) is TeaTime)



# namespace

class Chai:
    origin = "India" # properties

print(Chai.origin)

Chai.is_hot = True
print(Chai.is_hot)

# Creating object from class Chai

masala = Chai()
print(f"Masala {masala.origin}")
print(f"Masala {masala.is_hot}")

masala.is_hot = False

print(f"Masala {masala.is_hot}")

print(f"Chai {Chai.is_hot}")

masala.flavor = "Masala"
print(f"Masala {masala.flavor}")