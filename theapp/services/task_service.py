from sqlalchemy.orm import Session
from models.task import Task
from utils.taskstools import *
from schemas.task import *
from fastapi import HTTPException


def get_tasks(db: Session,proj_id:int,user_id:int) : 
    
    
    if not proj_is_for_user(db,user_id,proj_id) :
        raise HTTPException(
            status_code=409,
            detail="not allowed or project not found"
        )
    
    tasks = db.query(Task).filter(Task.project_id == proj_id).all()
    return tasks

def add_task(db: Session,user_id:int,proj_id:int,task_data: TaskCreate) : 
    if not proj_is_for_user(db,user_id,proj_id) :
        raise HTTPException(
            status_code=409,
            detail="not allowed or project not found"
        )
    new_task = Task(
        project_id = proj_id,
        title = task_data.title,
        description = task_data.description
        )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def up_task(db: Session,user_id:int,proj_id:int,task_id: int,task_data: TaskUp) : 
    if not proj_is_for_user(db,user_id,proj_id) :
        raise HTTPException(
                status_code=403,
                detail="not allowed or project not found"
            )
    
    if not is_this_task_for_proj(db,proj_id,task_id):
        raise HTTPException(
            status_code=403,
            detail="not allowed or task not found"
        )

    if task_data.title is None and task_data.description is None and task_data.status is None :
        raise HTTPException(
                status_code=400,
                detail="no change"
            )

    tsk = db.query(Task).filter(Task.id == task_id).first()
    
    if task_data.title is not None :
        tsk.title =task_data.title
    if task_data.description is not None :
        tsk.description =task_data.description
    if task_data.status is not None :
        tsk.status =task_data.status

    db.commit()
    db.refresh(tsk)
        

    return tsk


def delete_task(db: Session,user_id:int,proj_id:int,task_id: int) : 
    if not proj_is_for_user(db,proj_id,user_id) :
        raise HTTPException(
                status_code=409,
                detail="not allowed or project not found"
            )
    
    if not is_this_task_for_proj(db,proj_id,task_id):
        raise HTTPException(
            status_code=409,
            detail="not allowed or task not found"
        )
    
    tsk = db.query(Task).filter(Task.id == task_id).first()

    db.delete(tsk)
    db.commit()

    return tsk