import sqlalchemy
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine('sqlite:///sqlite3.db', echo=True, connect_args={"check_same_thread": False})
base = declarative_base()
meta = MetaData()

users = Table(
    'users',
    meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String, nullable=False),
    Column('team_link', String, nullable=False)
)

meta.create_all(engine)
