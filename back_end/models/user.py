#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class defining a user by attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
