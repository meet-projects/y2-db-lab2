from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    name = Column(String)
    id = Column(Integer, primary_key=True)
    gender = Column(String)
    nationality = Column(String)
    hometown = Column(String)

