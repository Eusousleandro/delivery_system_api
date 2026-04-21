from app.domain.exceptions.exception import NotFoundException
from app.infrastructure.repositories.user_repository_implementation import UserRepository
from app.infrastructure.security.auth_service import create_access_token
from app.interfaces.schemas.login_schemas import Login


class Authenticate:
    def __init__(self, repository: UserRepository):
        self.repository = repository
        
    async def login(self, login: Login):
        user = self.repository.get_user_email(login.email)
        if not user:
            raise NotFoundException()
        
        token = create_access_token({'sub': user.email})
        return { 'access_token': token, 'token_type': 'bearer' }