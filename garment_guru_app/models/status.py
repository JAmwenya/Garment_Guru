#!/usr/bin/python3
""" clothes status module for garment guru"""
from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import BaseModel
from models.database import create_session

class Status(BaseModel):
    __tablename__ = 'statuses'
    user_id = Column('user_id', Integer, ForeignKey('users.id'), nullable=False)
    image_id = Column('image_id', Integer, ForeignKey('images.id'), nullable=False)
    status = Column('status', String(128), nullable=False)  # 'clean' or 'dirty'

# Use Session to interact with the database
session = create_session(engine=None)
session.commit()
session.close()
