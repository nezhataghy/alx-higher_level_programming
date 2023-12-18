#!/usr/bin/python3
from sys import argv
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    connection = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(connection.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    demand = session.query(State).order_by(State.id).all()
    for ligne in demand:
        print("{}: {}".format(ligne.id, ligne.name))
        for ligne_rel in ligne.cities:
            print("\t{}: {}".format(ligne_rel.id, ligne_rel.name))
