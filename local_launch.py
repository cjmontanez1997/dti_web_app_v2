import Configurations as c
def _init_config_():
	c.SQLITE_DB = c.SQLITE_DB_LOCAL
	c.RECORDS = c.RECORDS_LOCAL
	c.M_APPVER = c.M_APPVER_LOCAL

	c._SERVER_PORT = c.LOCAL_PORT
	c._HOST = c.LOCAL_HOST
	c._USER = c.LOCAL_USER
	c._PASSWORD = c.LOCAL_PASSWORD
	c._DATABASE = c.LOCAL_DATABASE
	c.DB_CRED = [c.LOCAL_HOST,c.LOCAL_USER,c.LOCAL_PASSWORD,c.LOCAL_DATABASE] # DEV
	c.PORT = 80
# ===========================================================================
print(" * LOCAL Launch")

_init_config_()
import start_point as sp
_init_config_()
app = sp.app
# app.run(host=c.HOST,port=c._PORT,debug=c.IS_DEBUG,ssl_context='adhoc') 
app.run(host=c.HOST,port=c._PORT,debug=c.IS_DEBUG)
# app.run(debug=c.IS_DEBUG)

