import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.clients_db


def dropDB():
    client.drop_database('clients_db')
