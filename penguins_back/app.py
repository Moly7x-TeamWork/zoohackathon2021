from flask import Flask, json, request
from flask_cors import CORS

import database.dbConnector as connector
from module.utils import utils_api, isValidURL
from ai.summarization import summarization_model
from ai.countAnimal import count_animals
from collections import OrderedDict

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.register_blueprint(utils_api)
CORS(app)


@app.route("/v1/test")
def hello_world():
    raw = request.get_json()
    print(raw.get("hello"))
    response = app.response_class(
        response={
            "hello": "Hi"
        },
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/v1/addLinkGroup", methods=['POST'])
def addLinkGroup():
    raw = request.get_json()
    linkGroup = raw.get('linkGroup')

    if isValidURL(linkGroup) and connector.setNewLinkGroup(linkGroup):
        response = app.response_class(
            response=json.dumps({
                "message": "Inserted link group"
            }),
            status=200,
            mimetype='application/json'
        )
        return response

    response = app.response_class(
        response=json.dumps({
            "message": "Invalid link group"
        }),
        status=422,
        mimetype='application/json'
    )
    return response


@app.route("/v1/changeStatus", methods=['POST'])
def changeStatusGroup():
    raw = request.get_json()
    idGroup = raw.get('idGroup')
    idUser = raw.get('idUser')
    status = raw.get('status')

    if idGroup != None and status != None and idUser != None:
        if connector.modifyLinkGroup(idGroup, status, idUser):
            response = app.response_class(
                response=json.dumps({
                    "message": "Changed Status"
                }),
                status=200,
                mimetype='application/json'
            )
            return response

    response = app.response_class(
        response=json.dumps({
            "message": "Invalid idGroup or status"
        }),
        status=422,
        mimetype='application/json'
    )
    return response


@app.route("/v1/review", methods=['GET'])
def pendingList():

    pendingList = connector.getPending()

    content = OrderedDict()
    content['count'] = len(pendingList)
    content['record'] = list()

    for items in pendingList:
        tempRecord = OrderedDict()
        tempRecord['id'] = items['id']
        tempRecord['linkGroup'] = items['linkGroup']
        tempRecord['status'] = connector.statusKey(items['status'])

        tempRecord['summary'] = items['summary']

        tempRecord['idUser'] = items['idUser']

        tempRecord['reviewTime'] = items['reviewTime']

        content['record'].append(tempRecord)

    response = app.response_class(
        response=json.dumps(content),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/v1/login", methods=['POST'])
def login():
    raw = request.get_json()

    username = raw.get('username')
    password = raw.get('password')

    check = connector.getUser(username, password)

    if check == 0:
        response = app.response_class(
            response=json.dumps({
                "id": None,
                "username": None,
                "message": "Fail login"
            }),
            status=422,
            mimetype='application/json'
        )
        return response

    response = app.response_class(
        response=json.dumps({
            "id": check,
            "username": username,
            "message": "Login successful"
        }),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/v1/completed", methods=['GET'])
def completed():
    reviewed = connector.getReviewedGroup()

    content = OrderedDict()
    content['count'] = len(reviewed)
    content['record'] = list()

    for i in reviewed:
        tempDict = OrderedDict(i)
        if i.get("status") == "True":
            tempDict['link'] = connector.getInfoReview(i.get("id"))
            tempDict['stats'] = countAnimal(i.get("id"))
        else:
            tempDict['link'] = None
            tempDict['stats'] = None
        content['record'].append(tempDict)

    response = app.response_class(
        response=json.dumps(content),
        status=200,
        mimetype='application/json'
    )
    return response

def summary(id):
    temp = connector.getAllPost(id)
    listContent = list()
    for i in temp:
        listContent.append(i.get("content"))
    connector.addSummary(id, summarization_model(listContent))

def countAnimal(id):
    temp = connector.getAllPost(id)
    listContent = list()
    for i in temp:
        listContent.append(i.get("content"))
    return count_animals(listContent)


# if __name__ == "__main__":
    # summary(1)
    # summary(2)
    # summary(3)
    # summary(4)
    # summary(5)
    