#!/usr/local/bin/python3

"""server.py - a minimal REST api for the namegen service."""
from flask import Flask, jsonify, abort
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_marshmallow import Marshmallow
from namegen import NameGenerator

app = Flask(__name__)
api = Marshmallow(app)
#rate limiter
limiter = Limiter(app, key_func=get_remote_address)
#NameGenerator instance
ng = NameGenerator()


def valid_name_request(count):
    """A method for validating a request to get unique names.

        Parameters
        ----------
        filename : str
            The filename to read.
    """
    if 0 <= count <= 1000:
        return True


class NameServer():
    """A class used to provide a REST API for retrieving unique names.

    ...

    Methods
    -------
    get(count)
        API for retrieving unique names in human and machine readable format.
    """
    @app.route("/names/<count>")
    @limiter.limit("10000/day;1000/hour;100/minute")
    def get(count):
        """A method to get unique names.

        Parameters
        ----------
        count : str
            The count of unique names to generate
        """
        count = int(count)
        if count is not None and valid_name_request(count):
            names = ng.generate_names(count)
            return jsonify(names)
        else:
            abort(404, message="Count value {} is invalid".format(count))


if __name__ == '__main__':
     app.run(host='0.0.0.0', debug=True, port=7777)
