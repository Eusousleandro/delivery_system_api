from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.application.use_cases.authenticate_sercive import AuthentService
from app.interfaces.dependencies.user_dependency import get_user_service
from app.interfaces.schemas.login_schemas import Login, TokenResponse



router = APIRouter(prefix='/auth', tags=['Authentication'])

@router.post('/', response_model=TokenResponse)
async def login(
    data: OAuth2PasswordRequestForm = Depends(),
    service: AuthentService = Depends(get_user_service)
):
    login = Login(
        email=data.username,
        password=data.password
    )
    
    return await service.authenticate(login)
