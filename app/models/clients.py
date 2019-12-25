from flask import jsonify, Response
from app import app
from app.database.config import db
from app.models.errorHandling import errorHandling

clients_db = db.clients_db


def getClient(param, value):
    client = clients_db.find_one({param: value})

    if client:
        return client


def getNextSequenceValue():
    if int(db.counters.count_documents({})) == 0:
        db.counters.insert_one({"_id": "client_id", "sequence_value": 1})

    sequenceDocument = db.counters.find_one_and_update({"_id": "client_id"}, {"$inc": {"sequence_value": 1}})

    return int(sequenceDocument["sequence_value"])


def post(name, email):
    errorHandl = errorHandling('', {})
    client_email = getClient('email', email)

    if not client_email:
        clients_db.insert_one({"_id": getNextSequenceValue(), "name": name, "email": email})
        errorHandl.message = 'Client was successfully created.'
        errorHandl.object = getClient('email', email)
        return errorHandl.getReturn(), 201

    else:
        errorHandl.message = 'Client already exists.'
        return errorHandl.getReturn(), 200


def put(id, name):
    errorHandl = errorHandling('', {})

    if id.isdigit():
        client = getClient('_id', int(id))

        if client:
            clients_db.update_one(client, {"$set": {"name": name}})
            errorHandl.message = 'Client was successfully updated.'
            errorHandl.object = getClient('_id', int(id))
            return errorHandl.getReturn(), 200

        else:
            errorHandl.message = 'No client found.'
            return errorHandl.getReturn(), 200

    else:
        return 'Invalid parameters!.', 404


def delete(id):
    errorHandl = errorHandling('', {})

    if id.isdigit():
        client = getClient('_id', int(id))

        if client:
            clients_db.delete_one({"_id": int(id)})
            errorHandl.message = 'Client was successfully removed.'
            errorHandl.object = client
            return errorHandl.getReturn(), 200

        else:
            errorHandl.message = 'No client found.'
            return errorHandl.getReturn(), 200

    else:
        return 'Invalid parameters!.', 404


def get(id):
    errorHandl = errorHandling('', {})

    if id.isdigit():
        client = getClient('_id', int(id))

        if client:
            return jsonify(client)

        else:
            errorHandl.message = 'No client found.'
            return errorHandl.getReturn(), 200

    else:
        return 'Invalid parameters!.', 404


def getAll():
    clients = clients_db.find()
    result = []

    for client in clients:
        result.append({"id": client["_id"], "name": client["name"], "email": client["email"]})

    return jsonify(result), 200
