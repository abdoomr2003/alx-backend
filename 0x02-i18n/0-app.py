#!/usr/bin/env python3
"""
This module starts a Flask web application and renders a template on the root
route.

The application runs on host '0.0.0.0' and port 5000 with debug mode enabled.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world() -> str:
    """
    Renders the '0-index.html' template on the root route.

    Returns:
        str: The rendered HTML content of the '0-index.html' template.
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    """
    Starts the Flask web application.

    The application will run in debug mode, listening on all available
    IP addresses on port 5000.
    """
    app.run(debug=True, host='0.0.0.0', port=5000)
