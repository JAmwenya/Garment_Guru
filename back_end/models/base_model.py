#!/usr/bin/python3
""" a module that defines a base class"""
import uuid
from datetime import datetime


class BaseModel:
    """A base model class with default attributes and methods for object."""

    def __init__(self, *args, **kwargs):
        """
        Initializes an instance of the BaseModel class.

        Parameters:
        - *args: Variable positional arguments.
        - **kwargs: Variable kwargs. If provided, updates instance attributes
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                if key != "__class__":
                    setattr(self, key, value)
        else:

            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns:
        dict: Dictionary with 'id', 'created_at', 'updated_at', and '__class__
        """
        my1_dict = self.__dict__.copy()
        my1_dict['created_at'] = self.created_at.isoformat()
        my1_dict['updated_at'] = self.updated_at.isoformat()
        my1_dict['__class__'] = self.__class__.__name__
        return my1_dict

    def save(self):
        """ method that  the public instance attribute"""
        from models import storage
        storage.new(self)
        self.updated_at = datetime.now()
        storage.save()

    def __str__(self):
        """
        Returns a string representation of the object.

        Returns:
        str: String with class name, instance ID, and instance attributes.
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
