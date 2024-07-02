# Daniel OUATTARA
# 02 07 2024


import sqlite3

# Connect to the database
conn = sqlite3.connect("48-sqlite-database.db")
cur = conn.cursor()

# Load SQL script from file
with open('48_members.sql') as file:
    sql_script = file.read()

# Execute script
cur.executescript(sql_script)

# Commit the transaction (optional but good practice)
conn.commit()

# Close all
cur.close()
conn.close()
