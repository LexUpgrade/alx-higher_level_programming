#!/usr/bin/python3
"""
    Lists all 'State' objects, and correcponding 'City' objects, contained
    in the database 'hbtn_0e_101_usa'.
"""
from relationship_city import City
from relationship_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv as av


if __name__ == "__main__":
    db = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(av[1], av[2], av[3])
    engine = create_engine(db)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
        [print("\t{}: {}".format(city.id, city.name)) for city in state.cities]
