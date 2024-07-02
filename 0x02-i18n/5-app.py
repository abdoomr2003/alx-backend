#!/usr/bin/env python3
"""
This module starts a Flask web application and renders a template on the root
route.

The application runs on host '0.0.0.0' and port 5000 with debug mode enabled.
"""

from flask import Flask, render_template, g
from flask_babel import Babel, request

app = Flask(__name__)


class Config:
    """
    Configuration class for setting application parameters.

    Attributes:
        LANGUAGES (list): Supported languages.
        BABEL_DEFAULT_LOCALE (str): Default locale for the application.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone for the application.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = LANGUAGES[0]
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    Retrieves a user dictionary based on the login_as parameter.

    Returns:
        dict or None: The user dictionary if found, otherwise None.
    """
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """
    Executed before each request to set the user on flask.g if logged in.
    """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """
    Selects the best match for the client's preferred language.

    This function is used by Flask-Babel to determine which language to use
    for translations. It checks the languages preferred by the client (as
    indicated by the 'Accept-Language' header in the request) and matches
    them against the supported languages configured in the application.

    Returns:
        str: The best matching language code from the supported languages,
        or the default language if no match is found.
    """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def hello_world() -> str:
    """
    Renders the '5-index.html' template on the root route.

    Returns:
        str: The rendered HTML content of the '5-index.html' template.
    """
    return render_template('5-index.html', locale=get_locale())


if __name__ == "__main__":
    """
    Starts the Flask web application.

    The application will run in debug mode, listening on all available
    IP addresses on port 5000.
    """
    app.run(debug=True, host='0.0.0.0', port=5000)
