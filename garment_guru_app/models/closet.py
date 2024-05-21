#!/usr/bin/python3
""" Closet module for garment guru"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from models.database import create_session

class Closet(BaseModel):
    __tablename__ = 'closets'
    user_id = Column('user_id', Integer, ForeignKey('users.id'), nullable=False)
    location = Column('location', String(128), nullable=True)
    clean_clothes_images = relationship('Image', backref='closet')

# Use Session to interact with the database
session = create_session(engine=None)
session.commit()
session.close()
