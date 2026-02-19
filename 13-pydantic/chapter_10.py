# advance nested model patterns

from pydantic import BaseModel
from typing import Optional, List, Union

class Address(BaseModel):
    street: str
    city: str
    country: str

# Optional Nested Models
class Company(BaseModel):
    name: str
    address: Optional[Address] = None

class Employee(BaseModel):
    name: str
    company: Optional[Company] = None

class TextContent(BaseModel):
    type: str = "text"
    content: str

class ImageContent(BaseModel):
    type: str = "image"
    url: str
    alt_text: str

# Mixed Data Types
class Article(BaseModel):
    title: str
    section: List[Union[TextContent, ImageContent]]

# Deeply Nested Structure
class Country(BaseModel):
    name: str
    code: str

class State(BaseModel):
    name: str
    country: Country

class City(BaseModel):
    name: str
    state: State

class Address(BaseModel):
    street: str
    city: City
    postal_code: str

class Organisation(BaseModel):
    name: str
    head_quarters: Address
    branches: List[Address] =[]