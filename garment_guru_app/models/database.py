#!/usr/bin/python3
"""stores the images"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class StoreImage(Base):
    """class to store the images"""
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True)
    filename = Column(String)
    path = Column(String)

engine = create_engine('sqlite:///images.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
