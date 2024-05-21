#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from models.database import create_session


class User(BaseModel):
    __tablename__ = 'users'
    email = Column('email', String(128), nullable=False)
    password = Column('password', String(128), nullable=False)
    first_name = Column('first_name', String(128), nullable=True)
    last_name = Column('last_name', String(128), nullable=True)
    basket = relationship('Basket', backref='user', uselist=False)
    closet = relationship('Closet', backref='user', uselist=False)
    garments = relationship('Garment', backref='user')

# Use Session to interact with the database
session = create_session(engine=None)
session.commit()
session.close()
