#!/usr/bin/python3
"""
    Lists all 'State' object that contain the letter 'a' from the database
    'hbtn_0e_6_usa'.
"""
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv as av

if __name__ == "__main__":
    db = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(av[1], av[2], av[3])
    engine = create_engine(db)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like("%a%"))
    [print("{}: {}".format(s.id, s.name)) for s in states]
