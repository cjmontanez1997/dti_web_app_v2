import os, json, random, shutil
from tqdm import tqdm
import Configurations as c
from modules.Connections import mysql,sqlite
from controllers.value_cleaner import file_handler

# rapid_sqlite = sqlite(c.SQLITE_DB)
rapid_mysql = mysql(*c.DB_CRED)


class form_a1_handler:
	def __init__(self,args):
		super(form_a1_handler, self).__init__()
		self.args = args

	def profile_info_farmer(self,path):
		f = open(c.RECORDS+"/objects/profiling_forms/queued/pf_a/"+ path, "r")
		# f = open(c.RECORDS+"/objects/profiling_forms/queued/_temp_/"+ path, "r")
		strsd = f.read()
		f.close()
		prof_1 = "ERROR"
		prof_1 = json.loads(json.loads(strsd));
		prof_1['addr_region'] = file_handler.region_name_cleaner(prof_1['addr_region'])
		prof_1['farmer-primary_crop'] = file_handler.crops_name_cleaner(prof_1['farmer-primary_crop'])
		prof_1['farmer-fo_name_rapid']  = file_handler.other_name_cleaner(prof_1['farmer-fo_name_rapid'])
		prof_1['farmer_dip_ref']  = file_handler.other_name_cleaner(prof_1['farmer_dip_ref'])
		# prof_1['farmer_img_base64'] = "";
		prof_1['SOURCE'] = "MOBILE";
		return prof_1

	def push_mysql(self,data_,FILENAME):
		path_img_res = c.RECORDS+"/objects/img_resource/farmer_profile_img/"
		fields = ""
		vals = ""

		farmer_code = data_["farmer_code"]  # get farmer code
		img_data = data_["farmer_img_base64"] # get img_data for storing
		filename_img = "farmer_profile_img_{}".format(farmer_code) # generate filename for img_data

		if(len(img_data)>=20):
			fff = open(path_img_res+filename_img,"w")
			fff.write(img_data)
			fff.close()

		data_["farmer_img_base64"] = filename_img # #force value for mysql - VALUE = FILENAME
		
		for datum in data_:
			datum_ = datum.replace("-","_")
			fields = fields + ",`"+ datum_ +"`"
			datum_val = data_[datum]
			vals = vals + ",'"+ str(datum_val).replace("'"," ").replace('''"'''," ") +"'"
			
		fields = fields[1:]; vals = vals[1:]

		file_to_sql.insert_sql_move_file("a1","form_a_farmer_profiles",fields,vals,FILENAME)

		pass
# =====================================================================================================
# =====================================================================================================
# ================FARM LAND INFO=====================================================================================
# =====================================================================================================
class form_a2_handler:
	def __init__(self,args):
		super(form_a2_handler, self).__init__()
		self.args = args


	def profile_info_farmer(self,path):
		f = open(c.RECORDS+"/objects/profiling_forms/queued/pf_a/"+ path, "r")
		# f = open(c.RECORDS+"/objects/profiling_forms/queued/_temp_/"+ path, "r")
		strsd = f.read()
		f.close()
		prof_1 = "ERROR"
		prof_1 = json.loads(json.loads(strsd));
		prof_1['addr_region'] = file_handler.region_name_cleaner(prof_1['addr_region'])
		prof_1['SOURCE'] = "MOBILE";
		return prof_1

	def push_mysql(sef,data_,FILENAME):
		path_img_res = c.RECORDS+"/objects/img_resource/farmland_img/"
		fields = ""
		vals = ""

		farmer_code = data_["farmer_code"]  # get farmer code
		img_data = data_["farm-photo"] # get img_data for storing
		filename_img = "farmland_img{}".format(farmer_code) # generate filename for img_data

		if(len(img_data)>=20):
			fff = open(path_img_res+filename_img,"w")
			fff.write(img_data)
			fff.close()

		data_["farm-photo"] = filename_img # #force value for mysql - VALUE = FILENAME
		
		for datum in data_:
			datum_ = datum.replace("-","_")
			fields = fields + ",`"+ datum_ +"`"
			datum_val = data_[datum]
			vals = vals + ",'"+ str(datum_val).replace("'"," ").replace('''"'''," ") +"'"
			
		fields = fields[1:]; vals = vals[1:]

		file_to_sql.insert_sql_move_file("a2","form_a_farm_land",fields,vals,FILENAME)

		pass
