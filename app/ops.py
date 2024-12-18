from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from models import File_Model,User
from database import  get_db
from schemas import Users
from passlib.context import CryptContext
from utils import allowed_file_types, save_file_to_disk
from oauth import get_current_ops_user
router = APIRouter()




pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


    
@router.post("/users/")
def create_user(user: Users, db: Session = Depends(get_db)):
    
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    
    hashed_password = pwd_context.hash(user.password)

    new_user = User(email=user.email, hashed_password=hashed_password, is_ops=1)  

    db.add(new_user)
    try:
        db.commit()
        db.refresh(new_user)
    except Exception as e:
        db.rollback()  
        raise HTTPException(status_code=500, detail="Database error: " + str(e))

    return {"id": new_user.id, "email": new_user.email, "is_ops": new_user.is_ops}


@router.post("/upload")
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db), current_user: User = Depends(get_current_ops_user)):
    
    if file.content_type not in allowed_file_types:
        raise HTTPException(status_code=400, detail="File type not allowed")
    
    saved_file_path = save_file_to_disk(file)
    
    new_file = File_Model(name=file.filename, path=saved_file_path, owner_id=current_user.id)
    db.add(new_file)
    db.commit()
    db.refresh(new_file)
    
    return {"message": "File uploaded successfully", "file_id": new_file.id}
