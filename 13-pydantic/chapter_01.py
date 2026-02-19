# pydantic

# 1. data validation
# data parsing and validation
# api development
# config management
# data serialization and deserialization

# 2. settings management 



from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool

input_data = {"id": 123, "name": "Raman", "is_active": True}

user = User(**input_data)

print(user)


# steps

# import BaseModel
# Type Annotation
# Model init (always unpack the dictionary)
# automatic validation