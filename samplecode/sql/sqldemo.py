# MCS 275 Spring 2021 Lecture 31
# David Dumas
"""SQLite hello world: Make a database,
a table, and a few rows.  Read them back
and print the results."""
import sqlite3

# Create (or open) the database
con = sqlite3.connect("solarsystem.sqlite")

# Make the table
con.execute("""CREATE TABLE planets (
    name TEXT,
    dist REAL,
    year_discovered INTEGER
);""")

# Add two rows
con.execute(
    "INSERT INTO planets VALUES (?,?,?);",
    ("Earth",1.0,None)
)
con.execute(
    "INSERT INTO planets VALUES (?,?,?);",
    ("Neptune",30.1,1846)
)

# Ask for the entire table to be returned
# (The * means all columns, the lack of WHERE means
#  all rows.)
res = con.execute("SELECT * FROM planets;")

# Return value of con.execute is an iterable that
# yields the rows as tuples
for row in res:
    print(row)

# Save changes to disk
con.commit()

# (We could perform additional operations using
# the connection here.)

# Close the connection
con.close()

# After calling .close(), the connection cannot be used.

# -----

# Note: If you run this program twice, it will
# fail the second time because the table "planets"
# will already exist.  Attempting to create a table
# that already exists is an error in SQL.

# To try the program again, delete solarsystem.sqlite
# so the database will be empty at the start.
