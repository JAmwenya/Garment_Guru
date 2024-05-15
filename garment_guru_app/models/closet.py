#!/usr/bin/python3
""" Closet module for garment guru"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel

class Closet(BaseModel):
    __tablename__ = 'closets'
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    location = Column(String(128), nullable=True)
    clean_clothes_images = relationship('Image', backref='closet')
