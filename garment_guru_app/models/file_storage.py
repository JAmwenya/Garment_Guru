#!/usr/bin/python3
from models.database import StoreImage
from sqlalchemy.orm import sessionmaker

class FileStorage:
    def __init__(self, engine):
        self.engine = engine
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.images = self.session.query(StoreImage).all()

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
    # Refreshes all the data from the database
        self.session.expire_all()
