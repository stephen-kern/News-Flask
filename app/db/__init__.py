from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from flask import g

load_dotenv()

# connect to the database using the env variable
# The engine variable manages the overall connection to the database.
# The Session variable generates temporary connections for performing
# create, read, update, and delete (CRUD) operations.
# The Base class variable helps us map the models to real MySQL tables.
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
Session = sessionmaker(bind=engine)
Base = declarative_base()

def get_db():
    if 'db' not in g: 
        #store db connection in app context
        g.db = Session()
        
    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db(app):
    Base.metadata.create_all(engine)

    app.teardown_appcontext(close_db)