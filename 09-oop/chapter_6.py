# accessing base class

# 1. Code Duplication
# 2. Explicit Call
# 3. super()

class Chai:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength


# 1. Code Duplication
# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         self.type = type_
#         self.strength = strength
#         self.spice_level = spice_level


# 2. Explicit Call
# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         Chai.__init__(self, type_, strength)
#         self.spice_level = spice_level


# 3. super()
class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        super().__init__(type_, strength)
        self.spice_level = spice_level



# Method Resolution Order (MRO)

class A:
    label = "A: Base Class"

class B(A):
    label = "B: Masala Chai"

class C(A):
    label = "C: Herbal Chai"

class D(B, C):
    pass

cup = D()
print(cup.label)

print(D.__mro__) # (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)