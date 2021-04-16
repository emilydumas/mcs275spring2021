from flask import Flask, url_for, request, redirect
import sqlite3
import datetime
import time

app = Flask(__name__)

HEADER="""<!DOCTYPE html>
<html>
    <head>
        <title>Whinge</title>
        <link rel="stylesheet" href="/static/whinge.css">
    </head>

    <body>
        <h1>Whinge</h1>
        
        <div class="navigation">
            Showing <strong>top</strong> posts.  [Show new]
        </div>
"""

FOOTER="""</div>

        <div class="compose-form">
            <form action="/post" method="post">
                <div>
                    <label for="username">Username:</label>
                    <input type="text" id="username" name="username">
                </div>
                <div>
                    <label for="username">Whinge:</label>
                    <input type="text" id="whinge" name="whinge" size="80">
                </div>
                <input type="submit" value="Submit">
            </form>
            
        </div>
    </body>
</html>
"""

def get_db():
    """Open a connection to the database and return the connection object"""
    con = sqlite3.connect("whinge.db")
    con.row_factory = sqlite3.Row # return dict-like rows
    return con

def post_div(row):
    """Take a sqlite3.Row from the posts table and format it as a div compatible
    with the stylesheet."""
    timestr = datetime.datetime.fromtimestamp(row["ts"]).strftime("%Y-%m-%d %H:%M")

    return """
<div class="post">
    <div class="post-main">
        <span class="post-score">{0}</span><a class="post-plus-button" href="http://example.com">+</a><a class="post-minus-button" href="http://example.com">-</a><span class="post-content">{1}</span>
    </div>
    <div class="post-metadata">
        Submitted by <span class="post-author">{2}</span> at <span class="post-timestamp">{3}</span>
    </div>
</div>""".format(row["score"],row["content"],row["submitter"],timestr)

@app.route("/")
def redirect_top():
    """Root resource redirects to the top posts display"""
    return redirect(url_for("display_top"))

@app.route("/top/")
def display_top():
    """Show the top-ranked posts"""
    con = get_db()
    document = HEADER
    for row in con.execute("SELECT * FROM posts ORDER BY score DESC LIMIT 10;"):
        document += post_div(row)
    con.close()
    document += FOOTER
    # return the complete HTML document
    return document

@app.route("/post",methods=["GET","POST"])
def create_post():
    """Receive form data and add a row to the database"""

    # Check for and reject empty username or whinge
    if not request.values.get("username") or not request.values.get("whinge"):
        print("Ignoring request to with empty username or whinge")
    else:
        # Form data ok; add to DB
        con = get_db()
        con.execute("INSERT INTO posts (submitter,content,ts) VALUES (?,?,?);",
            (
                request.values.get("username"), # form field username -> DB column submitter
                request.values.get("whinge"),  # form field whinge  -> DB column content
                time.time()
            )
        )
        con.commit()
        con.close()
    
    # TODO: Handle possibility of failed INSERT

    # Send them back to the main page
    return redirect(url_for("display_top"))

if __name__=="__main__":
    app.run()