from fastapi import APIRouter, Depends
from schemas.task import *
from database.database import get_db
from services.task_service import *
from sqlalchemy.orm import Session
from typing import List
from auth.dependencies import get_curr_u
from models.user import User

router1 = APIRouter(
    prefix="/projects/{proj_id}/tasks",
    tags=["Tasks"]
)

router2 = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

@router1.get("",response_model=list[TaskResp])
def get_t (proj_id:int,crr_u: User = Depends(get_curr_u),db: Session =Depends (get_db)) :
    return get_tasks(db,proj_id,crr_u.id)

@router1.post("",response_model=TaskResp)
def add_t (proj_id:int,data: TaskCreate ,crr_u: User = Depends(get_curr_u), db: Session=Depends (get_db)) :
    return add_task(db,crr_u.id,proj_id,data)

@router2.put("/{task_id}", response_model=TaskResp)
def update_t(
    task_id:int,
    task_data:TaskUp,
    crr_u: User = Depends(get_curr_u),
    db:Session=Depends(get_db)):
    return up_task(db,crr_u.id,task_id,task_data)

@router2.delete("/{task_id}", response_model=TaskResp)
def delete_t(
    task_id:int,
    crr_u: User = Depends(get_curr_u),
    db:Session=Depends(get_db)):
    return delete_task(db,crr_u.id,task_id)