# =====================================================================================================
# =====================================================================================================
# ================HOUSE HOLd PROFILE=====================================================================================
# =====================================================================================================
class form_a3_handler:
	def __init__(self,args):
		super(form_a3_handler, self).__init__()
		self.args = args


	def profile_info_farmer(self,path):
		f = open(c.RECORDS+"/objects/profiling_forms/queued/pf_a/"+ path, "r")
		# f = open(c.RECORDS+"/objects/profiling_forms/queued/_temp_/"+ path, "r")
		strsd = f.read()
		f.close()
		prof_1 = "ERROR"
		prof_1 = json.loads(json.loads(strsd));
		prof_1['SOURCE'] = "MOBILE";
		return prof_1

	def push_mysql(sef,data_,FILENAME):
		fields = ""
		vals = ""
		
		for datum in data_:
			datum_ = datum.replace("-","_")
			fields = fields + ",`"+ datum_ +"`"
			datum_val = data_[datum]
			vals = vals + ",'"+ str(datum_val).replace("'"," ").replace('''"'''," ") +"'"
			
		fields = fields[1:]; vals = vals[1:]

		file_to_sql.insert_sql_move_file("a3","form_a_hh_profile",fields,vals,FILENAME)

		pass
# =====================================================================================================
# =====================================================================================================
# ================PRODUCTION COST=====================================================================================
# =====================================================================================================
class form_a4_handler:
	def __init__(self,args):
		super(form_a4_handler, self).__init__()
		self.args = args

	def profile_info_farmer(self,path):
		f = open(c.RECORDS+"/objects/profiling_forms/queued/pf_a/"+ path, "r")
		# f = open(c.RECORDS+"/objects/profiling_forms/queued/_temp_/"+ path, "r")
		strsd = f.read()
		f.close()
		prof_1 = "ERROR"
		prof_1 = json.loads(json.loads(strsd));
		prof_1['SOURCE'] = "MOBILE";
		return prof_1

	def push_mysql(sef,data_,FILENAME):
		fields = ""
		vals = ""
		
		for datum in data_:
			datum_ = datum.replace("-","_")
			fields = fields + ",`"+ datum_ +"`"
			datum_val = data_[datum]
			vals = vals + ",'"+ str(datum_val).replace("'"," ").replace('''"'''," ") +"'"
			
		fields = fields[1:]; vals = vals[1:]

		file_to_sql.insert_sql_move_file("a4","form_a_prod_cost",fields,vals,FILENAME)

		pass
# =====================================================================================================
# =====================================================================================================
# ================WORKERS AND LABORERS=====================================================================================
# =====================================================================================================
class form_a5_handler:
	def __init__(self,args):
		super(form_a5_handler, self).__init__()
		self.args = args


	def profile_info_farmer(self,path):
		f = open(c.RECORDS+"/objects/profiling_forms/queued/pf_a/"+ path, "r")
		# f = open(c.RECORDS+"/objects/profiling_forms/queued/_temp_/"+ path, "r")
		strsd = f.read()
		f.close()
		prof_1 = "ERROR"
		prof_1 = json.loads(json.loads(strsd));
		prof_1['SOURCE'] = "MOBILE";
		return prof_1

	def push_mysql(sef,data_,FILENAME):
		fields = ""
		vals = ""
		
		for datum in data_:
			datum_ = datum.replace("-","_")
			fields = fields + ",`"+ datum_ +"`"
			datum_val = data_[datum]
			vals = vals + ",'"+ str(datum_val).replace("'"," ").replace('''"'''," ") +"'"
			
		fields = fields[1:]; vals = vals[1:]

		file_to_sql.insert_sql_move_file("a5","form_a_farm_workers_laborers",fields,vals,FILENAME)

		pass


