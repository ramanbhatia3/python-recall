# model dump and model dump json in serialization of pydantic

from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime


class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: str
    name: str
    email: str
    is_active: bool = True
    created_at: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')},
    )

user = User(
    id="1",
    name="Raman",
    email="raman@example.com",
    created_at=datetime(2026, 2, 19, 12, 0, 0),
    address=Address(street="123 Something", city="Hoshiarpur", zip_code="100001"),
    is_active=False,
    tags=["premium", "subscriber"]
)

print(user)
print("="*30)

python_dict = user.model_dump()  # returns a dictionary representation of the model

print(python_dict)

print("="*30)

json_str = user.model_dump_json()  # returns a JSON string representation of the model

print(json_str)