import pytest
import json
from app.controllers.routes import *


# Add a client with success.
def test_add_client_success(client):
    request = client.post('/client', json={
        'name': 'Rafael', 'email': 'rafael@email.com'
    })

    response = request.get_json()

    assert response["message"] == 'Client was successfully created.'


# Add an existing client.
def test_add_client_who_already_exist(client):
    request = client.post('/client', json={
        'name': 'Carlos', 'email': 'carlos@email.com'
    })

    response = request.get_json()

    assert response["message"] == 'Client already exists.'


# Add a client with invalid param - name.
def test_add_client_with_invalid_name_param(client):
    response = client.post('/client', json={
        'nam': 'Rafael', 'email': 'rafael@email.com'
    })

    assert response == 404


## Add a client with invalid param - email.
def test_add_client_with_invalid_email_param(client):
    response = client.post('/client', json={
        'name': 'Rafael', 'emai': 'rafael@email.com'
    })

    assert response == 404


# Get a client with success.
def test_get_client_success(client):
    request = client.get('/client/', query_string={'id': '1'})

    response = request.get_json()

    assert response["_id"] == 1


# Get a client who doenst exist.
def test_get_client_who_doesnt_exist(client):
    request = client.get('/client/', query_string={'id': '0'})

    response = request.get_json()

    assert response["message"] == 'No client found.'


# Get a client with invalid param - id.
def test_get_client_with_invalid_id_param(client):
    response = client.get('/client/', query_string={'_id': '1'})

    assert response == 404


# Get a client with invalid type.
def test_get_client_with_invalid_type(client):
    response = client.get('/client/', query_string={'id': 'invalid_type'})

    assert response == 404


# Get all clients.
def test_get_all_clients(client):
    response = client.get('/clients')

    assert response == 200


# Update a client with success.
def test_put_client_success(client):
    request = client.put('/client/update/', query_string={'id': '1', 'name': 'Carloz'})

    response = request.get_json()

    assert response["message"] == 'Client was successfully updated.'


# Update a client who doenst exist.
def test_put_client_who_doesnt_exist(client):
    request = client.put('/client/update/', query_string={'id': '0', 'name': 'Carloz'})

    response = request.get_json()

    assert response["message"] == 'No client found.'


# Update a client with invalid param - id.
def test_put_client_with_invalid_id_param(client):
    response = client.put('/client/update/', query_string={'_id': '1', 'name': 'Carloz'})

    assert response == 404


# Update a client with invalid param - name.
def test_put_client_with_invalid_name_param(client):
    response = client.put('/client/update/', query_string={'id': '1', '_name': 'Carloz'})

    assert response == 404


# Update a client with invalid type.
def test_put_client_with_invalid_type(client):
    response = client.put('/client/update/', query_string={'id': 'invalid_type', 'name': 'Carloz'})

    assert response == 404


# Remove a client with success.
def test_remove_client_success(client):
    request = client.delete('/client/remove/', query_string={'id': '1'})

    response = request.get_json()

    assert response["message"] == 'Client was successfully removed.'


# Remove a client who doenst exist.
def test_remove_client_who_doenst_exist(client):
    request = client.delete('/client/remove/', query_string={'id': '0'})

    response = request.get_json()

    assert response["message"] == 'No client found.'


# Remove a client with invalid param - id.
def test_remove_client_invalid_id_param(client):
    response = client.delete('/client/remove/', query_string={'_id': '1'})

    assert response == 404


# Remove a client with invalid type - id.
def test_remove_client_with_invalid_type(client):
    response = client.delete('/client/remove/', query_string={'id': 'invalid_type'})

    assert response == 404
