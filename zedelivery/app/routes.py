from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Partner
from app.schema import PartnerCreate, Partner as PartnerSchema  


router = APIRouter()

@router.post("/partners", response_model=PartnerSchema)  
def create_partner(partner: PartnerCreate, db: Session = Depends(get_db)):
    new_partner = Partner(
        tradingName=partner.tradingName,  
        ownerName=partner.ownerName,
        document=partner.document,
        coverageArea=partner.coverageArea,  
        address=partner.address,  
    )

    db.add(new_partner)
    db.commit()
    db.refresh(new_partner)
    return new_partner

@router.get("/partners/{id}", response_model=PartnerSchema)
def get_partner(id:int, db: Session = Depends(get_db)):
    partner = db.query(Partner).filter(Partner.id == id).first()

    if not partner:
        raise HTTPException(status_code=404, detail="Parceiro não encontrado")
    
    return partner