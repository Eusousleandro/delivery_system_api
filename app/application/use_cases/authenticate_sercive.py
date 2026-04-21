from fastapi import HTTPException

from app.infrastructure.repositories.user_repository_implementation import UserRepository
from app.infrastructure.security.auth_service import create_access_token
from app.interfaces.schemas.login_schemas import Login


class AuthentService:
    def __init__(self, repository: UserRepository):
        self.repository = repository
        
    async def authenticate(self, login: Login):
        user = await self.repository.get_user_email(login.email)
        if not user or user.password != login.password:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        token = create_access_token({'sub': user.email})
        return { 'access_token': token, 'token_type': 'bearer' }