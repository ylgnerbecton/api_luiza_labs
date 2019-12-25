import pytest
import json
from app.controllers.routes import *

# Add client's favorite products with success.
def test_add_client_favorite_product_success(client):
    request = client.get('/client/product/add/',
                         query_string={
                             'client_id': '3',
                             'product_id': '77be5ad3-fa87-d8a0-9433-5dbcc3152fac'})

    response = request.get_json()

    assert response["message"] == 'Favorite product was successfully added.'


# Add product the client already added.
def test_add_client_favorite_product_already_added(client):
    request = client.get('/client/product/add/',
                         query_string={
                             'client_id': '1',
                             'product_id': '77be5ad3-fa87-d8a0-9433-5dbcc3152fac'})

    response = request.get_json()

    assert response["message"] == 'Client already added this favorite product.'


# Add favorite product to client who doesnt exist.
def test_add_client_favorite_product_client_doenst_exist(client):
    request = client.get('/client/product/add/',
                         query_string={
                             'client_id': '0',
                             'product_id': '77be5ad3-fa87-d8a0-9433-5dbcc3152fac'})

    response = request.get_json()

    assert response["message"] == 'No product or client found.'


# Add invalid favorite product to client.
def test_add_client_favorite_product_product_doenst_exist(client):
    request = client.get('/client/product/add/',
                         query_string={
                             'client_id': '1',
                             'product_id': '77be5ad3-fa87-d8a0-9433'})

    response = request.get_json()

    assert response["message"] == 'No product or client found.'


# Add favorite product to client with invalid param - client_id.
def test_add_client_favorite_product_invalid_client_id_param(client):
    response = client.get('/client/product/add/',
                          query_string={
                              '_client_id': '1',
                              'product_id': '6e1f37ff-d3d4-88cc-dbbf-5747a327694f'})

    assert response == 404


# Add favorite product to client with invalid param - product_id.
def test_add_client_favorite_product_invalid_client_product_param(client):
    response = client.get('/client/product/add/',
                          query_string={
                              'client_id': '1',
                              '_product_id': '6e1f37ff-d3d4-88cc-dbbf-5747a327694f'})

    assert response == 404


# Add favorite product to client with invalid client type
def test_add_client_favorite_product_invalid_client_type(client):
    response = client.get('/client/product/add/',
                          query_string={
                              'client_id': 'invalid_type',
                              'product_id': '6e1f37ff-d3d4-88cc-dbbf-5747a327694f'})

    assert response == 404


## Remove client's favorite product with success
def test_remove_client_favorite_product_success(client):
    request = client.delete('/client/product/remove/',
                            query_string={
                                'client_id': '1',
                                'product_id': '77be5ad3-fa87-d8a0-9433-5dbcc3152fac'})

    response = request.get_json()

    assert response["message"] == 'Favorite product was successfully removed.'


## Remove invalid product
def test_remove_client_favorite_product_invalid(client):
    request = client.delete('/client/product/remove/',
                            query_string={
                                'client_id': '1',
                                'product_id': '77be5ad3-fa87'})

    response = request.get_json()

    assert response["message"] == 'No product or client found.'


# Remove favorite product of a noexistent client
def test_remove_client_favorite_product_nonexistent_client(client):
    request = client.delete('/client/product/remove/',
                            query_string={
                                'client_id': '0',
                                'product_id': '77be5ad3-fa87-d8a0-9433-5dbcc3152fac'})

    response = request.get_json()

    assert response["message"] == 'No product or client found.'


# Remove a nonexistent favorite product
def test_remove_client_favorite_product_nonexistent_product(client):
    request = client.delete('/client/product/remove/',
                            query_string={
                                'client_id': '1',
                                'product_id': '6e1f37ff-d3d4-88cc-dbbf-5747a327694f'})

    response = request.get_json()

    assert response["message"] == 'No product found.'


# Remove client's favorite product with invalid param - client_id.
def test_remove_client_favorite_product_invalid_client_id_param(client):
    response = client.delete('/client/product/remove/',
                             query_string={
                                 '_client_id': '1',
                                 'product_id': '77be5ad3-fa87-d8a0-9433-5dbcc3152fac'})

    assert response == 404


# Remove client's favorite product with invalid param - product_id.
def test_remove_client_favorite_product_invalid_product_id_param(client):
    response = client.delete('/client/product/remove/',
                             query_string={
                                 'client_id': '1',
                                 '_product_id': '77be5ad3-fa87-d8a0-9433-5dbcc3152fac'})

    assert response == 404


# Remove client's favorite product with invalid client type
def test_remove_client_favorite_product_invalid_client_type(client):
    response = client.delete('/client/product/remove/',
                             query_string={
                                 'client_id': 'invalid_type',
                                 'product_id': '77be5ad3-fa87-d8a0-9433-5dbcc3152fac'})

    assert response == 404


# Get a product with success.
def test_get_client_favorite_product_success(client):
    request = client.get('/client/products/', query_string={'client_id': '1'})

    response = request.get_json()

    assert response["_id"] == 1


# Get a nonexistent client.
def test_get_client_favorite_product_client_doesnt_exist(client):
    request = client.get('/client/products/', query_string={'client_id': '0'})

    response = request.get_json()

    assert response["message"] == 'No client found.'


# Get a favorite products with invalid param - client_id.
def test_get_client_favorite_product_with_invalid_id_param(client):
    response = client.get('/client/products/', query_string={'_client_id': '1'})

    assert response == 404


# Get a favorite product with invalid client type.
def test_get_client_favorite_product_with_invalid_type(client):
    response = client.get('/client/products/', query_string={'id': 'invalid_type'})

    assert response == 404
