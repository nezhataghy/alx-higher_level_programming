#!/usr/bin/python3
"""
script that prints all City objects from the database hbtn_0e_14_usa
 """
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    con = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    my_eng = create_engine(con.format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=my_eng)
    session = Session()
    demand = session.demand(State, City).filter(
        City.state_id == State.id).all()
    for row in demand:
        print("{}: ({}) {}".format(row[0].name, row[1].id, row[1].name))
