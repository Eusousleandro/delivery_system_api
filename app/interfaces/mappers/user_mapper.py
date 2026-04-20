from app.domain.entities.user import User
from app.interfaces.schemas.user_schema import UserResponse

def to_user_response(user: User) -> UserResponse:
    return UserResponse(
        id=user.id,
        name=user.name,
        email=user.email
    )