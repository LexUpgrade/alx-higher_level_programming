#!/usr/bin/python3
"""
    Creates a 'State': "California" with the 'City': "San Francisco" from
    the database 'hbtn_0e_100_usa'.
"""
from relationship_city import City
from relationship_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv as av


if __name__ == "__main__":
    db = "mysql+mysqldb://{}:{}@localhost:3306/{}"\
            .format(av[1], av[2], av[3], pre_pool_ping=True)
    engine = create_engine(db)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name="California")
    city = City(name="San Francisco")
    state.cities.append(city)

    session.add_all([state, city])
    session.commit()
