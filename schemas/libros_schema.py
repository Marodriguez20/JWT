from typing import Optional
from pydantic import BaseModel

class LibroSchema(BaseModel):
    id: Optional[int] = None
    nombre: Optional[str] = None
    genero: Optional[str] = None

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "nombre": "Harry Potter",
                "genero": "Fantasia"
            }
        }
