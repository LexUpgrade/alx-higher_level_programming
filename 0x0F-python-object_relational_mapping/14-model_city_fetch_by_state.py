#!/usr/bin/python3
"""
    Prints all 'City' objects from the database 'hbtn_0e_14_usa'.
"""
from sys import argv as av
from model_city import City
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    db = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(av[1], av[2], av[3])
    engine = create_engine(db)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states_n_cities = session.query(State.name, City.id, City.name).where(State.id == City.state_id).order_by(City.id).all()
    [print("{}: ({}) {}".format(i[0], i[1], i[2])) for i in states_n_cities]
