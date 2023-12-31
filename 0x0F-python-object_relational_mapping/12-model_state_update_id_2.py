#!/usr/bin/python3
"""
script that changes the name of a State object from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    con = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    my_eng = create_engine(con.format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=my_eng)
    session = Session()
    demand = session.query(State).filter_by(id=2).first()
    demand.name = "New Mexico"
    session.commit()
