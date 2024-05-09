#!/usr/bin/python3
from sqlalchemy import create_engine
from models.database import StoreImage

# Define new database file path
database_uri = 'sqlite:///images.db'

# Create an SQLAlchemy engine
engine = create_engine(database_uri)

StoreImage.metadata.create_all(engine)

print("New database images.db created successfully.")
