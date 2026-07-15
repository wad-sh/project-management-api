from models.project import Project
from models.task import Task
from sqlalchemy.orm import Session

def proj_is_for_user (db: Session,user_id:int,proj_id:int) :
    pj = db.query(Project).filter(
        Project.id == proj_id,
        Project.owner_id == user_id
    ).first()
    
    return pj is not None
    

def is_this_task_for_proj (db: Session,proj_id:int,task_id: int) :
    tx = db.query(Task).filter(
        Task.id == task_id,
        Task.project_id == proj_id
    ).first()

    return tx is not None