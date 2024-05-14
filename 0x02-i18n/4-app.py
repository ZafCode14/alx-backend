#!/usr/bin/env python3
"""Module with a python script"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Class that configures the flask app"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Function that determines the best match with the supported languages"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        print(locale)
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def hello_world():
    """Function that renders a template"""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(debug=True)
