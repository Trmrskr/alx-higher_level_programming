#!/usr/bin/python3
"""
This script lists all State objects
from the database `hbtn_0e_6_usa`
using sqlalchemy ORM.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    The namespace of the this script.
    Connect to the database engine, establish a session
    from the database.
    """

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State).order_by(State.id)

    for state in states:
        print('{}: {}'.format(state.id, state.name))
