# MCS 275 Spring 2021 Lecture 38
# vote app (Whinge) database creation/reset

import sqlite3
import sys

DBFILE = "whinge.db"

con = sqlite3.connect(DBFILE)

print("Resetting database '{}'".format(DBFILE))

# delete messages table
con.execute("""
DROP TABLE IF EXISTS posts;
""")

# create messages table
con.execute("""
CREATE TABLE posts (
    postid INTEGER PRIMARY KEY,
    submitter TEXT NOT NULL,
    content TEXT NOT NULL,
    score INTEGER DEFAULT 0,
    ts REAL NOT NULL
);
""")

if "--sampledata" in sys.argv:
    print("Adding sample data to table 'posts'.")

    con.executemany("""
    INSERT INTO posts (score,ts,submitter,content) VALUES
    (?,?,?,?);
    """,
        [
            (16,1618421491.75,"user001","Having a loud side conversation on Zoom without muting your mic.",),
            (9,1618453592.06,"ddumas","Forgetting to shake the mustard before applying it to your hot dog so a bunch of liquid vinegar comes out and soaks the bun."),
            (7,1618448133.04,"recalcitrant_heliotrope","When someone stops in front of you on the stairs to check their phone."),
        ]
    )
else:
    print("Leaving table 'posts' empty.  (Run this script with '--sampledata' as a command line argument to add some sample data.)")

con.commit()
con.close()
