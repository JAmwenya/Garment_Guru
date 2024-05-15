#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel


class User(BaseModel):
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    basket = relationship('Basket', backref='user', uelist=False)
    closet = relationship('Closet', backref='user', uselist=False)
    garments = relationship('Garment', backref='user')
