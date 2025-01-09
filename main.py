from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
#importar route
from fastapi import APIRouter
#importar route
from routes.movie import routerMovie
from routes.users import login_users
import uvicorn
import os

#Intsantiate the FastAPI class
app = FastAPI(
    title="FastAPI Tutorial",
    description="Primeros pasos con FastAPI",
    version="1.0"
)
app.include_router(routerMovie)
app.include_router(login_users)


#ruta de enpoint
@app.get("/", tags=["Root"])
def read_root():
    return HTMLResponse(content="<h1>FastAPI Tutorial</h1><p>Primeros pasos con FastAPI</p>")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
