from flask import Blueprint, render_template, request, session, redirect, jsonify, Response,send_file
from flask_session import Session
from modules.Connections import mysql,sqlite
import Configurations as c
import os, random, json, shutil
from controllers.outbound import outbound as outb
from controllers.inbound import inbound as inb
from werkzeug.utils import secure_filename

from controllers.engine_excel_to_sql import form_excel_a_handler

app = Blueprint("feature_0",__name__,template_folder='pages')
_excel = form_excel_a_handler(__name__)
rapid_mysql = mysql(*c.DB_CRED)

outbound = outb(app,rapid_mysql,session)
inbound = inb(app,rapid_mysql,session)

# rapid = mysql(c.LOCAL_HOST,c.LOCAL_USER,c.LOCAL_PASSWORD,c.LOCAL_DATABASE)

class _main:
	def __init__(self, arg):
		print(" * main loading done")
		super(_main, self).__init__();
		self.arg = arg


	def is_on_session(): return ('USER_DATA' in session)
	# ===========================V1==========================================
	@app.route("/feature_0",methods=["POST","GET"])
	def feature_0():
		# outbound.app = app
		# outbound.db = rapid_mysql
		# outbound.session = session
		return redirect("/feature_home#dashboard")



	@app.route("/feature_home",methods=["POST","GET"])
	def feature_0page():
		# return render_template("SITE_OFF.html") # MAINTENANCE
		Filter.position_data_filter() # initialize restrictions
		if(_main.is_on_session()):
			_main.settings(request.args)
			return render_template("feature_0_home.html",USER_DATA = session["USER_DATA"][0], dash_data_=_main.dashboard_home_sql_driven())
		else:
			return redirect("/login?force_url=1")


	def settings(setngs):
		session["USER_DATA"][0]["office"] = "On Dev"
		for ss in setngs:
			if(ss == "getsesh"):
				return redirect("/settings/getsesh")
			elif(ss == "chjob"):
				print(" * Changing job")
				session["USER_DATA"][0]["job"] = setngs['chjob']
			elif(ss == "chrcu"):
				print(" * Changing job")
				session["USER_DATA"][0]["rcu"] = setngs['chrcu'].replace("_"," ").upper()
		pass

	@app.route("/settings/getsesh",methods=["POST","GET"])
	def getsesh():
		return session["USER_DATA"][0]



	@app.route("/notification/web_safe_encode/<strs>",methods=["POST","GET"])
	def web_safe_encode(strs):
		return inbound.web_safe_encode(strs)

	@app.route("/notification/web_safe_decode/<strs>",methods=["POST","GET"])
	def web_safe_decode(strs):
		return inbound.web_safe_decode(strs)

	@app.route("/notification/get_notif",methods=["POST","GET"])
	def get_notif():
		return inbound.get_notif()

	@app.route("/notification/get_notif_unseen",methods=["POST","GET"])
	def get_notif_unseen():
		return inbound.get_notif_unseen()

	@app.route("/notification/set_notif_seen",methods=["POST","GET"])
	def set_notif_seen():
		notif_id = request.form['notif_id']
		return inbound.set_notif_seen(notif_id)


	# ========================================================================
	@app.route("/migrations/export_excel_mobile",methods=["POST","GET"])
	def export_excel_mobile():
		mobile_export_selection = request.form['form']
		print(" *  Getting Data ")
		return outbound.export_excel_mobile(mobile_export_selection)

	@app.route("/migrations/export_excel_excel",methods=["POST","GET"])
	def export_excel_excel():
		print(" *  Getting Data ")
		return outbound.export_excel_excel()

	@app.route("/excel_upload",methods=["POST","GET"])
	def excel_upload():
		from datetime import date, datetime
		today = str(datetime.today()).replace("-","_").replace(" ","_").replace(":","_").replace(".","_")
		uploader = request.form['uploader']
		excel_ = request.files
		UPLOAD_NAME = "NONE"
		for excel in excel_:
			f = excel_[excel]
			UPLOAD_NAME = uploader+"#"+today+"#"+secure_filename(f.filename)
			f.save(os.path.join(c.RECORDS+"/objects/spreadsheets/queued/",UPLOAD_NAME ))
		uploadstate = _excel.excel_popu_individual(UPLOAD_NAME)
		return uploadstate

	@app.route("/download_excel/<excel_file>",methods=["POST","GET"])
	def download_excel(excel_file):
		# excel_file = request.form['file']
		print(excel_file)
		def_name = excel_file.split("@@")[2]
		excel_file = excel_file.replace("@@","#")
		return send_file(c.RECORDS+"/objects/spreadsheets/migrated/"+excel_file, as_attachment=True,download_name=def_name)

	@app.route("/download_excel_from_notif/<excel_file>",methods=["POST","GET"])
	def download_excel_from_notif(excel_file):
		return send_file(c.RECORDS+"/objects/spreadsheets/exports/"+excel_file, as_attachment=True,download_name=excel_file)
	
	@app.route("/delete_excel/",methods=["POST","GET"])
	def delete_excel():
		excel_file = request.form['file']
		# print(excel_file)
		def_name = excel_file.split("@@")[2]
		excel_file = excel_file.replace("@@","#")

		shutil.move(
			c.RECORDS+"/objects/spreadsheets/migrated/{}".format(excel_file),
			c.RECORDS+"/objects/spreadsheets/deleted/{}".format(excel_file)
		)
		rapid_mysql.do("DELETE FROM `excel_import_form_a` WHERE `file_name`='{}' ;".format(excel_file))
		return jsonify({"status":"done"})
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
	@app.route("/feature_0/filter_list_farmers",methods=["POST","GET"])
	def feature_0_filter_list_farmers():
		return _main.feature_0_get_farmer_data_a1()


	@app.route("/feature_0/get_uploaded_excel",methods=["POST","GET"])
	def feature_0_get_uploaded_excel():
		_sql = ("SELECT `file_name` as `key`, count(file_name) as `total` FROM `excel_import_form_a` WHERE `user_id`={} GROUP by `file_name`;".format(session["USER_DATA"][0]['id']))
		upld_excel = rapid_mysql.select(_sql)
		return upld_excel

	@app.route("/feature_0/get_farmer_data_a1",methods=["POST","GET"])
	def feature_0_get_farmer_data_a1():
		sql_mobile = '''
			SELECT 
				`id` as 'db_id',
				`f_name`,
				`m_name`,
				`l_name`,
				`ext_name`,
				`farmer_sex`,
				`farmer_primary_crop`,
				`farmer_fo_name_rapid`,
				`addr_region`,
				`addr_prov`,
				`addr_city`,
				`farmer_dip_ref`
				-- `farmer_head_of_house`,
				-- `farmer_civil_status`,
				`SOURCE`
			FROM `form_a_farmer_profiles` {} ;'''.format(Filter.position_data_filter())

		sql_excel = '''
			SELECT 
				`id` as 'db_id',
				`frmer_prof_@_basic_Info_@_First_name` as `f_name`,
				`frmer_prof_@_basic_Info_@_Middle_name` as `m_name`,
				`frmer_prof_@_basic_Info_@_Last_name` as `l_name`,
				`frmer_prof_@_basic_Info_@_Extension_name` as `ext_name`,
				`frmer_prof_@_basic_Info_@_Sex` as `farmer_sex`,
				`frmer_prof_@_Farming_Basic_Info_@_primary_crop` as `farmer_primary_crop`,
				`frmer_prof_@_Farming_Basic_Info_@_Name_coop` as `farmer_fo_name_rapid`,
				`frmer_prof_@_frmer_addr_@_region` as `addr_region`,
				`frmer_prof_@_frmer_addr_@_province` as `addr_prov`,
				`frmer_prof_@_frmer_addr_@_city_municipality` as `addr_city`,
				`frmer_prof_@_Farming_Basic_Info_@_DIP_name` as `farmer_dip_ref`
				-- `frmer_prof_@_hh_Head_Info_@_is_head_og_household` as `farmer_head_of_house`,
				-- `frmer_prof_@_basic_Info_@_civil_status` as `farmer_civil_status`
			FROM `excel_import_form_a` {} ;'''.format(Filter.position_data_filter())
		all_farmer_small_data = rapid_mysql.select(sql_mobile) + rapid_mysql.select(sql_excel)
		random.shuffle(all_farmer_small_data)
		return all_farmer_small_data

	@app.route("/feature_0/dashboard_home_",methods=["POST","GET"])
	def dashboard_home_sql_driven_():
		return {
			"query_suffix" : "",
			"area_reg" : "",
			"all_farmer_count" : "",
			"all_sex_untag" : "",
			"all_sex_female" : "",
			"all_sex_male" : "",
			"is_ip_num" : "",
			"is_hh_head_num" : "",
			"with_dip": "",
			"with_fo": "",
			"enumerator": {"mobile":[],"excel":[]} ,
			"mobile_geotag": [] ,
			"ls_arr" : {
				"primary_crop" :{"main": [],"breakdown":{"excel": [] , "mobile" : []}},
				"ip_gr" :{"excel": [] , "mobile" : []},
				"fo" :{"excel": [] , "mobile" : []},
				"dip" :{"excel": [] , "mobile" : []},
			}
		}
	@app.route("/feature_0/dashboard_home",methods=["POST","GET"])
	def dashboard_home_sql_driven():
		FILTER_SUFFIX = Filter.position_data_filter()
		count_excel = rapid_mysql.select("SELECT COUNT(`frmer_prof_@_basic_Info_@_First_name`) as `ex` FROM excel_import_form_a {};".format(FILTER_SUFFIX))
		count_mobile = rapid_mysql.select("SELECT COUNT(`farmer_code`) as `mob` FROM form_a_farmer_profiles {};".format(FILTER_SUFFIX))
		all_farmer_count = count_excel[0]['ex'] + count_mobile[0]['mob'] 

		query = rapid_mysql.select
		dic = Filter.strct_clean
		dic_ = Filter.strct_dic

		mobile_sex = dic(query("SELECT `farmer_sex` as `key`, count(farmer_sex) as `total` FROM form_a_farmer_profiles  {} GROUP by farmer_sex;".format(FILTER_SUFFIX) ))
		mobile_ip = dic(query("SELECT `farmer_is_ip` as `key`, count(farmer_is_ip) as `total` FROM form_a_farmer_profiles  {} GROUP by farmer_is_ip;".format(FILTER_SUFFIX) ))
		mobile_head_hh = dic(query("SELECT `farmer_head_of_house` as `key`, count(farmer_head_of_house) as `total` FROM form_a_farmer_profiles  {} GROUP by farmer_head_of_house;".format(FILTER_SUFFIX) ))
		mobile_ip_grp = dic(query("SELECT `farmer_ip` as `key`, count(farmer_ip) as `total` FROM form_a_farmer_profiles  {} GROUP by farmer_ip;".format(FILTER_SUFFIX) ))
		mobile_fo = dic_(query("SELECT `farmer_fo_name_rapid` as `key`, count(farmer_fo_name_rapid) as `total` FROM form_a_farmer_profiles  {} GROUP by farmer_fo_name_rapid;".format(FILTER_SUFFIX) ))
		mobile_dip = dic_(query("SELECT `farmer_dip_ref` as `key`, count(farmer_dip_ref) as `total` FROM form_a_farmer_profiles  {} GROUP by farmer_dip_ref;".format(FILTER_SUFFIX) ))
		mobile_primary_c = dic(query("SELECT `farmer_primary_crop` as `key`, count(farmer_primary_crop) as `total` FROM form_a_farmer_profiles  {} GROUP by farmer_primary_crop;".format(FILTER_SUFFIX) ))

		mobile_geotag = query("SELECT `farmer_primary_crop`,`farmer_coords_long`,`farmer_coords_lat` FROM `form_a_farmer_profiles` {} AND `farmer_coords_lat` != '' AND `farmer_coords_lat` != ' ';".format(FILTER_SUFFIX))

		excl_sex = dic(query("SELECT `frmer_prof_@_basic_Info_@_Sex` as `key`, count(`frmer_prof_@_basic_Info_@_Sex`) as `total` FROM `excel_import_form_a`  {} GROUP by `frmer_prof_@_basic_Info_@_Sex`;".format(FILTER_SUFFIX) ))
		excl_ip = dic(query("SELECT `frmer_prof_@_Farming_Basic_Info_@_farmer_ip` as `key`, count(`frmer_prof_@_Farming_Basic_Info_@_farmer_ip`) as `total` FROM `excel_import_form_a`  {} GROUP by `frmer_prof_@_Farming_Basic_Info_@_farmer_ip`;".format(FILTER_SUFFIX) ))
		excl_head_hh = dic(query("SELECT `frmer_prof_@_hh_Head_Info_@_is_head_og_household` as `key`, count(`frmer_prof_@_hh_Head_Info_@_is_head_og_household`) as `total` FROM `excel_import_form_a`  {} GROUP by `frmer_prof_@_hh_Head_Info_@_is_head_og_household`;".format(FILTER_SUFFIX) ))
		excl_ip_grp = dic(query("SELECT `frmer_prof_@_Farming_Basic_Info_@_farmer_ip` as `key`, count(`frmer_prof_@_Farming_Basic_Info_@_farmer_ip`) as `total` FROM `excel_import_form_a`  {} GROUP by `frmer_prof_@_Farming_Basic_Info_@_farmer_ip`;".format(FILTER_SUFFIX) ))
		excl_fo = dic_(query("SELECT `frmer_prof_@_Farming_Basic_Info_@_Name_coop` as `key`, count(`frmer_prof_@_Farming_Basic_Info_@_Name_coop`) as `total` FROM `excel_import_form_a`  {} GROUP by `frmer_prof_@_Farming_Basic_Info_@_Name_coop`;".format(FILTER_SUFFIX) ))
		excl_dip = dic_(query("SELECT `frmer_prof_@_Farming_Basic_Info_@_DIP_name` as `key`, count(`frmer_prof_@_Farming_Basic_Info_@_DIP_name`) as `total` FROM `excel_import_form_a`  {} GROUP by `frmer_prof_@_Farming_Basic_Info_@_DIP_name`;".format(FILTER_SUFFIX) ))
		excl_primary_c = dic(query("SELECT `frmer_prof_@_Farming_Basic_Info_@_primary_crop` as `key`, count(`frmer_prof_@_Farming_Basic_Info_@_primary_crop`) as `total` FROM `excel_import_form_a`  {} GROUP by `frmer_prof_@_Farming_Basic_Info_@_primary_crop`;".format(FILTER_SUFFIX) ))
		

		enumerator_mobile = (query(('''
				SELECT 
					users.id as `id`,
					users.name as `key`,
					count(form_a_farmer_profiles.USER_ID) as `total`
				FROM
					form_a_farmer_profiles
				INNER JOIN users ON form_a_farmer_profiles.USER_ID = users.id
				{}
				GROUP by users.name
				ORDER BY count(form_a_farmer_profiles.USER_ID) DESC;
		''').format(FILTER_SUFFIX) ))

		enumerator_excel = (query(('''
				SELECT 
					users.id as `id`,
					users.name as `key`,
					count(excel_import_form_a.user_id) as `total`
				FROM
					excel_import_form_a
				JOIN users ON excel_import_form_a.user_id = users.id
				{}
				GROUP by users.name
				ORDER BY count(excel_import_form_a.user_id) DESC;
		''').format(FILTER_SUFFIX) ))


		if('untagged' not in mobile_dip):mobile_dip['untagged'] = 0
		if('untagged' not in mobile_fo):mobile_fo['untagged'] = 0
		if("" not in mobile_dip):mobile_dip[""] = 0
		if("" not in mobile_fo):mobile_fo[""] = 0

		if('untagged' not in excl_dip):excl_dip['untagged'] = 0
		if('untagged' not in excl_fo):excl_fo['untagged'] = 0
		if("" not in excl_dip):excl_dip[""] = 0
		if("" not in excl_fo):excl_fo[""] = 0

		with_dip = all_farmer_count - (mobile_dip['untagged']+excl_dip[""])
		with_fo = all_farmer_count - (mobile_fo['untagged']+excl_fo[""])

		primary_crop = Populate.primary_crop(mobile_primary_c,excl_primary_c)
		data = {
			"query_suffix" : str(FILTER_SUFFIX),
			"area_reg" : session["USER_DATA"][0]["office"],
			"all_farmer_count" : all_farmer_count,
			"all_sex_untag" : all_farmer_count + (mobile_sex['male'] + mobile_sex['female'] + excl_sex['male'] + excl_sex['female'] ),
			"all_sex_female" : mobile_sex['female'] + excl_sex['female'],
			"all_sex_male" : mobile_sex['male'] + excl_sex['male'],
			"is_ip_num" : all_farmer_count - (mobile_ip['false']+excl_ip[""]),
			"is_hh_head_num" : all_farmer_count - (mobile_head_hh['false']+excl_head_hh[""]),
			"with_dip": with_dip,
			"with_fo": with_fo,
			"enumerator": {"mobile":enumerator_mobile,"excel":enumerator_excel} ,
			"mobile_geotag": mobile_geotag ,
			"sex" : {"mobile":mobile_sex,"excel":excl_sex},
			"ls_arr" : {
				"primary_crop" :{"main": primary_crop,"breakdown":{"excel": excl_primary_c , "mobile" : mobile_primary_c}},
				"ip_gr" :{"excel": excl_ip_grp , "mobile" : mobile_ip_grp},
				"fo" :{"excel": excl_fo , "mobile" : mobile_fo},
				"dip" :{"excel": excl_dip , "mobile" : mobile_dip},
			}
		}
		return data
		# return [all_mob_female[0]['f'],all_mob_male[0]['m']]

