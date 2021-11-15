from flask import json, request, Response
from flask import Blueprint
import re

utils_api = Blueprint('utils_api', __name__)


@utils_api.route("/v1/isValidEmail", methods=['POST'])
def isValidEmail():
    email = request.form.get('email', default="", type=str)
    regexEmail = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

    if ("edu.vn" in email or "gov.vn" in email) \
            and re.fullmatch(regexEmail, email):
        response = Response(
            response=json.dumps({
                "message": "Valid Email"
            }),
            status=200,
            mimetype='application/json'
        )
        return response
    response = Response(
        response=json.dumps({
            "message": "Invalid Email"
        }),
        status=422,
        mimetype='application/json'
    )
    return response


def isValidURL(str):

    # Regex to check valid URL
    regex = ("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")

    # Compile the ReGex
    p = re.compile(regex)

    # If the string is empty
    # return false
    if (str == None):
        return False

    # Return if the string
    # matched the ReGex
    if(re.search(p, str)):
        return True
    else:
        return False
