from fastapi import APIRouter, Depends
from schemas.user import *
from database.database import get_db
from services.user_service import *
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/register", response_model = UserResponse) 
def register (data: UserCreate,
              db: Session = Depends(get_db)) :
    return user_reg(db,data)

@router.post("/login", response_model= UserResponse) 
def login (
    data: UserLogin,
    db: Session = Depends(get_db)
) :
    return user_login(db, data)
