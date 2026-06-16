from sqlalchemy import create_engine, event
from sqlalchemy.orm import Session
from sqlalchemy.engine import Engine
        
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://ehsan:1234@0.0.0.0:5432/mydb"

def get_session():
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    return Session(engine)

