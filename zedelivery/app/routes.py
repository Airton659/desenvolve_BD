from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Partner  # Modelo do banco de dados SQLAlchemy
from app.schema import PartnerCreate, PartnerResponse  # Usando Pydantic para entrada e saída
import uuid

router = APIRouter()

@router.post("/partners", response_model=PartnerResponse)
def create_partner(
    partner: PartnerCreate,  # O Pydantic para validação de entrada
    db: Session = Depends(get_db)
):
    new_partner = Partner(
        id=str(uuid.uuid4()),  # Gerando um UUID para o parceiro
        trading_name=partner.trading_name,
        owner_name=partner.owner_name,
        document=partner.document,
        coverage_area=partner.coverage_area,
        address=partner.address,
    )

    db.add(new_partner)
    db.commit()
    db.refresh(new_partner)
    
    return new_partner  # Retorna a resposta com o modelo de PartnerResponse

@router.get("/partners/{id}", response_model=PartnerResponse)
def get_partner(id: str, db: Session = Depends(get_db)):
    partner = db.query(Partner).filter(Partner.id == id).first()
    if not partner:
        raise HTTPException(status_code=404, detail="Partner not found")
    
    return partner  # Retorna o parceiro encontrado no banco
