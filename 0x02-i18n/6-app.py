#!/usr/bin/env python3
""" Use user locale """
from flask import (
    Flask,
    render_template,
    request,
    g
)
from flask_babel import Babel
from typing import Dict, Union


class Config(object):
    """
    Configuration for Babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """
    Returns a user dictionary or None if ID value can't be found
    or if 'login_as' URL parameter was not found
    """
    id = request.args.get('login_as', None)
    if id and int(id) in users.keys():
        return users.get(int(id))
    return None


@app.before_request
def before_request():
    """
    Add user to flask.g if user is found
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """
    Select and return best language match based on supported languages
    """
    language = request.args.get('locale')
    if language in app.config['LANGUAGES']:
        return language
    if g.user:
        language = g.user.get('locale')
        if language and language in app.config['LANGUAGES']:
            return language
    language = request.headers.get('locale', None)
    if language in app.config['LANGUAGES']:
        return language
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    setup the route
    """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run()
