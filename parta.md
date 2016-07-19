# Databases lab 2a: Adding data to a database

### Check out the code

Type the following commands into a terminal:

    git clone https://github.com/meet-projects/y2-db-lab2

### Set up python

Here's what you run the first time after you log in:

    exec bash
    wget http://tinyurl.com/MEETpythonY2
    source MEETpythonY2

If you have already run the code above but you've opened a new terminal window, please run:

    exec bash
    source ~/y2-venv/bin/activate

### Set up the database

Now, set up the database. *Warning: if you already have people in the
database, this command will delete all of them and reset it to Priscila,
Lorenzo, Jacek, Amit, and Mustafa.* You can use this any time if you mess up the
database or add too many people.

    python initialize.py

For this lab, you'll write your code either interactively in Python, or in
`add_to_database.py`.

#### Exercise: Create
Write code in `add_to_database.py` to add you and your partner to the database.
Run your code and use `print_databases.py` to make sure you have seven entries:
Priscila, Jacek, Lorenzo, Amit, Mustafa, and the two of you.
