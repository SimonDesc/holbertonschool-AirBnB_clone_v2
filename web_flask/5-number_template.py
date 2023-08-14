#!/usr/bin/python3
"""Start a web application"""
from flask import Flask, render_template
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


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Display if n is a number"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Display if n is a number"""
    return render_template("5-number.html", abc=n)


if __name__ == "__main__":
    app.run()
