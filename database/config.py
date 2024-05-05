from decouple import config

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_CONN = config("DATABASE_CONN")

print("SQLALCHEMY_DATABASE_CONN", SQLALCHEMY_DATABASE_CONN)

engine=create_engine(SQLALCHEMY_DATABASE_CONN,
    echo=True
)

Base=declarative_base()

SessionLocal=sessionmaker(bind=engine)
