#!/usr/bin/python3
"""
script that creates the State “California”
with the City “San Francisco” from the database hbtn_0e_100_usa
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
    n_city = City(name="San Francisco")
    n_state = State(name="California")
    n_state.cities.append(n_city)
    session.add_all([n_state, n_city])
    session.commit()
