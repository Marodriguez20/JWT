from typing import Optional
from pydantic import BaseModel

class SeccionSchema(BaseModel):
    id_genero: Optional[int] = None
    descripcion: Optional[str] = None
    subgenero: Optional[str] = None

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id_genero": 1,
                "descripcion": "Harry Potter",
                "subgenero": "Fantasia"
            }
        }
