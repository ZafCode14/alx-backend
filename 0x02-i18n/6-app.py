#!/usr/bin/env python3
"""Module with a python script"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """Class that configures the flask app"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user():
    """Function that gets user"""
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """Fuction before request"""
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """Function that determines the best match with the supported languages"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    if g.user:
        locale = g.user.get('locale')
        if locale and locale in app.config['LANGUAGES']:
            return locale

    locale = request.headers.get('locale', None)
    if locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def hello_world():
    """Function that renders a template"""
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run(debug=True)
