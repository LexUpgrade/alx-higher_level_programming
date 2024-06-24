#!/usr/bin/python3
"""Lists all 'State' objects from the database 'hbtn_0e_6_usa'."""
from sys import argv as av
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

url_db = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(av[1], av[2], av[3])
engine = create_engine(url_db)
Session = sessionmaker(bind=engine)
session = Session()

states = session.query(State).all()

[print("{}: {}".format(state.id, state.name)) for state in states]
