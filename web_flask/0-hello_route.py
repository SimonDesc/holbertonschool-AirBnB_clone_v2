#!/usr/bin/python3
"""Start a web application"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def route():
    """Show Hello HBNB"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run()
