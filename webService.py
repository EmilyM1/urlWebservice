#!/usr/bin/python

import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
# from urlparse import urlparse

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class BadSite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(100), unique=True, nullable=False)

    def __init__(self,id,url):
        self.id = id
        self.url = url

    def __repr__(self):
        return '<BadSite %r>' % self.url


def create_db():
    db.create_all()
    db.session.commit()

def add_bad_urls():
    badsite1 = BadSite(1, 'http://www.badsite.com')
    badsite2 = BadSite(2, 'http://google.com/http://www.evenworsesite.com/?foo=1')
    db.session.add(badsite1)
    db.session.add(badsite2)
    db.session.commit()
    #print BadSite.query.all()

create_db();
if BadSite.query.count() <= 0:
    add_bad_urls();

# define routes
@app.route('/')
def index():
    resp = {
        'view':  {
            'uri': '/urlinfo/1/{hostname_and_port}/{original_path_and_query_string}',
            'methods': ['GET']
        }
        
    }
    return jsonify(resp)

@app.route('/urlname/1/<path:path>', methods=['GET'])
def check_url(path):
    # u = urlparse(path)
    # (scheme='http', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html', params='', query='', fragment='')
    url = path
    if request.query_string:
        url = path + '?' + request.query_string

    try:
        result = BadSite.query.filter_by(url = url).first()
        resp = {
                'url': result.url,
                'safe': False
        }
    except:
        resp = {
                'safe': True
        }

    return jsonify(resp)
    
if __name__ == '__main__':
    app.debug = True
app.run()