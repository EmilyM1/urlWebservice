#!/usr/bin/python


from flask import Flask

app = Flask(__name__)

@app.route('/stuff/<name>')
def index(name):
	return'<h1> hello world and %s! I can now map a route to a url. The url will take the get call later </h1>' %name
	

if __name__ == '__main__':
	app.run()

	#test