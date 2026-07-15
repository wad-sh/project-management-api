from sqlalchemy.orm import Session
from models.project import *
from schemas.project import *
from fastapi import HTTPException

def create_p (db: Session , data: ProjCreate, user_id: int ):
    new_proj = Project(
        owner_id =user_id ,
        title = data.title,
        description = data.description
    )

    db.add(new_proj)
    db.commit()
    db.refresh(new_proj)
    return new_proj


def update_p (db: Session , data: ProjUp, id: int, user_id : int ) :
    pj = db.query(Project).filter(Project.id == id).first()
    if not pj :
        raise HTTPException (
            status_code=404,
            detail="no project has been found"
        )
    if pj.owner_id != user_id :
        raise HTTPException (
            status_code=403,
            detail="not allowed"
        )
    if data.title is None and data.description is None :
        raise HTTPException (
            status_code=400,
            detail="no change"
        )
    
    if data.title is not None :
        pj.title = data.title

    if data.description is not None :
        pj.description = data.description

    db.commit()
    db.refresh(pj)
    return pj

def delete_p (db:Session, id: int, user_id:int) :
    pj = db.query(Project).filter(Project.id == id).first()
    if not pj :
        raise HTTPException (
            status_code=404,
            detail="no project has been found"
        )
    if pj.owner_id != user_id :
        raise HTTPException (
            status_code=403,
            detail="not allowed")
    
    db.delete(pj)
    db.commit()
    return pj

def get_projects(db:Session, user_id:int) :
    pjs = db.query(Project).filter(Project.owner_id == user_id).all()
    if not pjs :
        return []
    return pjs