class Populate:
	def primary_crop(mobi,excl):
		new_comd = {}
		comodities = rapid_mysql.select("SELECT `name` as `key` FROM `value_chain_comodities`",False)
		for count in range(len(comodities)):
			cmdty_sndrd = comodities[count][0]
			if(cmdty_sndrd not in new_comd):new_comd[cmdty_sndrd] = 0
			if(cmdty_sndrd not in mobi):mobi[cmdty_sndrd] = 0
			if(cmdty_sndrd not in excl):excl[cmdty_sndrd] = 0
			new_comd[cmdty_sndrd] = new_comd[cmdty_sndrd] + mobi[cmdty_sndrd] + excl[cmdty_sndrd]
		print(sorted(new_comd))
		return sorted(new_comd.items(), key=lambda x:x[1], reverse=True)


class Filter:
	def position_data_filter():
		_filter = "WHERE 1 "
		JOB = session["USER_DATA"][0]["job"].lower()

		if(JOB in "admin" or JOB in "super admin"):
			session["USER_DATA"][0]["office"] = "NPCO"
			_filter = "WHERE 1 "
		else:
			session["USER_DATA"][0]["office"] = "Regional ({})".format(session["USER_DATA"][0]["rcu"])
			_filter = "WHERE  USER_ID in ( SELECT id from users WHERE rcu='{}' )".format(session["USER_DATA"][0]["rcu"])

		return _filter

	def strct_dic(dict_):
		new_dict_ = {};
		for data in dict_:new_dict_[data['key']] = data['total']
		return json.loads(json.dumps(new_dict_))

	def strct_clean(dict_):
		new_dict_ = {};
		for data in dict_:new_dict_[data['key']] = data['total']
		return Filter.clean(json.loads(json.dumps(new_dict_)))

	def clean(dict_):
		new_dict_ = {};
		for key in dict_:
			KEY = key.lower().replace(" ","").replace(".","").replace("/","").replace("\\","").replace("-","").replace("*","").replace(",","").replace("(","").replace(")","").replace("&","")
			if(KEY not in new_dict_):
				new_dict_[KEY] = 0
			new_dict_[KEY] = new_dict_[KEY]+dict_[key]
			
		return json.loads(json.dumps(new_dict_))