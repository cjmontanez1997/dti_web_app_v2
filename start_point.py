import Configurations as c

from flask import Flask, session, jsonify, request, redirect
from flask_cors import CORS,cross_origin
from flask_minify import Minify

from views.login import login
from views.home  import home
from views.webrep  import webrep
from views.feature_0  import feature_0
from views.psalm  import bp_app

from modules.public_vars import public_vars
from controllers.inbound import inbound
from apis import api

app = Flask(__name__)
# Minify(app=app, html=True, js=True, cssless=True)
app.config['JSON_SORT_KEYS'] = False
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
app.secret_key=c.SECRET_KEY
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.register_blueprint(login.app)
app.register_blueprint(home.app)
app.register_blueprint(api.app)
app.register_blueprint(feature_0.app)
app.register_blueprint(webrep.app)
app.register_blueprint(bp_app.app)

@app.route("/")
def index():return redirect("/rapid/home.html")


@app.before_request
def before_request():
	if( request.endpoint != "static" and "Handshake" not in str(request.endpoint).split(".")):
		if "USER_DATA" not in session:
			if(request.endpoint != "login.login"):
				# return redirect('/login')
				pass
		else:
			if(request.endpoint == "login.login"):
				# return redirect('/home')
				pass
	pass