from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from databases import Database

SQLALCHEMY_DATABASE_URL = 'sqlite:///./app/database/db.sqlite3'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={'check_same_thread': False}
)

Session = sessionmaker(bind=engine)

Base = declarative_base()

db = Database(SQLALCHEMY_DATABASE_URL)
