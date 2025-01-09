from fastapi import FastAPI, Request,HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from fastapi.security import HTTPBearer
from token_utils import validateToken

class User(BaseModel):
    email: str = Field(min_length=3, max_length=50, example="user@gmail.com")
    username: str = Field(min_length=3, max_length=15, example="JohnDoe")
    password: str = Field(example="password")


#iNSTANTIATE THE BASEMODEL CLASS
class Movie(BaseModel):
    # id: Optional[int] = None
    title: str = Field(example="The Godfather")
    director: str = Field(example="Nombre director")
    year: int = Field(example=1972)
    rating: float = Field(ge=1, le=10,example=9.2)
    category: str = Field(min_length=3, max_length=15, example="Drama")

    class Config:
        orm_mode = True


class BearerJwt(HTTPBearer):
    async def __call__(self, request : Request):
        auth = await super().__call__(request)
        data = validateToken(auth.credentials)
        if data['email'] != 'eduar@gmail.com':
            raise HTTPException(status_code=403, detail='Credenciales incorrectas')