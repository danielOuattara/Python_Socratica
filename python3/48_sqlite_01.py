# Daniel OUATTARA
# 02 07 2024


"""
SQLite

https://docs.python.org/3.11/library/sqlite3.html#module-sqlite3

https://docs.python.org/3.12/library/sqlite3.html#module-sqlite3


SQLite       Python
-------      --------

INTEGER  --> INT
REAL     --> FLOAT
TEXT     --> STRING
BLOB     --> BYTES
NULL     --> NONE

"""

import sqlite3

# connect to a (new) database
conn = sqlite3.connect("48-sqlite-database.db")

#  create a cursor
cur = conn.cursor()

# create a 'people' table
cur.execute('''CREATE TABLE IF NOT EXISTS people
            (first_name TEXT, last_name TEXT)''')

conn.commit()

# close connection
cur.close()
conn.close()


# --------------------------------

# connect again to database
conn = sqlite3.connect("48-sqlite-database.db")

#  create a cursor (again)
cur = conn.cursor()

# Test data
name_list = [
    ("John", "Doe"),
    ("Jane", "Smith"),
    ("Alice", "Johnson"),
    ("Michael", "Williams"),
    ("Emily", "Brown"),
    ("Daniel", "Jones"),
    ("Laura", "Garcia"),
    ("David", "Martinez"),
    ("Sophia", "Davis"),
    ("James", "Rodriguez")
]


cur.executemany(
    '''INSERT INTO people (first_name, last_name) VALUES (?,?)''', name_list)

conn.commit()

# close connection
cur.close()
conn.close()


# =================================== Optimized


# Connect to the database
with sqlite3.connect("48-sqlite-database.db") as conn:
    # Create a cursor
    cur = conn.cursor()

    # Create a 'people' table if it doesn't exist
    cur.execute('''CREATE TABLE IF NOT EXISTS people_2
                   (first_name TEXT, last_name TEXT)''')

    # Commit the table creation
    conn.commit()

    # Insert test data into the 'people' table
    name_list = [
        ("John", "Doe"),
        ("Jane", "Smith"),
        ("Alice", "Johnson"),
        ("Michael", "Williams"),
        ("Emily", "Brown"),
        ("Daniel", "Jones"),
        ("Laura", "Garcia"),
        ("David", "Martinez"),
        ("Sophia", "Davis"),
        ("James", "Rodriguez")
    ]

    cur.executemany(
        '''INSERT INTO people_2 (first_name, last_name) VALUES (?, ?)''', name_list)

    # Commit the insertions
    conn.commit()

    # Close the cursor (automatically done by 'with' block)
    # cur.close()

# Connection is automatically closed after exiting the 'with' block
