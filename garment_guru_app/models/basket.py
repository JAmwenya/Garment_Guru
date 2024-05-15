#!/usr/bin/python3
""" Basket module for garment guru"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel

class Basket(BaseModel):
    __tablename__ = 'baskets'
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    location = Column(String(128), nullable=True)
    dirty_clothes_images = relationship('Image', backref='basket')
