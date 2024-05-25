from sqlalchemy.orm import Session
from schemas.libros_schema import LibroSchema
from models.libro_models import LibroModel

def get_libro(db: Session, skip: int = 0, limit: int = 100):
    return db.query(LibroModel).offset(skip).limit(limit).all()

def get_libro_by_id(db: Session, libro_id: int):
    return db.query(LibroModel).filter(LibroModel.id == libro_id).first()

def create_libro(db: Session, libro: LibroSchema):
    _libro = LibroModel(
        nombre=libro.nombre,
        genero=libro.genero
    )
    db.add(_libro)
    db.commit()
    db.refresh(_libro)
    return _libro

def remove_libro(db: Session, libro_id: int):
    _libro = get_libro_by_id(db=db, libro_id=libro_id)
    if _libro:
        db.delete(_libro)
        db.commit()
    return _libro

def update_libro(db: Session, libro_id: int, nombre: str, genero: str):
    _libro = get_libro_by_id(db=db, libro_id=libro_id)
    if _libro:
        _libro.nombre = nombre
        _libro.genero = genero
        db.commit()
        db.refresh(_libro)
    return _libro
