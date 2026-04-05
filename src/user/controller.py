from src.user.dtos import UserSchema
from sqlalchemy.orm import Session
from src.user.models import UserModel
from fastapi import HTTPException
from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

def get_password_hash(password):
    return password_hash.hash(password)

def register(body:UserSchema,db:Session):
    is_user = db.query(UserModel).filter(UserModel.username == body.username).first()
    print("is_user :",is_user)
    if is_user:
        raise HTTPException(400,detail="Username already exist...")
        
    is_user = db.query(UserModel).filter(UserModel.email == body.email).first()
    print("asssssssssssssssssss",is_user)
    if is_user:
        raise HTTPException(400,detail="Email Address already exist...")
    
    hash_password = get_password_hash(body.password)
    
    new_user = UserModel(
        name = body.name,
        email = body.email,
        username = body.username,
        hash_password = hash_password,
        
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    
    return new_user