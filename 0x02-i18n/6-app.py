#!/usr/bin/env python3
"""
This module starts a Flask web application and renders a template on the root
route.

The application runs on host '0.0.0.0' and port 5000 with debug mode enabled.
"""

from flask import Flask, render_template, g, request
from flask_babel import Babel, gettext as _
from typing import Optional, Dict, Any

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
    1: {"name": "John Doe", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Jane Smith", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Unknown", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> object:
    """
    Retrieves a user dictionary based on the login_as parameter.

    Returns:
        Optional[Dict[str, Any]]: The user dictionary if found, otherwise None.
    """
    try:
        user_id = int(request.args.get('login_as', default='0'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request() -> None:
    """
    Executed before each request to set the user on flask.g if logged in.
    """
    g.user = get_user()


@babel.localeselector
def get_locale() -> Optional[str]:
    """
    Selects the best match for the client's preferred language.

    This function is used by Flask-Babel to determine which language to use
    for translations. It checks the languages preferred by the client (as
    indicated by the 'Accept-Language' header in the request) and matches
    them against the supported languages configured in the application.

    The order of priority is:
    1. Locale from URL parameters
    2. Locale from user settings
    3. Locale from request header
    4. Default locale

    Returns:
        Optional[str]: The best matching language code from the supported languages,
        or None if no match is found.
    """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def hello_world() -> str:
    """
    Renders the '6-index.html' template on the root route.

    Returns:
        str: The rendered HTML content of the '6-index.html' template.
    """
    user = g.user
    if user:
        message = _('You are logged in as %(username)s.', username=user['name'])
    else:
        message = _('You are not logged in.')
    return render_template('6-index.html', locale=get_locale(), message=message)


if __name__ == "__main__":
    """
    Starts the Flask web application.

    The application will run in debug mode, listening on all available
    IP addresses on port 5000.
    """
    app.run(debug=True, host='0.0.0.0', port=5000)
