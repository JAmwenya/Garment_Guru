#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.database import StoreImage

class FileStorage:
    def __init__(self):
        # Connecting to the database
        self.engine = create_engine('sqlite:///images.db')
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    # Return all images from the database
    def all(self):
        return self.session.query(StoreImage).all()

    # Adding a new image to the database
    def new(self, image):
        self.session.add(image)
        self.session.commit()

    # Committing changes to the database
    def save(self):
        self.session.commit()

    def reload(self):
        pass
