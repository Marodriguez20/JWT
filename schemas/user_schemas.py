from pydantic import BaseModel
from typing import Optional


class UserSchema(BaseModel):
    id: Optional[int] = None
    email: Optional[str] = None
    password: Optional[str] = None

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "email": "Rodriguezarizamarlon@gmail.com",
                "password": "2001"
            }
        }