from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Configuración de la conexión
DATABASE_URL = 'mysql+pymysql://root:@localhost/biblioteca'

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL, echo=True)

# Crear una sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para declarar modelos
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
