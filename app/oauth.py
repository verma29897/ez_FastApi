import os
from dotenv import load_dotenv
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException, Depends, status
from fastapi.security.oauth2 import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from database import get_db
from models import User
from schemas import TokenData




load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
oauth2_schema = OAuth2PasswordBearer(tokenUrl='login')




def createAccessToken(data: dict):
    to_encode = data.copy()
    expire_time = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp': expire_time})

    encoded_token = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return encoded_token



def verifyAccessToken(token: str, credentialException):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get('id')
        user_role = payload.get('role')

        if not user_id or not user_role:
            raise credentialException

        return TokenData(id=str(user_id), role=str(user_role))
    except JWTError:
        raise credentialException



def get_current_client_user(token: str = Depends(oauth2_schema), db: Session = Depends(get_db)):
    credException = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Unauthorized Access",
        headers={"WWW-Authenticate": "Bearer"}
    )

    token_data = verifyAccessToken(token, credException)

    user = db.query(User).filter(User.id == token_data.id).first()
    if not user:
        raise credException

    return user


def get_current_ops_user(db: Session = Depends(get_db)):
    user = db.query(User).filter(User.is_ops == 1).first()
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return user