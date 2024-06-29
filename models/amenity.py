#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models import storage_type

class Amenity(BaseModel, Base):
    ''' class amenity'''
    __tablename__ = 'amenities'
    if storage_type == 'db':
        name = column(string(128), nullable=False)
    else:
        name = ""
