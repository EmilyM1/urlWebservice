#!/usr/bin/python

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class urlChecker(Resource):
    def get(self):
        return {'urldb': 'info'}


api.add_resource(urlChecker, '/urlname/urlinfo/1/<site_name>') # add for google.com/bad site too 

if __name__ == '__main__':
    app.run(debug=True)
