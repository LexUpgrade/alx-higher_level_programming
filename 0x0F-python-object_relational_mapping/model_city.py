#!/usr/bin/python3
"""
    Creates a class 'City'.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class City(Base):
    """A class 'City'.

    Args:
        id (int): ID of the city
        name (string): Name of the city
        state_id (int): ID of the referencing state
    """

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("State.id"), nullable=False)
