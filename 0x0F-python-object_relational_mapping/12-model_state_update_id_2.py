#!/usr/bin/python3

"""MODULE"""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]))

    Base.metadata.create_all(engine)

    DBSession = sessionmaker(bind=engine)

    session = DBSession()

    up_state = session.query(State).filter(State.id == '2').first()

    up_state.name = 'New Mexico'

    session.commit()