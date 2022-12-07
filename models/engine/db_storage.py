#!/usr/bin/python3
""" This module defines a class to manage database storage for hbnb clone """
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv
from models.city import City
from models.place import Place
from models.state import State
from models.user import User
from models.review import Review
from models.amenity import Amenity
from models.base_model import Base

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    """ This class manages storage of hbnb database """
    __engine = None
    __session = None

    def __init__(self):
        """ instantiates DBStorage object """
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(HBNB_MYSQL_USER,
                                              HBNB_MYSQL_PWD,
                                              HBNB_MYSQL_HOST,
                                              HBNB_MYSQL_DB),
                                      pool_pre_ping=True)

        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)
