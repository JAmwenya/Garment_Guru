#!/usr/bin/python3
""" clothes status module for garment guru"""
from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import BaseModel

class Status(BaseModel):
    __tablename__ = 'statuses'
        user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
            image_id = Column(Integer, ForeignKey('images.id'), nullable=False)
                status = Column(String(128), nullable=False)  # 'clean' or
                'dirty'
