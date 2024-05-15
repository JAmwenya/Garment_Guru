#!/usr/bin/python3
from sqlalchemy import Column, Integer, LargeBinary, String
from models.base_model import BaseModel

class StoreImage(BaseModel):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True)
    filename = Column(String)
    image_data = Column(LargeBinary)
    user_id = Column(String)
