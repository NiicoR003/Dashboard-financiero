from pydantic import BaseModel
from datetime import datetime

class TransaccionCreate (BaseModel):
    tipo: str
    monto: float
    categoria: str

class TransaccionResponse (BaseModel):
    id: int
    tipo: str
    monto: float
    categoria: str
    fecha: datetime

    class Config:
        from_attributes = True