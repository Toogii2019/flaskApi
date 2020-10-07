#!/usr/bin/env python

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLALchemy 
from flask_marshmallow import Marshmallow
from flask_restful import Resource, Api

from model import User, UserSchema, UsersManager

app = Flask(__name__)

api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

ma = Marshmallow(app)



user_schema = UserSchema()
users_schema = UserSchema(many=True)




api.add_resource(UsersManager, '/api/users')

if __name__ == '__main__':
    app.run(debug=True)
    







