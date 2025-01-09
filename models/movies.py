from sqlalchemy import Column, Integer, String, Float
from bd.database import Base

class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    director = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    category = Column(String)
