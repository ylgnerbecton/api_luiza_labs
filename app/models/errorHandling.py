from flask import jsonify


class errorHandling:

    def __init__(self, message, object):
        self.message = message
        self.object = object

    def getReturn(self):
        res = {
            'message': self.message,
            'object': self.object
        }
        return res