# =====================================================================================================
# =====================================================================================================
# ================form_a_farm_post_harvest=====================================================================================
# =====================================================================================================
class form_a6_handler:
	def __init__(self,args):
		super(form_a6_handler, self).__init__()
		self.args = args

	def profile_info_farmer(self,path):
		f = open(c.RECORDS+"/objects/profiling_forms/queued/pf_a/"+ path, "r")
		# f = open(c.RECORDS+"/objects/profiling_forms/queued/_temp_/"+ path, "r")
		strsd = f.read()
		f.close()
		prof_1 = "ERROR"
		prof_1 = json.loads(json.loads(strsd));
		prof_1['SOURCE'] = "MOBILE";
		return prof_1

	def push_mysql(sef,data_,FILENAME):
		path_img_res = c.RECORDS+"/objects/img_resource/post_harvest_img/"

		post_harvest_fields = {"record_num":[],"record_duplicate_id":[],"farmer_code":[],"is_synced":[],"datetime":[],"post_harv-type_faci_equip":[],"post_harv-type_faci_equip_name":[],"farmer-coords_long":[],"farmer-coords_lat":[],"addr_region":[],"addr_prov":[],"addr_city":[],"addr_brgy":[],"addr_street_purok_sitio":[],"post_harv-ph_product_form":[],"post_harv-phcropothers":[],"post_harv-capacity":[],"post_harv-capacity_unit":[],"post_harv-capacity_unit_time":[],"post_harv-photo":[],"form-remarks":[],"USER_ID":[]}

		fields = ""
		vals = ""
		img_data = []
		fname = "post_harvest_img_{}".format(data_["farmer_code"])
		for datum in data_:
			for ph_field in post_harvest_fields:
				if("post_harv-photo" in datum):
					# print("post_harv-photo || {}".format(data_[datum]))
					if(len(data_[datum])>=30):
						img_data.append(data_[datum])
						data_[datum] = fname
				if(ph_field in datum):
					post_harvest_fields[ph_field].append(data_[datum])


		# CHECK IF IMG_DATA has Image base64
		if(len(str(img_data))>=10):
			fff = open(path_img_res+fname,"w")
			fff.write(json.dumps(img_data))
			fff.close()


		# CONVERT TO SQL FORMAT
		for datum in post_harvest_fields:
			datum_ = datum.replace("-","_")
			fields = fields + ",`"+ datum_ +"`"
			datum_val = post_harvest_fields[datum]
			if(datum=="farmer_code" or datum=="USER_ID"):
				datum_val = str(str(datum_val).replace("[","").replace("]","")).replace(" ","")  # REMOVE BRACKERS FROM STRING IN ID
				vals = vals + ",'"+ str(datum_val).replace("'","").replace('''"''',"") +"'"
			else:
				vals = vals + ",'"+ str(datum_val).replace("'"," ").replace('''"'''," ") +"'"

			
		fields = fields[1:]; vals = vals[1:]


		file_to_sql.insert_sql_move_file("a6","form_a_farm_post_harvest",fields,vals,FILENAME)

		pass


# =====================================================================================================
# =====================================================================================================
# ======================marketing_sales===============================================================================
# =====================================================================================================
class form_a7_handler:
	def __init__(self,args):
		super(form_a7_handler, self).__init__()
		self.args = args

	def profile_info_farmer(self,path):
		f = open(c.RECORDS+"/objects/profiling_forms/queued/pf_a/"+ path, "r")
		# f = open(c.RECORDS+"/objects/profiling_forms/queued/_temp_/"+ path, "r")
		strsd = f.read()
		f.close()
		prof_1 = "ERROR"
		prof_1 = json.loads(json.loads(strsd));
		prof_1['SOURCE'] = "MOBILE";
		return prof_1

	def push_mysql(sef,data_,FILENAME):
		marketing_sales_fields = {"record_num":[],"farmer_code":[],"is_synced":[],"datetime":[],"market-primary_crop_type":[],"market-primary_vol_del":[],"market-is_coop":[],"market-is_sme":[],"market-is_anchor_firm":[],"market-is_negosyo_center":[],"market-is_others":[],"market-name_coop":[],"market-name_sme":[],"market-name_anchor_firm":[],"market-name_others":[],"market-primary_crop_dist_point":[],"market-primary_crop_dist_others":[],"market-primary_crop_type_buyer":[],"market-primary_crop_buyer_others":[],"market-primary_crop_product_fgp":[],"market-primary_crop_product_fgp_unit":[],"form-remarks":[],"USER_ID":[]}
		fields = ""
		vals = ""

		for datum in data_:
			for ph_field in marketing_sales_fields:
				if(ph_field in datum):
					marketing_sales_fields[ph_field].append(data_[datum])



		for datum in marketing_sales_fields:
			datum_ = datum.replace("-","_")
			fields = fields + ",`"+ datum_ +"`"
			datum_val = marketing_sales_fields[datum]
			if(datum=="farmer_code" or datum=="USER_ID"):
				datum_val = str(str(datum_val).replace("[","").replace("]","")).replace(" ","")  # REMOVE BRACKERS FROM STRING IN ID
				vals = vals + ",'"+ str(datum_val).replace("'","").replace('''"''',"") +"'"
			else:
				vals = vals + ",'"+ str(datum_val).replace("'"," ").replace('''"'''," ") +"'"

			
		fields = fields[1:]; vals = vals[1:]

		file_to_sql.insert_sql_move_file("a7","form_a_farm_marketing_sales",fields,vals,FILENAME)

		pass

