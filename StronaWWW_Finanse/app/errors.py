from flask import render_template  # pylint: disable=W0613
from app import app


@app.errorhandler(404)
def not_found_error(error):  # pylint: disable=W0613
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):  # pylint: disable=W0613
    return render_template('500.html'), 500
