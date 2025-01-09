from fastapi import FastAPI, Body, Path, Query, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from sqlalchemy.orm import Session
from token_utils import createToken
from classFastApi import Movie, BearerJwt
#import de mi modelo
from bd.database import SessionLocal , engine, Base
from models.movies import Movie as ModelMovie
#modulo para deserialize
from fastapi.encoders import jsonable_encoder

#importar la instancia de la base de datos
from bd.conect import get_db

#importar route
from fastapi import APIRouter


routerMovie = APIRouter()


#ruta de enpoint de movies
@routerMovie.get("/movies", tags=["Movies"], dependencies=[Depends(BearerJwt())])
def get_movies():

    #crear variable de busqueda
    db = SessionLocal()
    data = db.query(ModelMovie).all()
    return JSONResponse(content=jsonable_encoder(data))

# Endpoint para obtener una película por ID
@routerMovie.get("/movies/{id}", tags=["Movies"],status_code=200)
def get_movie(id: int, db: Session = Depends(get_db)):
    db = SessionLocal()
    movie = db.query(ModelMovie).filter(ModelMovie.id == id).first()
    if movie is None:
        return JSONResponse(status_code=404,content={"message": "Movie not found"})
    return JSONResponse(status_code=200, content=jsonable_encoder(movie))



# Endpoint para agregar una película
@routerMovie.post("/movies", tags=["Movies"], status_code=201)
def add_movie(movie: Movie, db: Session = Depends(get_db)):  # Usa el tipo Session
    new_movie = ModelMovie(**movie.dict())
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)  # Refresca para obtener el ID
    return {"message": "Movie created successfully", "movie_id": new_movie.id}

#Endpoint para actualizar una pelicula
@routerMovie.put("/movies/{id}", tags=["Movies"], status_code=200)  
def update_movie(id: int, movie: Movie):
    db = SessionLocal()
    data = db.query(ModelMovie).filter(ModelMovie.id == id).first()
    if data is None:
        return JSONResponse(status_code=404,content={"message": "Movie not found"})
    data.title = movie.title   
    data.director = movie.director
    data.year = movie.year
    data.rating = movie.rating
    data.category = movie.category
    db.commit()
    db.refresh(data)
    return JSONResponse(status_code=200, content=jsonable_encoder(data))
        
#endpoint para eliminar una pelicula
@routerMovie.delete("/movies/{id}", tags=["Movies"], status_code=200)
def delete_movie(id: int):
    db = SessionLocal()
    data = db.query(ModelMovie).filter(ModelMovie.id == id).first()
    if not data:
        return JSONResponse(status_code=404, content={"message": "Movie not found"})
    db.delete(data)
    db.commit()
    return JSONResponse(status_code=200, content={"message": "Movie deleted successfully", 'data': jsonable_encoder(data)})

#endpoint para buscar peliculas por categoria
@routerMovie.get("/movies/category/{category}", tags=["Movies"], status_code=200)
def get_movie_by_category(category: str):
    db = SessionLocal()
    data = db.query(ModelMovie).filter(ModelMovie.category == category).all()
    if not data:
        return JSONResponse(status_code=404, content={"message": "Category not found"})
    return JSONResponse(status_code=200, content=jsonable_encoder(data))
    