# Databases lab 2b: reading data from a database

### Check out the code

Type the following commands into a terminal:

    git clone https://github.com/meet-projects/y2-db-labs

### Set up python

Here's what you run the first time after you log in:

    exec bash
    wget http://tinyurl.com/MEETpythonY2
    source MEETpythonY2

If you have already run the code above but you've opened a new terminal window, please run:

    exec bash
    source ~/y2-venv/bin/activate

### Exercise: Read

1. Use `session.query` to find the hometown of the only French person in the database.

2. Write a function `find_nationality` in `add_to_database.py` that takes a
   nationality and returns a list of names of people in the database with that
   nationality. For example, `find_nationality('American')` should return
   `['Priscila Cortez', 'Lorenzo Brown']` (the order doesn't matter). Your code
   should start like this:

    def find_nationality(nat):
