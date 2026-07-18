from fastapi import APIRouter, Depends
from schemas.project import *
from database.database import get_db
from services.project_service import *
from sqlalchemy.orm import Session
from auth.dependencies import get_curr_u
from models.user import User
from typing import List

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)

@router.get("",response_model= List[ProjResp])
def get_pjs (crr_u: User = Depends(get_curr_u)
             ,db: Session = Depends(get_db)) :
    return get_projects(db, crr_u.id)

@router.post("",response_model= ProjResp)
def add_proj (data: ProjCreate, crr_u: User = Depends(get_curr_u) , db: Session = Depends(get_db)) :
    return create_p(db,data ,crr_u.id)

@router.put("/{id}",response_model= ProjResp)
def update_pj (id: int , data: ProjUp ,  crr_u: User = Depends(get_curr_u), db: Session = Depends(get_db)) :
    return update_p(db,data,id,crr_u.id)

@router.delete ("/{id}",response_model=ProjResp)
def delete_pj (id: int , crr_u: User = Depends(get_curr_u), db: Session = Depends(get_db)) :
    return delete_p(db,id,crr_u.id)
    
