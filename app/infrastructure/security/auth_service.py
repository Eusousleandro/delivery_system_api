from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session

from app.config.dependency_db import Dependencies
from app.infrastructure.database.models.user import User

SECRET_KEY = "A_MINHA_CHAVE"
ALGORITHM = 'HS256'
ACCESS_TOKEN_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/login')

class AuthService:
    @staticmethod
    def get_current_user(
        token: str = Depends(oauth2_scheme),
        db: Session = Depends(Dependencies.get_db)
    ):
        try: 
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            user_email = payload.get('sub')
            if not user_email:
                raise HTTPException(status_code=401, detail='Token invalid')
        
            user = db.query(User).filter(User.email == user_email).first()

            if not user:
                raise HTTPException(status_code=401, detail='Usuário não encontrado')
            return user 
        
        except JWTError:
            raise HTTPException(status_code=401, detail="Token inválido")
        
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_MINUTES)
    to_encode.update({'exp': expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token
