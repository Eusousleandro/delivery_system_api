from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.application.use_cases.authenticate_sercive import AuthentService
from app.interfaces.dependencies.login_dependency import get_auth_service
from app.interfaces.schemas.login_schemas import Login, TokenResponse

router = APIRouter(prefix='/auth', tags=['Authentication'])

@router.post('/login', response_model=TokenResponse)
async def login(
    data: OAuth2PasswordRequestForm = Depends(),
    service: AuthentService = Depends(get_auth_service)
):
    login = Login(
        email=data.username,
        password=data.password
    )
    
    return await service.authenticate(login)
