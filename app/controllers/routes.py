from app import app
from flask import request, jsonify
from app.models.clients import post, put, delete, get, getAll
from app.models.products import addProduct, deleteProduct, getProducts


@app.route("/client/", methods=["GET"])
def getClient():
    if "id" in request.args:
        client_id = request.args.get("id")
        client = get(client_id)

        return client

    return 'Invalid parameters!', 404


@app.route("/clients", methods=["GET"])
def getClients():
    return getAll()


@app.route("/client", methods=["POST"])
def addClient():
    if "name" in request.json:
        if "email" in request.json:
            name = request.json['name']
            email = request.json['email']

            client = post(name, email)

            return client

        return 'Invalid parameters!', 404
    return 'Invalid parameters!', 404


@app.route("/client/update/", methods=["PUT"])
def updateClient():
    if "id" in request.args:
        if "name" in request.args:
            client_id = request.args.get("id")
            new_name = request.args.get("name")

            client = put(client_id, new_name)

            return client

        return 'Invalid parameters!', 404
    return 'Invalid parameters!', 404


@app.route("/client/remove/", methods=["DELETE"])
def removeClient():
    if "id" in request.args:
        client_id = request.args.get("id")
        client = delete(client_id)

        return client

    return 'Invalid parameters!', 404


@app.route("/client/product/add/", methods=["GET"])
def addFavoriteProduct():
    if "client_id" in request.args:
        if "product_id" in request.args:
            client_id = request.args.get("client_id")
            product_id = request.args.get("product_id")

            client_product = addProduct(client_id, product_id)

            return client_product

        return 'Invalid parameters!', 404
    return 'Invalid parameters!', 404


@app.route("/client/product/remove/", methods=["DELETE"])
def removeFavoriteProduct():
    if "client_id" in request.args:
        if "product_id" in request.args:
            client_id = request.args.get("client_id")
            product_id = request.args.get("product_id")

            client_product = deleteProduct(client_id, product_id)

            return client_product

        return 'Invalid parameters!', 404
    return 'Invalid parameters!', 404


@app.route("/client/products/", methods=["GET"])
def getFavoritesProducts():
    if "client_id" in request.args:
        client_id = request.args.get("client_id")
        client_product = getProducts(client_id)

        return client_product

    return 'Invalid parameters!', 404


@app.errorhandler(404)
def notFound(e):
    return 'Page not found.', 404
