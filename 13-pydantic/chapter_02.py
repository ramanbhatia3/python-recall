# pydantic default conversions

from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True


product_one = Product(id=1, name="Laptop", price="50000", in_stock=True)

product_two = Product(id=2, name="Smartphone", price=30000)

# product_three = Product(name="Headphones")

# always use type notations

# int, float, str, bool, etc

# set sensible defaults



# pydantic 'can' convert data types but it is always better to provide the correct data types in the first place

# common conversions:
# "123" -> 123
# "true" -> True
# "50000" -> 50000.0