from flask import jsonify
import requests
from app import app
from app.database.config import db
from app.models.errorHandling import errorHandling
from app.models.clients import getClient

clients_db = db.clients_db


def getProduct(product_id):
    response = requests.get(f'http://challenge-api.luizalabs.com/api/product/{product_id}')

    if response.ok:
        return response.json()


def findProduct(client_id, product_id):
    return clients_db.find_one({"_id": int(client_id), "product": {"$elemMatch": {"id": product_id}}})


def addProduct(client_id, product_id):
    errorHandl = errorHandling('', {})

    if client_id.isdigit():
        client = getClient('_id', int(client_id))
        product = getProduct(product_id)

        if product and client:
            find = findProduct(client_id, product_id)

            if not find:
                clients_db.update_one(client, {"$push": {"product": product}})
                errorHandl.message = 'Favorite product was successfully added.'
                errorHandl.object = getProduct(product_id)
                return errorHandl.getReturn(), 200

            else:
                errorHandl.message = 'Client already added this favorite product.'
                return errorHandl.getReturn(), 200

        else:
            errorHandl.message = 'No product or client found.'
            return errorHandl.getReturn(), 200

    else:
        errorHandl.message = 'Invalid parameters!.'
        return errorHandl.getReturn(), 404


def deleteProduct(client_id, product_id):
    errorHandl = errorHandling('', {})

    if client_id.isdigit():
        client = getClient('_id', int(client_id))
        product = getProduct(product_id)

        if product and client:
            find = findProduct(client_id, product_id)

            if find:
                prod = getProduct(product_id)
                clients_db.update_one(client, {"$pull": {"product": product}})
                errorHandl.message = 'Favorite product was successfully removed.'
                errorHandl.object = prod
                return errorHandl.getReturn(), 200

            else:
                errorHandl.message = 'No product found.'
                return errorHandl.getReturn(), 200

        else:
            errorHandl.message = 'No product or client found.'
            return errorHandl.getReturn(), 200

    else:
        errorHandl.message = 'Invalid parameters!.'
        return errorHandl.getReturn(), 404


def getProducts(client_id):
    errorHandl = errorHandling('', {})

    if client_id.isdigit():
        client = getClient('_id', int(client_id))

        if client:
            return jsonify(client)

        else:
            errorHandl.message = 'No client found.'
            return errorHandl.getReturn(), 200

    else:
        errorHandl.message = 'Invalid parameters!.'
        return errorHandl.getReturn(), 404
