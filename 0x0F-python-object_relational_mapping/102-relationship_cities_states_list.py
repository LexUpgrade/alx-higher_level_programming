#!/usr/bin/python3
"""
    Lists all 'City' objects from the database 'hbtn_0e_101_usa'.
"""
from relationship_city import City
from relationship_state import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv as av


if __name__ == "__main__":
    db = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(av[1], av[2], av[3])
    engine = create_engine(db)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).all()

    [print("{}: {} -> {}".format(c.id, c.name, c.states.name)) for c in cities]
