# Databases lab 2b: reading data from a database

### Set up python

Here's what you run to set up Python:

    wget tinyurl.com/MEETpythonY2
    source MEETpythonY2

## Using SQLAlchemy interactively
Open up Python from the `y2-db-lab2' folder. Paste the following lines into Python:

    from sqlalchemy.orm import relationship, sessionmaker
    from sqlalchemy import create_engine

    from database_setup import Base, Person
    engine = create_engine('sqlite:///crudlab.db')
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

### Exercise: Read

1. In Python, use `session.query` to find the hometown of the only French person in the database.

2. Write a function `find_nationality` in `add_to_database.py` that takes a
   nationality and returns a list of names of people in the database with that
   nationality. For example, `find_nationality('American')` should return
   `['Priscila Cortez', 'Lorenzo Brown']` (the order doesn't matter). Your code
   should start like this:

    def find_nationality(nat):
