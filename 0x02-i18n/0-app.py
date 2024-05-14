#!/usr/bin/env python3
"""Module with a python script"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def hello_world():
    """function that renders a template"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
