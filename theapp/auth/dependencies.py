from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from auth.jwt_handler import verify_token
from models.user import User


tok_reader = OAuth2PasswordBearer(
    tokenUrl="/users/login"
)

def get_curr_u (
        token: str = Depends (tok_reader),
        db: Session = Depends(get_db)
) :
    payload = verify_token(token)

    if payload is None :
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )
    

    u_id = payload.get("sub")

    if u_id is None :
        raise HTTPException (
            status_code= 401,
            detail="invalid token data"
        )
    

    #return the user itself for later updates
    user = db.query(User).filter (User.id == int(u_id)).first()

    if user is None :
        raise HTTPException (
            status_code=404,
            detail= "user not found"
        )
    
    return user