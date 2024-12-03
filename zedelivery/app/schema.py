from pydantic import BaseModel
from typing import Dict, Any

# A classe base para os dados do parceiro
class PartnerBase(BaseModel):
    trading_name: str
    owner_name: str
    document: str
    coverage_area: Dict[str, Any]
    address: Dict[str, Any]

# Usada para criação de novo parceiro
class PartnerCreate(PartnerBase):
    pass

# Modelo para a resposta, incluindo o ID
class PartnerResponse(PartnerBase):
    id: str

    class Config:
        orm_mode = True  # Isso garante que o Pydantic saiba como lidar com modelos SQLAlchemy
