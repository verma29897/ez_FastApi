from pydantic import BaseModel
class Users(BaseModel):
    email: str
    password: str

class TokenData(BaseModel):
    id: str
    role: str
    
    
class Clients(BaseModel):
    email: str
    password: str