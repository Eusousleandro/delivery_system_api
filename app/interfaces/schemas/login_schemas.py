from pydantic import BaseModel, Field

class Login(BaseModel):
    email: str
    password: str = Field(max_length=72)

class TokenResponse(BaseModel):
    access_token: str
    token_type: str