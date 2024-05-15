#!/usr/bin/python3
""" Garment module for Garment guru """
from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import BaseModel

class Garment(BaseModel):
    __tablename__ = 'garments'
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(256), nullable=True)
    image_url = Column(String(256), nullable=True)
