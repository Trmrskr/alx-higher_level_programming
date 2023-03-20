#!/usr/bin/python3
"""
This python script that use sqlalchemy to query a database and list
all State objects containing the letter `a` from `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Connect to the database using db_uri, create a session and query
    the database
    """

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State).filter(State.name.contains('a'))

    for state in states:
        print('{}: {}'.format(state.id, state.name))
