"""
This is the people module and supports all the ReST actions for the
PEOPLE collection
"""

import logging

# System modules
import random
from datetime import datetime

# 3rd party modules
from flask import (
    make_response,
    abort
)


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve with our API
PEOPLE = {
    "Farrell": {
        "fname": "Doug",
        "lname": "Farrell",
        "timestamp": get_timestamp()
    },
    "Brockman": {
        "fname": "Kent",
        "lname": "Brockman",
        "timestamp": get_timestamp()
    },
    "Easter": {
        "fname": "Bunny",
        "lname": "Easter",
        "timestamp": get_timestamp()
    }
}



def predict(surveyResult):
    """
    This function responds to a request for /api/people/{lname}
    with one matching person from people

    :param lname:   last name of person to find
    :return:        person matching last name
    """

    # Bad input?
    badInput = False
    if badInput:
        abort(500, 'Invalid input data: %s', surveyResult)


    logging.info(surveyResult)
    inRemission = random.choice([True, False])

    return {
        'inRemission': inRemission,
        'sourceSurveyResult': surveyResult
    }