# =====================================================================================================
# =====================================================================================================
# ======================access_financial===============================================================================
# =====================================================================================================
class form_a8_handler:
	def __init__(self,args):
		super(form_a8_handler, self).__init__()
		self.args = args

	def profile_info_farmer(self,path):
		f = open(c.RECORDS+"/objects/profiling_forms/queued/pf_a/"+ path, "r")
		# f = open(c.RECORDS+"/objects/profiling_forms/queued/_temp_/"+ path, "r")
		strsd = f.read()
		f.close()
		prof_1 = "ERROR"
		prof_1 = json.loads(json.loads(strsd));
		prof_1['SOURCE'] = "MOBILE";
		return prof_1

	def push_mysql(sef,data_,FILENAME):
		fields = ""
		vals = ""
		
		for datum in data_:
			datum_ = datum.replace("-","_")
			fields = fields + ",`"+ datum_ +"`"
			datum_val = data_[datum]
			vals = vals + ",'"+ str(datum_val).replace("'"," ").replace('''"'''," ") +"'"
			
		fields = fields[1:]; vals = vals[1:]

		file_to_sql.insert_sql_move_file("a8","form_a_access_financial",fields,vals,FILENAME)

		pass
		
# =====================================================================================================
# =====================================================================================================
# ======================feedback===============================================================================
# =====================================================================================================
class form_a9_handler:
	def __init__(self,args):
		super(form_a9_handler, self).__init__()
		self.args = args

	def profile_info_farmer(self,path):
		f = open(c.RECORDS+"/objects/profiling_forms/queued/pf_a/"+ path, "r")
		# f = open(c.RECORDS+"/objects/profiling_forms/queued/_temp_/"+ path, "r")
		strsd = f.read()
		f.close()
		prof_1 = "ERROR"
		prof_1 = json.loads(json.loads(strsd));
		prof_1['SOURCE'] = "MOBILE";
		return prof_1

	def push_mysql(sef,data_,FILENAME):
		feedback_fields = {"record_num": [],"farmer_code": [],"is_synced": [],"datetime": [],"feedback-num_of_trainings_2_3_years": [],"farmer-Cacao": [],"farmer-Coffee": [],"farmer-Coconut": [],"farmer-Banana": [],"farmer-Calamansi": [],"farmer-Jackfruit": [],"farmer-Mango": [],"farmer-Pili_Nut": [],"farmer-Other_fruits_nuts": [],"farmer-Others": [],"feedback-cert_acquired": [],"feedback-support_need": [],"feedback[]-media": [],"feedback[]-freq": [],"feedback-type_mobile": [],"feedback-commnets": [],"feedback-remarks": [],"USER_ID": []}
		fields = ""
		vals = ""

		for datum in data_:
			for ph_field in feedback_fields:
				if(ph_field in datum):
					feedback_fields[ph_field].append(data_[datum])

		for datum in feedback_fields:
			datum_ = datum.replace("-","_").replace("[]","_array")
			fields = fields + ",`"+ datum_ +"`"
			datum_val = feedback_fields[datum]
			if(datum=="farmer_code" or datum=="USER_ID"):
				datum_val = str(str(datum_val).replace("[","").replace("]","")).replace(" ","")  # REMOVE BRACKERS FROM STRING IN ID
				vals = vals + ",'"+ str(datum_val).replace("'","").replace('''"''',"") +"'"
			else:
				vals = vals + ",'"+ str(datum_val).replace("'"," ").replace('''"'''," ") +"'"

			
		fields = fields[1:]; vals = vals[1:]

		file_to_sql.insert_sql_move_file("a9","form_a_feedback",fields,vals,FILENAME)

		pass


