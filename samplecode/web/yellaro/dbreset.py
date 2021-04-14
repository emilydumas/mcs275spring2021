# MCS 275 Spring 2021 Lecture 36
# Chat app (Yellaro) database creation/reset

import sqlite3

con = sqlite3.connect("yellaro.db")

# delete messages table
con.execute("""
DROP TABLE IF EXISTS messages;
""")

# create messages table
con.execute("""
CREATE TABLE messages (
    id INTEGER PRIMARY KEY,
    sender TEXT,
    content TEXT,
    ts REAL
);
""")

con.execute("""
INSERT INTO messages (sender,content,ts) VALUES
(?,?,?);
""",
("David","How's it going?",1618247723.27))

con.execute("""
INSERT INTO messages (sender,content,ts) VALUES
(?,?,?);
""",
("Zoe","Great, I just started working on Worksheet 13!!!",1618248002.79))

con.commit()
con.close()
