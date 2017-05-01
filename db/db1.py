#!/usr/bin/python

from flask_sqlalchemy import SQLAlchemy
import os
from flask import Flask

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db=SQLAlchemy(app)

# database config

# class

class urlName(db.Model):
	__tablename__ = "urls"
	id = db.Column(db.Integer, primary_key=True)
	websiteName = db.Column(db.String(100), unique=True, nullable=False)

	def __repr__(self):
		return '<urlName %r>' % self.websiteName

print urlName.query.all()