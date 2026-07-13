import os

from sqlalchemy import create_engine, event
from sqlalchemy.orm import Session
from sqlalchemy.engine import Engine

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
SECOND_DATABASE_URL = os.getenv("SECOND_DATABASE_URL")

def get_session(SQLITE: bool = False):
    
    engine = create_engine(DATABASE_URL)

    if SQLITE and SECOND_DATABASE_URL:
        engine = create_engine(SECOND_DATABASE_URL)
    
    return Session(engine)

