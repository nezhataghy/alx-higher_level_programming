#!/usr/bin/python3
"""
script that lists all City objects from the database hbtn_0e_101_usa
"""
from sys import argv
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    eng = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
          argv[1], argv[2], argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    demand = session.query(City).order_by(City.id).all()
    for row in demand:
            print("{}: {} -> {}".format(row.id, row.name, row.state.name))
    session.close()
