from pydantic import BaseModel, ConfigDict

class ProjResp (BaseModel) :
    id : int
    title : str
    description : str | None = None
    model_config = ConfigDict(from_attributes=True)

class ProjCreate (BaseModel) :
    title : str
    description : str | None = None

class ProjUp (BaseModel) :
    title : str | None = None
    description : str | None = None

