* Write a function called `calculate_nationality_percentage` that calculates
  the percentage of each nationality in your database. When you run it, it
  should print out something like

    ```
    This database is 33% Israeli, 33% Palestinian, 33% American
    ```

  It should automatically figure out all the nationalities in the database. For
  example, if someone of Japanese nationality is added to the database, it might
  print

    ```
    This database is 31% Israeli, 31% Palestinian, 31% American, 6% Japanese
    ```

* Write a function `count_names_with_length` that takes a length (number) and
  returns the number of people whose first name is that long.  For example, if
  your database has Lorenzo Brown, Amin Manna, Sean Bonawitz, Haim Ehrlich,
  Mustafa Husein:

    ```
    >>> count_names_with_length(7)
    2
    >>> count_names_with_length(4)
    3
    >>> count_names_with_length(10)
    0
    ```

* Write a function `make_binational_pairs` that pairs off people in the
  database into binational pairs. Each pair can be from any two nationalities.
  You should return a list of tuples, where each tuple has two names. For
  example:

    ```
    make_binational_pairs()
    [('Priscila Cortez', 'Jacek Kaminski'), ('Mustafa Husein', 'Amit Nahari')]
