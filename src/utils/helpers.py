from sqlalchemy.orm import Session
from src.user.models import UserModel
from fastapi import HTTPException,status,Request,Depends
from src.utils.settings import settings
from jwt.exceptions import InvalidTokenError
import jwt
from src.utils.db import get_db

def is_authenticated(request: Request, db: Session=Depends(get_db)):
    try:
        token = request.headers.get("authorization")
        if not token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="you are unauthorized"
            )

        token = token.split(" ")[-1]

        data = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        user_id = data.get("_id")



        user = db.query(UserModel).filter(UserModel.id == user_id).first()

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="you are unauthorized"
            )

        return user

    except InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="you are unauthorized"
        )

 