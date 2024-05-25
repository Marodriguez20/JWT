from sqlalchemy import Column, Integer, String
from core.config import Base


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)  # Especificando longitud para VARCHAR
    password = Column(String(255))