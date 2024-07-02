# Daniel OUATTARA
# 02 07 2024


import sqlite3

# Connect to the database
conn = sqlite3.connect("48-sqlite-database.db")
cur = conn.cursor()

# when executing a query using a cursor, it returns the cursor
members = cur.execute('''SELECT * FROM members ORDER BY ln''')

for row in members:
    print(row)


# Close all
cur.close()
conn.close()

print('-------------------------------')

# Connect to the database
conn = sqlite3.connect("48-sqlite-database.db")
cur = conn.cursor()

# when executing a query using a cursor, it returns the cursor
cur.execute('''SELECT * FROM members ORDER BY ln''')

for row in cur:
    print(row)


# Close all
cur.close()
conn.close()


print('-------------------------------')
# -------------------------------------- version optimized

with sqlite3.connect("48-sqlite-database.db") as conn:
    cur = conn.cursor()

    # Execute the SELECT query
    cur.execute('''SELECT * FROM members ORDER BY ln''')

    # Fetch all rows
    members = cur.fetchall()

    # Print the rows
    for row in members:
        print(row)

    # No need to commit for SELECT queries

    # Close the cursor
    cur.close()

# Connection is automatically closed after exiting the 'with' block
