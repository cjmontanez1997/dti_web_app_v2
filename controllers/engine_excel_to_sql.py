import os, json, random, shutil
from tqdm import tqdm
import Configurations as c
from modules.Connections import mysql,sqlite
from controllers.value_cleaner import file_handler as cleaner

import base64
import sys
import pandas as pd
from tqdm import tqdm
import warnings
import csv
import xlrd ####### IMPORTANT pip install xlrd==1.2.0

warnings.filterwarnings('ignore')

# rapid_sqlite = sqlite(c.SQLITE_DB)
rapid_mysql = mysql(*c.DB_CRED)
# rapid_mysql.err_page = 0

class form_excel_a_handler:
	def __init__(self,args):
		super(form_excel_a_handler, self).__init__()
		self.args = args
		self.loads_ = None
		self.record_counter = 0

	def get_all_uploaded_excel_data_f_a(self):
		return self.excel_popu_a()

	def excel_popu_a(self):
		msg = "Unfinished"
		status = "Unfinished"
		self.record_counter = 0
		# dir_path = c.RECORDS+"/objects/spreadsheets/_temp_/"
		dir_path = c.RECORDS+"/objects/spreadsheets/queued/"
		FROM_EXCEL_RPOFILES = {}
		# FROM_EXCEL_RPOFILES = []
		# loads_ = tqdm(os.listdir(dir_path))
		counter = 0
		# for path in loads_:os.listdir(dir_path)
		for path in os.listdir(dir_path):
			PATH__ = os.path.join(dir_path, path)
			if os.path.isfile(PATH__):
				# if (("._DELETED_FILE_" not in str(path)) or ("~$" not in str(path))):	
				fn_ = path.split(".")[len(path.split("."))-1]
				if(fn_ not in "._DELETED_FILE_"):
					file_name =  PATH__ 
					sheet =  "VC FORM A" 
					print("\n= Scanning [{}]".format(path))
					try:
						resp = self.push_mysql(self.readRows(file_name, sheet),path)
						if(resp["err"]):
							msg = "Error in Moving to Database"
							status = "failed"
							return resp["msg"]
							# return resp["msg"]["sql"]
						else:
							self.move_to_done_files(path)
							FROM_EXCEL_RPOFILES[resp["data"]["file"]] = resp["data"]["count"]
							msg = "Moved to Database"
							status = "success"
						counter = counter + 1
					except Exception as e:
						if("No sheet named <'VC FORM A'>" in str(e)):
							print("  --- ERROR in XLRD Parser (ignoring file [{}]) || {}".format(path,e))
							self.move_to_failed_files(path)
							msg = "No <'VC FORM A'> Found"
							status = "failed"
						elif("Unsupported format, or corrupt file" in str(e)):
							print("  --- ERROR in XLRD Parser (ignoring file [{}]) || {}".format(path,e))
							self.move_to_failed_files(path)
							msg = "Corrupt File"
							status = "failed"
						else:
							raise e
			# if(counter >= 3):
			# 	break
		return {"status":status,"msg":msg,"success_files":FROM_EXCEL_RPOFILES}

	def excel_popu_individual(self,_NAME_):
		msg = "Unfinished"
		status = "Unfinished"
		self.record_counter = 0
		# dir_path = c.RECORDS+"/objects/spreadsheets/_temp_/"
		dir_path = c.RECORDS+"/objects/spreadsheets/queued/"
		FROM_EXCEL_RPOFILES = {}
		# FROM_EXCEL_RPOFILES = []
		# loads_ = tqdm(os.listdir(dir_path))
		counter = 0
		# for path in loads_:os.listdir(dir_path)
		PATH__ = os.path.join(dir_path, _NAME_)
		if os.path.isfile(PATH__):
			# if (("._DELETED_FILE_" not in str(path)) or ("~$" not in str(path))):	
			file_name =  PATH__ 
			sheet =  "VC FORM A" 
			print("\n= Scanning [{}]".format(_NAME_))
			try:
				resp = self.push_mysql(self.readRows(file_name, sheet),_NAME_)
				if(resp["err"]):
					msg = "Error in Moving to Database"
					status = "failed"
					return resp["msg"]
					# return resp["msg"]["sql"]
				else:
					self.move_to_done_files(_NAME_)
					FROM_EXCEL_RPOFILES[resp["data"]["file"]] = resp["data"]["count"]
					msg = "Moved to Database"
					status = "success"
				counter = counter + 1
			except Exception as e:
				if("No sheet named <'VC FORM A'>" in str(e)):
					print("  --- ERROR in XLRD Parser (ignoring file [{}]) || {}".format(_NAME_,e))
					self.move_to_failed_files(_NAME_)
					msg = "No <'VC FORM A'> Found"
					status = "failed"
				elif("Unsupported format, or corrupt file" in str(e)):
					print("  --- ERROR in XLRD Parser (ignoring file [{}]) || {}".format(_NAME_,e))
					self.move_to_failed_files(_NAME_)
					msg = "Corrupt File"
					status = "failed"
				else:
					msg = "Corrupt File"
					status = "failed"
					println(e)
			# if(counter >= 3):
			# 	break
		print(" * Done excel process")
		return {"status":status,"msg":msg,"success_files":FROM_EXCEL_RPOFILES}

