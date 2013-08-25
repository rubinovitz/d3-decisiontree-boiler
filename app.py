from werkzeug import SharedDataMiddleware
import os
from flask import Flask, request, Response, render_template, jsonify, make_response, session, escape, flash
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('decision-tree.html')

# store static files on server for now
app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
	'/': os.path.join(os.path.dirname(__file__), 'static')
})

if __name__ == '__main__':
	app.run(debug=True, port=8000)
