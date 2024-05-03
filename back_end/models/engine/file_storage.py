#!/usr/bin/python3
"""This module defines a class to manage file storage for Garmrnt Guru"""
import json


class FileStorage:
    """This class manages storage of Garment Guru models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns a dictionary of models currently in storage"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.image_upload import ImageUpload
        from models.closet import Closet
        from models.basket import Basket
        from models.garment import Garment
        from models.status import Status

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Status': Status, 'Image_upload': ImageUpload,
                    'Closet': Closet, 'Basket': Basket, 'Garment': Garment,
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
