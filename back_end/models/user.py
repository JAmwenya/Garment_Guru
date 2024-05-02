#!/usr/bin/python3
""" User Module for garment guru """
from models.base_model import BaseModel


class User(BaseModel):
    """Class for a User"""
    username = ""
    email = ""
    password_hash = ""
