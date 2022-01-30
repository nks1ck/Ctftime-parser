import datetime

from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# TODO: Connect to postgres
engine = create_engine('sqlite:///sqlite3.db', echo=True, connect_args={"check_same_thread": False})
base = declarative_base()
meta = MetaData()

users = Table(
    'users',
    meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String, nullable=False),
    Column('team_link', String, nullable=False),
    Column('register_time', DateTime, default=datetime.datetime.now())
)

meta.create_all(engine)
