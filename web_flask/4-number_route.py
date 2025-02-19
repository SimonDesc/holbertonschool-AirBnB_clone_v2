#!/usr/bin/python3
"""Start a web application"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def route():
    """Show Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Display c followed by the value of text"""
    text = text.replace("_", " ")
    return f"C {escape(text)}"


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """Display python is cool by default"""
    text = text.replace("_", " ")
    return f"Python {escape(text)}"


@app.route("/number/<int:n>")
def number(n):
    """Display if n is a number"""
    return f"{n} is a number"


if __name__ == "__main__":
    app.run()
