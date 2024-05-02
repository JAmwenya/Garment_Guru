#!/usr/bin/python3
""" ImageUpload module for garment guru """
from models.base_model import BaseModel


class ImageUpload(BaseModel):
    """Class containing details for uploaded images"""

    user_id = ""
    uploaded_images = []
    upload_location = ""
