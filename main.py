from fastapi import FastAPI
import uvicorn
from core.config import engine
import core.config as model

from routes.seccion_routes import router as secc
from routes.libros_routes import router as libr
from routes.user_routes import router as user_routes

from fastapi.middleware.cors import CORSMiddleware


model.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="MACKEUP",
    description="Desarrolo Web - FastAppi",
    version="1.0.0"
)

origin = [
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def index():
    return {
        "message": "Bienvenidos"
    }


app.include_router(router=secc, tags=['seccion'], prefix='/seccion')
app.include_router(router=libr, tags=["Libros"], prefix="/libros")
app.include_router(router=user_routes, tags=['Users'], prefix='/users')

if __name__ == "__main__":
    uvicorn.run("main:app",
                host="localhost",
                reload=True)