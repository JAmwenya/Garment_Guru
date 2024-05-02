#!/usr/bin/python3
""" Status Module for garment guru """
from models.base_model import BaseModel


class Status(BaseModel):
    """Class for status (clean/dirty) of a garment"""

    user_id = ""
    garment_id = ""
    is_clean = False
