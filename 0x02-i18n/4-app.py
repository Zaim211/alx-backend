#!/usr/bin/env python3
"""
Force locale with URL parameter
"""
from flask import (
    Flask,
    render_template,
    request
)
from flask_babel import Babel


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


@babel.localeselector
def get_locale():
    """
    detect if the incoming request contains locale argument and
    if value is a supported locale, return it
    """
    language = request.args.get('locale')
    if language in app.config['LANGUAGES']:
        return language
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    index the route
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run()
