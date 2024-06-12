# MCS 275 Spring 2021 - Emily Dumas
# Lecture 36 and 37
"""Simple chat web app"""
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
# footer format string has placeholders for the default username {0}
# and the URL that should be used for posting a message {1}
FOOTER="""</div>

        <div class="refresh-form">
            <form action="/" method="get">
                <input type="submit" value="Check for new messages">
                <input type="hidden" name="lastuser" value="{0}">
            </form>
        </div>

        <div class="message-compose-form">
            <form action="{1}" method="post">
                <div>
                    <input type="text" id="message" name="message" class="fullwidth">
                </div>
                <div>
                    <label for="username">Username:</label>
                    <input type="text" id="username" name="username" value="{0}">
                </div>
                <input type="submit" value="Send">
            </form>
            
        </div>
    </body>
</html>
"""

def footer():
    """Front page footer (the end of the messagebox div and everything after it).
    This contains the message composition form.  It needs to be dynamically generated
    because of the feature that auto-populates the username with the previously-used
    one if it is provided as a query param `lastuser`, and because it uses `url_for`
    to get the URL of the form submission target."""
    return FOOTER.format(
        request.values.get("lastuser",default=""),
        url_for("post_message")   # url_for takes a *function* name and 
                                  # determines which URL calls it.  Here
                                  # URL /post calls post_message.
    )

def get_db():
    """Open a connection to the yellaro database
    and return the connection object"""
    con = sqlite3.connect("yellaro.db")
    con.row_factory = sqlite3.Row # return dict-like rows
    return con

def message_div(row):
    """Take a sqlite3.Row with columns "sender" and "content" and convert it
    to a single HTML div that is compatible with the stylesheet."""
    return """<div class="message"><span class="message-username">{}</span><span class="message-content">{}</span></div>\n""".format(
        row["sender"],
        row["content"]
    )

@app.route("/")
def message_feed():
    """Return the HTML message feed and new message form."""
    con = get_db()
    feed = ""
    # We only show 10 messages, so they need to be the 10 largest timestamps.
    # Here we fetch them all, resulting in a list with the newest message first
    rows = con.execute("SELECT sender,content FROM messages ORDER BY ts DESC LIMIT 10;").fetchall()
    # But we want to display them with oldest first, so we reverse the list
    for row in reversed(rows):
        feed += message_div(row)    
    con.close()
    # return the complete HTML document
    return HEADER + feed + footer()

@app.route("/post",methods=["GET","POST"])
def post_message():
    """Receive form data and add a row to the database"""
    # Whether called after HTTP GET or POST, the form fields
    # are available with `flask.request.values.get(fieldname)`
    # Since we used `from flask import request` earlier, we 
    # can shorten this to `request.values(fieldname)`
    if not request.values.get("message") or not request.values.get("username"):
        print("Ignoring request to post message with empty content or username")
    else:
        # message is present and not empty.  Post it.
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
    
    # TODO: If the operations above result in an exception, this route will
    # return a 500 server error with an ugly default error page that doesn't
    # tell the user anything useful.  It would be better to catch exceptions
    # and handle them in a way that reports the problem to the user nicely.
    # (e.g. redirect to main page, but add a query param that the `/` route
    # recognizes as a sign to display some kind of error message)

    # Send them back to the main page, but pre-fill the username in the form
    return redirect(url_for("message_feed",lastuser=request.values.get("username")))

if __name__=="__main__":
    app.run()