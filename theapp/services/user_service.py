from sqlalchemy.orm import Session
from fastapi import HTTPException
from utils.security import *
from models.user import *
from schemas.user import *

def user_reg (db: Session ,data: UserCreate) :
    exist_un = db.query(User).filter(User.username == data.username).first()
    exist_em = db.query(User).filter(User.email == data.email).first()

    if exist_un :
        raise HTTPException(
            status_code= 400,
            detail="username already existed")
    if exist_em :
        raise HTTPException(
            status_code= 400,
            detail="email already existed")
    
    new_user = User(
       username = data.username,
       email = data.email,
       hashed_password=hash_password(data.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def user_login (db: Session, data: UserLogin) :
    u = db.query(User).filter(User.email == data.email).first()
    if not u :
        raise HTTPException(
            status_code= 400,
            detail="Incorrect email or password")
    hpw = u.hashed_password
    if not check_password(data.password,hpw) :
        raise HTTPException(
            status_code=400,
            detail="Incorrect email or password"
        )
    return u