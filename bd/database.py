import os
from  sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


dbName = 'movies.sqlite'
base_dir = os.path.abspath(os.path.dirname(__file__))
databaseUrl = f"sqlite:///{os.path.join(base_dir, dbName)}"

engine = create_engine(databaseUrl,echo=True, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()