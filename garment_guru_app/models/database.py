#!/usr/bin/python3
from sqlalchemy import Column, Integer, LargeBinary, String
from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

def create_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()

class StoreImage(BaseModel, Base):
    __tablename__ = 'images'

    id = Column('id', Integer, primary_key=True)
    filename = Column('filename', String)
    image_data = Column('image_data', LargeBinary)
    user_id = Column('user_id', String)

class FileStorage:
    def __init__(self, engine):
        self.session = create_session(engine)

    # Return all images from the database
    def all(self):
        return self.session.query(StoreImage.filename, StoreImage.image_data, StoreImage.user_id).all()

    # Adding a new image to the database
    def new(self, image):
        self.session.add(image)
        self.session.commit()

    # Create a new BaseModel instance and save it to the database
    def create_base_model(self, *args, **kwargs):
        base_model = BaseModel(*args, **kwargs)
        self.new(base_model)
        return base_model

    # Committing changes to the database
    def save(self):
        self.session.commit()

    def reload(self):
    # Refreshes all the data from the database
        self.session.expire_all()
