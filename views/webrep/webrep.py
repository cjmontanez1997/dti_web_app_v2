from flask import Blueprint, render_template, request, session, redirect, jsonify
from flask_session import Session
import Configurations as c


app = Blueprint("webrep",__name__,template_folder='pages')
# app = Blueprint("webrep",__name__,url_prefix='/webrep',template_folder='pages')



class _main:
	def is_on_session(): return ('USER_DATA' in session)

	def __init__(self, arg):super(_main, self).__init__();self.arg = arg

	app.errorhandler(404)

	# ======================================================================================================
	@app.route("/webrep",methods=["POST","GET"])
	def home():
		return render_template("home.html")

	@app.route("/rapid/<_>",methods=["POST","GET"])
	def home_(_):
		if(_!="home.html"):
			return _main._404(404)
		return render_template("home.html")
	# ===========================================================/

	@app.route("/rapid/<segment>/<page>",methods=["POST","GET"])
	def page_loader(segment,page):
		_main.moderator(segment,page)
		return render_template("{}/{}".format(segment,page))
	# ==================================================================


	@app.app_errorhandler(404)
	def _404(err):
		return render_template("error/404.html"), 404


	def moderator(segment,page):
		pass;
	#sample EDIT
