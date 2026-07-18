from fastapi import APIRouter, Depends
from schemas.user import *
from database.database import get_db
from services.user_service import user_reg,user_login
from sqlalchemy.orm import Session
from schemas.token import Token

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/register", response_model = UserResponse) 
def register (data: UserCreate,
              db: Session = Depends(get_db)) :
    return user_reg(db,data)

@router.post("/login", response_model= Token) 
def login (
    data: UserLogin,
    db: Session = Depends(get_db)
) :
    return user_login(db, data)
