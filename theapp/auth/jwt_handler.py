from jose import jwt,JWTError
from datetime import datetime,timedelta,timezone
from config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

def create_access_token(data: dict) :
    to_enc = data.copy()
    exp = datetime.now(timezone.utc) + timedelta (minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_enc.update({
        "exp" : exp
    })
    token = jwt.encode(
        to_enc,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    return token

def verify_token (token: str) :
    try:
        dec = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return dec
    except JWTError:
        return None

