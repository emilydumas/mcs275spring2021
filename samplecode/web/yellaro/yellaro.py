from flask import Flask, url_for, request, redirect
import sqlite3
import time

app = Flask(__name__)

# Flask automatically handles URLs beginning with /static
# by looking for files in the /static subdirectory of the
# applicaiton directory.  We use this to deliver the CSS.
HEADER="""<!DOCTYPE html>
<html>
    <head>
        <title>Yellaro</title>
        <link rel="stylesheet" href="/static/yellaro.css">
    </head>

    <body>
        <h1>Yellaro</h1>
        
        <div class="messagebox">
"""

FOOTER="""</div>

        <div>
            <form action="/post" method="post">
                <div>
                    <label for="username">Username:</label>
                    <input type="text" id="username" name="username">
                </div>
                <div>
                    <label for="message">Message:</label>
                    <input type="text" id="message" name="message">
                </div>
                <input type="submit" value="Post">
            </form>
            
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

@app.route("/post",methods=["GET","POST"])
def create_message():
    """Receive form data and add a row to the database"""
    # Whether called after HTTP GET or POST, the form fields
    # are available with `flask.request.values.get(fieldname)`
    # Since we used `from flask import request` earlier, we 
    # can shorten this to `request.values(fieldname)`
    con = get_db()
    con.execute("INSERT INTO messages (sender,content,ts) VALUES (?,?,?);",
        (
            request.values.get("username"), # form field username -> DB column sender
            request.values.get("message"),  # form field message  -> DB column content
            time.time()
        )
    )
    con.commit()
    con.close()
    return redirect("/")

if __name__=="__main__":
    app.run()