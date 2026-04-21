import hashlib
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto') 

class AuthService:
    @staticmethod
    def _normalize(password: str) -> str:
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    @staticmethod
    def hash_password(password: str):
        return pwd_context.hash(AuthService._normalize(password))
    
    @staticmethod
    def verificy_password(plain_password, hashed_password):
        return pwd_context.verify(AuthService._normalize(plain_password), hashed_password)