# ================================MAIN=============================
CONN = rapid_mysql.db_ready()

class form_migration:
	def __init__(self,args):
		super(form_migration, self).__init__()
		self.args = args

	def get_all(self):
		res = []
		dir_path = c.RECORDS+"/objects/profiling_forms/queued/pf_a/";
		# dir_path = c.RECORDS+"/objects/profiling_forms/queued/_temp_/";
		_title = "----";
		loads_ = tqdm(os.listdir(dir_path),  desc =_title,ascii ="►>○•|█");
		_counter = 0
		__a = [0,0,0,0,0,0,0,0,0,0]
		for path in loads_:
			if os.path.isfile(os.path.join(dir_path, path)):
				if(path.find("@profile")>=0):
					_CLASS_ = form_a1_handler(__name__)
					__a[1] = __a[1] + 1
				elif(path.find("@add_farm")>=0):
					_CLASS_ = form_a2_handler(__name__)
					__a[2] = __a[2] + 1
				elif(path.find("@hh_profile")>=0):
					_CLASS_ = form_a3_handler(__name__)
					__a[3] = __a[3] + 1
				elif(path.find("@prod_cost")>=0):
					_CLASS_ = form_a4_handler(__name__)
					__a[4] = __a[4] + 1
				elif(path.find("@workers_laborers")>=0):
					_CLASS_ = form_a5_handler(__name__)
					__a[5] = __a[5] + 1
				elif(path.find("@post_harvest")>=0):
					_CLASS_ = form_a6_handler(__name__)
					__a[6] = __a[6] + 1
				elif(path.find("@marketing_sales")>=0):
					_CLASS_ = form_a7_handler(__name__)
					__a[7] = __a[7] + 1
				elif(path.find("@access_financial")>=0):
					_CLASS_ = form_a8_handler(__name__)
					__a[8] = __a[8] + 1
				elif(path.find("@feedback")>=0):
					_CLASS_ = form_a9_handler(__name__)
					__a[9] = __a[9] + 1
				else:
					continue
				__a[0] == _counter
				loads_.desc = ('''inserted [{}] A1 [{}]  A2 [{}] A3 [{}] A4 [{}] A5 [{}] A6 [{}] A7 [{}] A8 [{}] A9 [{}] ''').format(*__a)
				try:
					data_ = _CLASS_.profile_info_farmer(path)
					_CLASS_.push_mysql(data_,path)
					res.append(path)
					_counter = _counter + 1
				except ValueError:
					print("json error || [{}]".format(path))
					# return ({"response":"error","message":ValueError})
				except Exception as ex:
					template = "An exception of type {0} occurred. Arguments:\n{1!r}"
					message = template.format(type(ex).__name__, ex.args)
					print(message)
					return ({"response":"error","message":message,"file":path})
		random.shuffle(res)
		CONN.commit()
		return res

class file_to_sql:
	def insert_sql_move_file(mv_file_to,table,fields,vals,FILENAME):
		sql = ("INSERT INTO `{}` ({}) VALUES ({})".format(table,fields,vals))
		# rapid_mysql.do(sql)
		resp = rapid_mysql.do_(sql,CONN)
		# shutil.copy(
		# 	c.RECORDS+"/objects/profiling_forms/queued/pf_a/"+FILENAME,
		# 	c.RECORDS+"/objects/profiling_forms/migrated/pf_a/{}/{}".format(mv_file_to,FILENAME)
		# )
		shutil.move(
			c.RECORDS+"/objects/profiling_forms/queued/pf_a/"+FILENAME,
			c.RECORDS+"/objects/profiling_forms/migrated/pf_a/{}/{}".format(mv_file_to,FILENAME)
		)