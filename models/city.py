#!/usr/bin/python3
""" City Module for HBNB project """

from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
from models.base_model import BaseModel, Base



class City(BaseModel, Base):
    """City class"""
    if getenv('HBNB_TYPE_STORAGE') == "db":
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship('Place', backref='cities')
    else:
        """ The city class, contains state ID and name """
        state_id = ""
        name = ""
