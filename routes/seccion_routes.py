from fastapi import APIRouter
from fastapi import Depends
from schemas.seccion_schema import SeccionSchema
from schemas.apischema import Response
from services import seccion_services as crud
from core.config import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post('/create')
async def create_seccion_service(request: SeccionSchema, db: Session = Depends(get_db)):
    crud.create_seccion(db, seccion=request)
    return Response(
        status="Ok",
        code="200",
        message="Sección creada exitosamente",
        result=request
    ).dict(exclude_none=True)

@router.get("/")
async def get_secciones(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _secciones = crud.get_seccion(db, skip, limit)
    return Response(
        status="Ok",
        code="200",
        message="Datos obtenidos con éxito",
        result=_secciones
    )

@router.patch("/update")
async def update_seccion(request: SeccionSchema, db: Session = Depends(get_db)):
    try:
        _seccion = crud.update_seccion(db, seccion_id=request.id,
                                       nombre=request.nombre, descripcion=request.descripcion)
        return Response(
            status="Ok",
            code="200",
            message="Datos actualizados con éxito",
            result=_seccion
        )
    except Exception as e:
        return Response(
            status="Error",
            code="304",
            message="La actualización falló"
        )

@router.delete("/delete")
async def delete_seccion(request: SeccionSchema, db: Session = Depends(get_db)):
    try:
        crud.remove_seccion(db, seccion_id=request.id)
        return Response(
            status="Ok",
            code="200",
            message="Datos eliminados con éxito"
        ).dict(exclude_none=True)
    except Exception as e:
        return Response(
            status="Error",
            code="",
            message="La eliminación falló"
        )
