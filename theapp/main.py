from fastapi import FastAPI
from models import user
from models import project
from models import task
from database import Base , engine

app = FastAPI()

Base.metadata.create_all(bind=engine)