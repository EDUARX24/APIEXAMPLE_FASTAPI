from fastapi import FastAPI, Body
#importar route
from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse
from classFastApi import  User, BearerJwt
from token_utils import createToken

login_users = APIRouter()


#endpoint de usuario
@login_users.post("/login", tags=["Authentication"])
def login(user: User = Body(...)):
   
    token : str = createToken(user.dict())
    print(token)
    return {"token": f"{token}",
        "message": f"Welcome {user.username},",
            }