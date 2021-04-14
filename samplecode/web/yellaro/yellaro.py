from flask import Flask
import sqlite3

app = Flask(__name__)

HEADER="""<!DOCTYPE html>
<html>
    <head>
        <title>Yellaro</title>
        <link rel="stylesheet" href="yellaro.css">
    </head>

    <body>
        <h1>Yellaro</h1>
        
        <div class="messagebox">
"""

FOOTER="""</div>

        <div>
            <div>User: ________</div>
            <div>Message: __________</div>
            <div>[post]</div>
        </div>
    </body>
</html>
"""

def get_db():
    """Open a connection to the yellaro database
    and return the connection object"""
    con = sqlite3.connect("yellaro.db")
    con.row_factory = sqlite3.Row # return dict-like rows
    return con

def message_div(row):
    return """<div class="message"><span class="message-username">{}</span><span class="message-content">{}</span></div>\n""".format(
        row["sender"],
        row["content"]
    )

@app.route("/")
def message_feed_html():
    """Render the entire message table as HTML and return
    as a string"""
    con = get_db()
    feed = ""
    for row in con.execute("SELECT sender,content FROM messages ORDER BY ts;"):
        feed += message_div(row)    
    con.close()
    # return the complete HTML document
    return HEADER + feed + FOOTER

if __name__=="__main__":
    app.run()