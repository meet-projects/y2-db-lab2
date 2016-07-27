from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from database_setup import Base, Person

engine = create_engine('sqlite:///crudlab.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

### These are the commands you just saw live.

priscila = Person(
        name = 'Priscila Cortez',
        gender = 'female',
        nationality = 'American',
        hometown = 'Miami')

lorenzo = Person(
        name = 'Lorenzo Brown',
        gender = 'male',
        nationality = 'American',
        hometown = 'Dallas')

jacek = Person(
        name = 'Jacek Kaminski',
        gender = 'male',
        nationality = 'French',
        hometown = 'Paris')

mustafa = Person(
        name = 'Mustafa Hussein',
        gender = 'male',
        nationality = 'Palestinian',
        hometown = 'Jerusalem')

amit = Person(
        name = 'Amit Nahari',
        gender = 'male',
        nationality = 'Israeli',
        hometown = 'Jerusalem')

# This deletes everything in your database.
session.query(Person).delete()
session.commit()

# This adds some rows to the database. Make sure you `commit` after `add`ing!
session.add(priscila)
session.add(jacek)
session.add(amit)
session.add(mustafa)
session.add(lorenzo)
session.commit()

print("I just created a file called crudlab.db with a database. The database has one table called person, and I added four people to the table.")
