# mixing pydantic and typing 

from pydantic import BaseModel
from typing import List, Dict, Optional

class Cart(BaseModel):
    user_id: int
    items: List[str]
    quantities: Dict[str, int]

class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None

    
cart_data = {
    "user_id": 123,
    "items": ["apple", "banana", "orange"],
    "quantities": {"apple": 2, "banana": 3, "orange": 1}
}

cart = Cart(**cart_data)