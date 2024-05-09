#!/usr/bin/python3
""" Garment module for Garment guru """
from models.base_model import BaseModel


class Garment(BaseModel):
     """class containing details to create a garment"""

     user_id = ""
     name = ""
     description = ""
     image_url = ""