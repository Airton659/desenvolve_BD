from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Partner
from app.schema import PartnerCreate, Partner as PartnerSchema  
from sqlalchemy import func
import json

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
def get_partner(id: int, db: Session = Depends(get_db)):
    partner = db.query(Partner).filter(Partner.id == id).first()

    if not partner:
        raise HTTPException(status_code=404, detail="Parceiro não encontrado")
    
    return partner

@router.get("/closest", response_model=PartnerSchema)
def get_closest_partner(lat: float, lon: float, db: Session = Depends(get_db)):
    # Criar o ponto GeoJSON com as coordenadas fornecidas
    point = json.dumps({"type": "Point", "coordinates": [lon, lat]})  # Converte para string

    # Consultar o parceiro mais próximo que tenha a localização dentro da área de cobertura
    closest_partner = db.query(Partner).filter(
        func.ST_Within(
            func.ST_GeomFromGeoJSON(Partner.coverageArea),  # coverageArea como string GeoJSON
            func.ST_GeomFromGeoJSON(point)  # ponto também como string GeoJSON
        )
    ).order_by(
        func.ST_Distance(
            func.ST_GeomFromGeoJSON(point),  # ponto como string GeoJSON
            func.ST_GeomFromGeoJSON(Partner.address)  # address como string GeoJSON
        )
    ).first()

    # Se não encontrar parceiro, retornar erro
    if not closest_partner:
        raise HTTPException(status_code=404, detail="Nenhum parceiro encontrado na área de cobertura.")

    return closest_partner

