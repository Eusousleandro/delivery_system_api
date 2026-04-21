from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, Depends

SECRET_KEY = "A_MINHA_CHAVE"
ALGORITHM = 'HS256'
ACCESS_TOKEN_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/login')

class AuthService:
    def get_current_user(token: str = Depends(oauth2_scheme)):
        try: 
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            user_email = payload.get('sub')
            if not user_email:
                raise HTTPException(status_code=401, detail='Token invalid')
        
        except JWTError:
            raise HTTPException(status_code=401, detail="Token inválido")

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_MINUTES)
    to_encode.update({'exp': expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token
