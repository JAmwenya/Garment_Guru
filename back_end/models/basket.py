#!/usr/bin/python3
""" Basket module for garment guru"""
from models.base_model import BaseModel


class Basket(BaseModel):
    """Class for a Basket that holds dirty clothes images"""

    user_id = ""
    dirty_clothes_images = []
    location = ""
