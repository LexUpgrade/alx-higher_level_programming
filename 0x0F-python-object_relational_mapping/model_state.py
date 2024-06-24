#!/usr/bin/python3
"""Creates a table class"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class State(Base):
    """A class 'State' table."""

    __tablename__ = "states"
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
