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

    add_state = State(name='Louisiana')

    session.add(add_state)

    session.commit()

    add_id = session.query(State).filter\
             (State.name.like('%Louisiana%')).first()

    if add_id:
        print(add_id.id)
    else:
        print("Nothing")
