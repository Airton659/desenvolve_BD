from sqlalchemy import Column, String, JSON
from app.database import Base  # Certifique-se de que 'Base' está sendo importado corretamente do seu 'database.py'

class Partner(Base):
    __tablename__ = "partners"

    id = Column(String(36), primary_key=True, index=True)
    trading_name = Column(String(255), index=True)
    owner_name = Column(String(255))
    document = Column(String(20), unique=True, index=True)
    coverage_area = Column(JSON)
    address = Column(JSON)
