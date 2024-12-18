from fastapi import APIRouter, Depends, HTTPException
from schemas import Clients
from sqlalchemy.orm import Session
from models import User, File_Model
from utils import send_verification_email, generate_secure_url
from database import get_db
import uuid
from oauth import createAccessToken, get_current_client_user
from passlib.context import CryptContext
from fastapi.security.oauth2 import OAuth2PasswordBearer



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")




@router.post("/client_signup")
async def sign_up(user: Clients, db: Session = Depends(get_db)):
    
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = pwd_context.hash(user.password)
    new_user = User(email=user.email, hashed_password=hashed_password, is_ops=0)
    db.add(new_user)
    db.commit()
    verification_url = f"http://192.168.1.9:8000/client/verify/{uuid.uuid4()}"
    

    send_verification_email(new_user.email, verification_url)

    return {"message": "User created successfully, please check your email for verification link"}



@router.get("/verify/{token}")
async def email_verify(token: str, db: Session = Depends(get_db)):
   return {"message": "Email verified successfully"}



@router.post("/client_login")
async def login(user: Clients, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not pwd_context.verify(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    
    token = createAccessToken(data={"sub": user.email, "role": "client"})
    return {"access_token": token, "token_type": "bearer"}



@router.get("/download-file/{file_id}")
async def download_file(file_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):

    user = get_current_client_user(token, db)  
    db_file = db.query(File_Model).filter(File_Model.id == file_id).first()
    if not db_file:
        raise HTTPException(status_code=404, detail="File not found")

    
    secure_url = generate_secure_url(file_id) 
    return {"download_link": secure_url, "message": "success"}
