# self referencing models in pydantic

from typing import List, Optional
from pydantic import BaseModel, Field

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None

Comment.model_rebuild()  # Rebuild the model to resolve forward references

comment = Comment(
    id=1,
    content="This is a comment",
    replies=[
        Comment(
            id=2,
            content="This is a reply",
            replies=[
                Comment(
                    id=3,
                    content="This is a nested reply"
                )
            ]
        )
    ]
)

print(comment)