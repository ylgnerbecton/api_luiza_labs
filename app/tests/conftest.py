import pytest
from app import create_app
from app.database.config import dropDB
from app.models.clients import *
from app.models.products import *


@pytest.fixture
def app():
    app = create_app()
    setup()

    yield app

    teardown()


def setup():
    dropDB()
    insertDatabase()


def teardown():
    dropDB()


def insertDatabase():
    clients_db = db.clients_db

    post('Carlos', 'carlos@email.com')
    post('Luana', 'luana@email.com')
    post('Julia', 'julia@email.com')

    addProduct('1', '77be5ad3-fa87-d8a0-9433-5dbcc3152fac')
    addProduct('2', '8cd7a789-4c93-45a1-a7d0-cb9fbc6b7edc')
    addProduct('2', '520dff12-8ec8-462b-b795-c35afbd12632')
