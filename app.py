import Configurations as c
def _init_config_():
	c.SQLITE_DB = c.SQLITE_DB_SERVER
	c.RECORDS = c.RECORDS_SERVER
	c.M_APPVER = c.M_APPVER_SERVER

	c._SERVER_PORT = c.SERVER_PORT
	c._HOST = c.SERVER_HOST
	c._USER = c.SERVER_USER
	c._PASSWORD = c.SERVER_PASSWORD
	c._DATABASE = c.SERVER_DATABASE
	c.DB_CRED = [c.SERVER_HOST,c.SERVER_USER,c.SERVER_PASSWORD,c.SERVER_DATABASE] # DEV
	c.PORT = 80
# ======================================================================
print(" * Providing Imports Flask app")

_init_config_()
import start_point as sp
_init_config_()
app = sp.app
# app.run(host=c.HOST,port=c._PORT,debug=c.IS_DEBUG,ssl_context='adhoc')
# app.run(host=c.HOST,port=c._PORT,debug=c.IS_DEBUG)
