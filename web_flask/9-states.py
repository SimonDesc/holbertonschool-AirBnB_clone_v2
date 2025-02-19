#!/usr/bin/python3
""" Script that runs an app with Flask framework """
from flask import Flask, render_template
from models import *

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Function called with / route"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Function called with /hbnb route"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """
    Function called with /c/<text> route
    display C followed by text variable
    """
    return "C %s" % text.replace("_", " ")


@app.route("/python/", defaults={"text": "is_cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """
    Function called with /python/<text> route
    display Python followed by text variable
    """
    return "Python %s" % text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    Function called with /number/<n> route
    """
    return "%d is a number" % n


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    Function called with /number_template/<int:n> route
    """
    return render_template("5-number.html", num=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """
    Function called with /number_odd_or_even/<int:n> route
    """
    return render_template("6-number_odd_or_even.html", num=n)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    Function called with /states_list route
    Display html page
    """
    list_states = storage.all("State")
    return render_template("7-states_list.html", states=list_states)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Call cities by states"""
    list_cities = storage.all("City")
    list_states = storage.all("State")
    return render_template(
        "8-cities_by_states.html", cities=list_cities, states=list_states
    )


@app.route("/states", strict_slashes=False)
def display_states():
    """function called with /states route that display a
    HTML page with the list of all State objects"""
    list_states = storage.all("State")
    return render_template("7-states_list.html", states=list_states)


@app.route("/states/<id>", strict_slashes=False)
def state_with_id(id):
    """function called with /states/<id> route that display a
    HTML page with the list of City objects linked to the State
    if a State object is found with this id ("Not found!")"""
    list_states = storage.all("State")
    return render_template("9-states.html", states=list_states, id=id)


@app.teardown_appcontext
def teardown(err):
    """remove the current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
