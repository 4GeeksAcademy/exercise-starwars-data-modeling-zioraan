import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(String(15))
    skin_color = Column(String(20))
    birth_year = Column(String(20))
    eye_color = Column(String(20))
    gender = Column(String(15))

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique = True)
    password = Column(String(50), nullable=False)
    email = Column(String(80), nullable=False)
    favorites_list = Column(Integer, ForeignKey('favorites.id'), unique=True)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    person_list = Column(Integer, ForeignKey('person.id'))
    planet_list = Column(Integer, ForeignKey('planet.id'))
    
class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(Integer)
    gravity = Column(String(40))
    climate = Column(String(40))
    terrain = Column(String(40))
    population = Column(Integer)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
