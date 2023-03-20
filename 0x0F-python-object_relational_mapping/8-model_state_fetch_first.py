#!/usr/bin/python3
"""
This script prints the first State object
from the database `hbtn_0e_6_usa` using sqlalchemy.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    connect to database engine using uri, establish a session
    print firs t row from database.
    """

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()
    state = session.query(State).order_by(State.id).first()

    if state is None:
        print('Nothing')
    else:
        print('{0}: {1}'.format(state.id, state.name))
