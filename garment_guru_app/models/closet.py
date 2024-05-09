#!/usr/bin/python3
""" Closet module for garment guru"""
from models.base_model import BaseModel


class Closet(BaseModel):
    """Class for a Closet that holds images of clean clothes"""
   
    user_id = ""
    clean_clothes_images = []
    location = ""
