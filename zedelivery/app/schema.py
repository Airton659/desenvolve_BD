from pydantic import BaseModel
from typing import Dict, Any


class PartnerBase(BaseModel):
    tradingName: str  
    ownerName: str
    document: str
    coverageArea: Dict[str, Any]  
    address: Dict[str, Any]

    class Config:
        orm_mode = True  


class PartnerCreate(PartnerBase):
    pass


class Partner(PartnerBase):
    id: int  

    class Config:
        orm_mode = True  
