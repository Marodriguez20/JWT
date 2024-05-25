from sqlalchemy import Column, Integer, String
from core.config import Base

class LibroModel(Base):
    __tablename__ = 'libros'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    genero = Column(String)