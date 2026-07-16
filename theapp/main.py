from fastapi import FastAPI
from database.database import Base , engine
from routers.user_router import router as user_router
from routers.project_router import router as project_router
from routers.task_router import router1, router2

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(project_router)
app.include_router(router1)
app.include_router(router2)