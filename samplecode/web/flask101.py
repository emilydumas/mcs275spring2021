from flask import Flask

app = Flask(__name__)

@app.route("/positivity/")
def name_of_function_does_not_matter():
    return """<!doctype html>
    <html>
        <body>
            You can do it!
        </body>
    </html>
    """

app.run()