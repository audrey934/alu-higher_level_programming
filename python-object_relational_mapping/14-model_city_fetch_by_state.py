#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>".format(sys.argv[0]))
        sys.exit(1)

    user, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to the MySQL server
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(user, password, db_name),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query: join State and City, sort by City.id
    results = session.query(State, City).filter(State.id == City.state_id).order_by(City.id).all()

    # Display as: <state name>: (<city id>) <city name>
    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
