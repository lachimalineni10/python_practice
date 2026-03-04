from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url  = 'postgresql://postgres:password@localhost:5432/project1'
engine  = create_engine(db_url)
session = sessionmaker(autoflush=False, bind=engine)
