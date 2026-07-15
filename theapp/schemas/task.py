from pydantic import BaseModel, ConfigDict
from enums.Taskstatus import TaskStatus



class TaskResp (BaseModel) :
    id : int
    title : str
    description : str | None = None
    status : TaskStatus
    model_config=ConfigDict(from_attributes=True)

class TaskCreate (BaseModel) :
    title : str
    description : str | None = None

class TaskUp (BaseModel) :
    title : str | None = None
    description : str | None = None
    status : TaskStatus | None = None