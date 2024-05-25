from sqlalchemy.orm import Session
from schemas.seccion_schema import SeccionSchema
from models.seccion_models import SeccionModel

def get_seccion(db: Session, skip: int = 0, limit: int = 100):
    return db.query(SeccionModel).offset(skip).limit(limit).all()

def get_seccion_by_id(db: Session, seccion_id: int):
    return db.query(SeccionModel).filter(SeccionModel.id == seccion_id).first()

def create_seccion(db: Session, seccion: SeccionSchema):
    _seccion = SeccionModel(
        nombre=seccion.nombre,
        descripcion=seccion.descripcion
    )
    db.add(_seccion)
    db.commit()
    db.refresh(_seccion)
    return _seccion

def remove_seccion(db: Session, seccion_id: int):
    _seccion = get_seccion_by_id(db=db, seccion_id=seccion_id)
    if _seccion:
        db.delete(_seccion)
        db.commit()
    return _seccion

def update_seccion(db: Session, seccion_id: int, nombre: str, descripcion: str):
    _seccion = get_seccion_by_id(db=db, seccion_id=seccion_id)
    if _seccion:
        _seccion.nombre = nombre
        _seccion.descripcion = descripcion
        db.commit()
        db.refresh(_seccion)
    return _seccion
