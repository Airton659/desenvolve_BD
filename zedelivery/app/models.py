from sqlalchemy import Column, String, Integer, JSON
from app.database import Base

class Partner(Base):
    __tablename__ = "partners"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tradingName = Column(String(255), index=True)  
    ownerName = Column(String(255))
    document = Column(String(20), unique=True, index=True)
    coverageArea = Column(JSON)  
    address = Column(JSON)
