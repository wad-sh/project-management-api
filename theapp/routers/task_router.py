from fastapi import APIRouter, Depends
from schemas.task import *
from database.database import get_db
from services.task_service import *
from sqlalchemy.orm import Session
from typing import List

router1 = APIRouter(
    prefix="/projects/{proj_id}/tasks",
    tags=["Tasks"]
)

router2 = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

@router1.get("",response_model=list[TaskResp])
def get_t (proj_id:int,user_id:int,db: Session =Depends (get_db)) :
    return get_tasks(db,proj_id,user_id)

@router1.post("",response_model=TaskResp)
def add_t (proj_id:int,user_id:int, data: TaskCreate ,db: Session=Depends (get_db)) :
    return add_task(db,user_id,proj_id,data)

@router2.put("/{task_id}", response_model=TaskResp)
def update_t(
    task_id:int,
    user_id:int,
    task_data:TaskUp,
    db:Session=Depends(get_db)):
    return up_task(db,user_id,task_id,task_data)

@router2.delete("/{task_id}", response_model=TaskResp)
def delete_t(
    task_id:int,
    user_id:int,
    db:Session=Depends(get_db)):
    return delete_task(db,user_id,task_id)