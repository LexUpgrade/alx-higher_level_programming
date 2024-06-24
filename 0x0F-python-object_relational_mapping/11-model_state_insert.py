#!/usr/bin/python3
"""
    Adds the 'State' object "Louisiana" to the database 'hbtn_0e_6_usa'.
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

    state = State(name="Louisiana")
    session.add(state)
    new_state = session.query(State).filter_by(name="Louisiana").first()
    print(new_state.id)
    session.commit()
