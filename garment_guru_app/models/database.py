#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, LargeBinary
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class StoreImage(Base):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True)
    filename = Column(String)
    image_data = Column(LargeBinary)
    user_id = Column(String)
