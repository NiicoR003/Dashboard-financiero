from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from database import Base

class Transaccion(Base):
    __tablename__= "transacciones"

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String)
    monto = Column(Float)
    categoria = Column(String)
    fecha = Column(DateTime, default=datetime.now)



