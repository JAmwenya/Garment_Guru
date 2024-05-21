#!/usr/bin/python3
"""This module defines a class Garment"""
from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import BaseModel
from models.database import create_session

class Garment(BaseModel):
    __tablename__ = 'garments'
    user_id = Column('user_id', Integer, ForeignKey('users.id'), nullable=False)
    name = Column('name', String(128), nullable=False)
    description = Column('description', String(256), nullable=True)
    image_url = Column('image_url', String(256), nullable=True)

# Use Session to interact with the database
session = create_session(engine=None)
session.commit()
session.close()
