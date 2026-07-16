from fastapi import APIRouter, Depends
from schemas.project import *
from database.database import get_db
from services.project_service import *
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)

@router.get("",response_model= List[ProjResp])
def get_pjs (user_id:int,db: Session = Depends(get_db)) :
    return get_projects(db, user_id)

@router.post("",response_model= ProjResp)
def add_proj (user_id:int, data: ProjCreate, db: Session = Depends(get_db)) :
    return create_p(db,data ,user_id)

@router.put("/{id}",response_model= ProjResp)
def update_pj (id: int , user_id: int , data: ProjUp , db: Session = Depends(get_db)) :
    return update_p(db,data,id,user_id)

@router.delete ("/{id}",response_model=ProjResp)
def delete_pj (id: int , user_id: int, db: Session = Depends(get_db)) :
    return delete_p(db,id,user_id)
    
