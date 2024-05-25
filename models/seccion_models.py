from sqlalchemy import Column, Integer, String
from core.config import Base


class SeccionModel(Base):
    __tablename__ = 'secciones'

    id_genero = Column(Integer, primary_key=True)
    descripcion = Column(String)
    subgenero = Column(String)