from flask import Flask

app = Flask(__name__)

app.config.from_object('config')


def create_app():
    app.config['TESTING'] = True
    return app


from app.controllers import routes
from app.models import clients
from app.models import errorHandling
from app.database import config
