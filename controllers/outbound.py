import Configurations as c
import os, random, json
import pandas as pd
import openpyxl
from datetime import datetime
from controllers.inbound import inbound



class outbound:
	"""docstring for outbound"""
	def __init__(self, app,db,session):
		super(outbound, self).__init__()
		self.app = app
		self.db = db
		self.session = session
		self.inb = inbound(self.app,self.db,self.session)
		
	def _test_(self):
		print(" * Testing outbound | {} | {}".format(self.session,self.app))
		pass

	def export_excel_mobile(self,form):
		DATE_NOW = str(datetime.today()).replace("-","_").replace(" ","_").replace(":","_").replace(".","_")
		USER_ID = self.session["USER_DATA"][0]["id"]
		print(" *  Generating and Running SQL [{}]".format(form))
		form_a_farm_land = self.db.select('''
				SELECT
					form_a_farmer_profiles.*,
					{}.*
				   
				FROM `form_a_farmer_profiles` 
				INNER JOIN {} ON form_a_farmer_profiles.farmer_code = {}.farmer_code

				WHERE
				   form_a_farmer_profiles.USER_ID in (SELECT users.id from users {} );
			'''.format(form,form,form,self.position_data_filter()))

		

		DATA = form_a_farm_land
		# dict_= json.loads(res)
		# df2 = pd.DataFrame.from_dict(dict_, orient="index")
		print(" *  Generating DATA FRAME ")
		df_nested_list = pd.json_normalize(DATA)
		# print(res[0])
		print(df_nested_list)
		print(" *  Writing to spreadsheet ")
		FILE_NAME_EXPORTED = '{}_{}_{}.xlsx'.format(USER_ID,form,DATE_NOW)
		__TO_DL_EXCEL = c.RECORDS+'/objects/spreadsheets/exports/'+FILE_NAME_EXPORTED
		writer = pd.ExcelWriter(__TO_DL_EXCEL) 
		print(" *  Saving spreadsheet. . .  ")
		df_nested_list.to_excel(writer, sheet_name='mobile_imports',index=False )
		writer.save()
		print(" *  Saving spreadsheet DOne ")

		notif_cont = "Your file export named [{}] has been created click <b>here</b> to download".format(FILE_NAME_EXPORTED)
		self.inb.push_notif("Excel Export Status","export_excel",notif_cont,"dlexcel",FILE_NAME_EXPORTED)
		return {"Status":"done","file_name":FILE_NAME_EXPORTED}

	def export_excel_excel(self):
		DATE_NOW = str(datetime.today()).replace("-","_").replace(" ","_").replace(":","_").replace(".","_")
		USER_ID = self.session["USER_DATA"][0]["id"]
		print(" *  Generating and Running SQL [For all in Excel Uploads]")
		EXCEL_UPLOADS = self.db.select('''
				SELECT
					excel_import_form_a.*
				   
				FROM `excel_import_form_a` 

				WHERE
				   excel_import_form_a.user_id in (SELECT users.id from users {} );
			'''.format(self.position_data_filter_excel()))
		DATA = EXCEL_UPLOADS
		# dict_= json.loads(res)
		# df2 = pd.DataFrame.from_dict(dict_, orient="index")
		print(" *  Generating DATA FRAME ")
		df_nested_list = pd.json_normalize(DATA)
		# print(res[0])
		print(df_nested_list)
		print(" *  Writing to spreadsheet ")
		FILE_NAME_EXPORTED = '{}_{}_{}.xlsx'.format(USER_ID,"EXCEL_UPLOADS",DATE_NOW)
		__TO_DL_EXCEL = c.RECORDS+'/objects/spreadsheets/exports/'+FILE_NAME_EXPORTED
		writer = pd.ExcelWriter(__TO_DL_EXCEL) 
		print(" *  Saving spreadsheet. . .  ")
		df_nested_list.to_excel(writer, sheet_name='mobile_imports',index=False )
		writer.save()
		print(" *  Saving spreadsheet DOne ")

		notif_cont = "Your file export named [{}] has been created click <b>here</b> to download".format(FILE_NAME_EXPORTED)
		self.inb.push_notif("Excel Export Status","export_excel",notif_cont,"dlexcel",FILE_NAME_EXPORTED)
		return {"Status":"done","file_name":FILE_NAME_EXPORTED}

	def position_data_filter(self):
		_filter = "WHERE 1 "
		JOB = self.session["USER_DATA"][0]["job"].lower()

		if(JOB in "admin" or JOB in "super admin"):
			self.session["USER_DATA"][0]["office"] = "NPCO"
			_filter = "WHERE 1 "
		else:
			self.session["USER_DATA"][0]["office"] = "Regional ({})".format(self.session["USER_DATA"][0]["rcu"])
			_filter = "WHERE  form_a_farmer_profiles.USER_ID in ( SELECT users.id from users WHERE rcu='{}' )".format(self.session["USER_DATA"][0]["rcu"])

		return _filter

	def position_data_filter_excel(self):
		_filter = "WHERE 1 "
		JOB = self.session["USER_DATA"][0]["job"].lower()

		if(JOB in "admin" or JOB in "super admin"):
			self.session["USER_DATA"][0]["office"] = "NPCO"
			_filter = "WHERE 1 "
		else:
			self.session["USER_DATA"][0]["office"] = "Regional ({})".format(self.session["USER_DATA"][0]["rcu"])
			_filter = "WHERE  excel_import_form_a.USER_ID in ( SELECT users.id from users WHERE rcu='{}' )".format(self.session["USER_DATA"][0]["rcu"])

		return _filter


	# def export_excel(self):
	# 	DATE_NOW = datetime.today().strftime('%Y-%m-%d')
	# 	USER_ID = self.session["USER_DATA"][0]["id"]
	# 	print(" *  Generating SQL ")
	# 	sql = ('''
	# 			SELECT
	# 				form_a_farmer_profiles.*,
	# 				form_a_farm_land.*
	# 				-- form_a_hh_profile.*,
	# 				-- form_a_prod_cost.*,
	# 				-- form_a_farm_workers_laborers.*,
	# 				-- -- form_a_farm_post_harvest.*,
	# 				-- -- form_a_farm_marketing_sales.*,
	# 				-- form_a_access_financial.*,
	# 				-- form_a_feedback.*
				   
	# 			FROM `form_a_farmer_profiles` 
	# 			INNER JOIN form_a_farm_land ON form_a_farmer_profiles.farmer_code = form_a_farm_land.farmer_code
	# 			-- INNER JOIN form_a_hh_profile ON form_a_farmer_profiles.farmer_code = form_a_hh_profile.farmer_code
	# 			-- INNER JOIN form_a_prod_cost ON form_a_farmer_profiles.farmer_code = form_a_prod_cost.farmer_code
	# 			-- INNER JOIN form_a_farm_workers_laborers ON form_a_farmer_profiles.farmer_code = form_a_farm_workers_laborers.farmer_code
	# 			-- -- INNER JOIN form_a_farm_post_harvest ON form_a_farmer_profiles.farmer_code = form_a_farm_post_harvest.farmer_code
	# 			-- -- INNER JOIN form_a_farm_marketing_sales ON form_a_farmer_profiles.farmer_code = form_a_farm_marketing_sales.farmer_code
	# 			-- INNER JOIN form_a_access_financial ON form_a_farmer_profiles.farmer_code = form_a_access_financial.farmer_code
	# 			-- INNER JOIN form_a_feedback ON form_a_farmer_profiles.farmer_code = form_a_feedback.farmer_code

	# 			WHERE
	# 			   form_a_farmer_profiles.USER_ID in (SELECT users.id from users {} );
	# 		'''.format(self.position_data_filter()))

	# 	print(" *  Generating SQL ")
	# 	res = self.db.select(sql)

	# 	# dict_= json.loads(res)
	# 	# df2 = pd.DataFrame.from_dict(dict_, orient="index")
	# 	print(" *  Generating DATA FRAME ")
	# 	df_nested_list = pd.json_normalize(res)
	# 	# print(res[0])
	# 	print(df_nested_list)
	# 	print(" *  Writing to spreadsheet ")
	# 	__TO_DL_EXCEL = c.RECORDS+'/objects/spreadsheets/exports/{}_{}.xlsx'.format(USER_ID,DATE_NOW)
	# 	writer = pd.ExcelWriter(__TO_DL_EXCEL) 
	# 	print(" *  Saving spreadsheet. . .  ")
	# 	df_nested_list.to_excel(writer, sheet_name='mobile_imports',index=False )
	# 	writer.save()
	# 	print(" *  Saving spreadsheet DOne ")

	# 	return {"Status":"done","file_name":"{}_{}.xlsx".format(USER_ID,DATE_NOW)}