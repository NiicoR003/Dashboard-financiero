from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware 
from sqlalchemy.orm import Session
from database import engine, SessionLocal
from schemas import TransaccionCreate, TransaccionResponse
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"mensaje": "API funcionando"}

@app.post("/transacciones", response_model=TransaccionResponse)
def crear_transaccion(trasaccion: TransaccionCreate, db: Session = Depends(get_db)):
    nueva = models.Transaccion(**trasaccion.model_dump())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

@app.get("/transacciones", response_model=list[TransaccionResponse])
def obtener_transacciones(db: Session = Depends(get_db)):
    return db.query(models.Transaccion).all()