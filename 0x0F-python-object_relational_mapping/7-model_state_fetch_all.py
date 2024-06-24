#!/usr/bin/python3
"""Lists all 'State' objects from the database 'hbtn_0e_6_usa'."""
from sys import argv as av
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    db = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(av[1], av[2], av[3])
    engine = create_engine(db)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    [print("{}: {}".format(state.id, state.name)) for state in states]
