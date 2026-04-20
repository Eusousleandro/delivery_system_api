from pydantic import BaseModel, ConfigDict


class RestaurantBase(BaseModel):
    name: str
    email: str
    cnpj: str
    password: str

class RestaurantCreate(RestaurantBase):
    pass

class RestaurantUpdate(BaseModel):
    name: str | None
    email: str | None
    cnpj: str | None
    password: str | None

class RestaurantResponse(BaseModel):
    id: int
    name: str
    email: str
    cnpj: str

model_config = ConfigDict(from_attributes=True)