# /////////////////// 94#2023-01-16#Profile_AGUSAN_DEL_SUR1.xlsx
	def push_mysql(self, rows, user_id):
		excel_a_heads = get_all_uploaded_excel_data_heads()
		err = False
		RESP = "None"
		CONN = rapid_mysql.db_ready()
		data_row_counter = 0
		ALL_ROW_LENGTH = range(len(rows))
		EXIT = False
		loads_ = tqdm(ALL_ROW_LENGTH)
		ret_data = {"file":user_id,"count":data_row_counter}
		for row_num in loads_:
			counter = 0
			# print(rows)
			fields = "" ; vals = ""
			if(row_num==0):continue;
			for val__ in rows[row_num]:
				if(counter==1):
					# print("{} :: {}".format(excel_a_heads[counter],val__))
					if(val__ == "" or val__ == " " or val__ == None or val__ == "NaN"):
						EXIT = True
				__VAL = str(val__).replace("\\","").replace("'","").replace('''"''',"")
				fields = fields + ",`"+ excel_a_heads[counter] +"`"
				vals = vals + ',"'+ __VAL +'"'
				counter = counter + 1
			if(EXIT == False):
				sql = ('''INSERT INTO `excel_import_form_a` (`user_id`,`file_name`,{}) VALUES('{}','{}',{}) ;'''.format(fields[1:],user_id.split("#")[0],user_id,vals[1:]))
				resp = rapid_mysql.do_(sql,CONN)
				loads_.desc = "   -FileData[{}] Total Data[{}] file[{}]".format(data_row_counter+1,self.record_counter,user_id)
				self.record_counter = self.record_counter + 1
				data_row_counter = data_row_counter + 1
				try:
					if("response" in resp):
						err = True;RESP = resp;break
				except Exception as e:
					RESP = {"file":user_id,"count":data_row_counter}
					pass
			else:
				break
		CONN.commit()
		return {"err":err,"msg":RESP,"data":ret_data}

	def readRows(self, file, s_index):
		wb = xlrd.open_workbook(file,encoding_override='utf-8')
		# wb = xlrd.open_workbook(file)
		sheet = wb.sheet_by_name(s_index)
		data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
		counter = 0
		return data[3:]

	def move_to_done_files(self,FILENAME):
		# shutil.copy(
		shutil.move(
			c.RECORDS+"/objects/spreadsheets/queued/{}".format(FILENAME),
			# c.RECORDS+"/objects/spreadsheets/_temp_/{}".format(FILENAME),
			c.RECORDS+"/objects/spreadsheets/migrated/{}".format(FILENAME)
		)
		return "Done"

	def move_to_failed_files(self,FILENAME):
		# shutil.copy(
		shutil.move(
			c.RECORDS+"/objects/spreadsheets/queued/{}".format(FILENAME),
			# c.RECORDS+"/objects/spreadsheets/_temp_/{}".format(FILENAME),
			c.RECORDS+"/objects/spreadsheets/failed/{}".format(FILENAME)
		)
		return "Done"

# ======================

def get_all_uploaded_excel_data_heads():
	excel_f_a_heads = c.RECORDS+"/settings/db_sql_excel_form_a.head"
	reader = open(excel_f_a_heads,"r");excel_f_a_heads = json.loads(reader.read());reader.close()
	return excel_f_a_heads

	# ============================================================