#!/usr/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

url = [

    {
        'id': 1,
        'title': u'url title',
        
       
    }
]

@app.route('/urlname/urlinfo/', methods=['GET'])
def get_url():
    return jsonify({'url': url})

if __name__ == '__main__':
    app.run(debug=True)