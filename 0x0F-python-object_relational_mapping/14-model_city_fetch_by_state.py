#!/usr/bin/python3

"""MODULE"""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import Base, City

if __name__ == "__main__":

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]))

    Base.metadata.create_all(engine)

    DBSession = sessionmaker(bind=engine)

    session = DBSession()

    city_state = session.query(City, State).filter(City.state_id == State.id)

    for inst in city_state:
        print("{}: ({}) {}".format(
            inst.State.name, inst.City.id, inst.City.name))
