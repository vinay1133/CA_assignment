import frappe
import re

def validateAY(academic_yr_str):
	res_dict = {"valid": True, "error_msg": ''}
	pattern_for_ay = re.compile(r'^\d{4}-\d{4}$')
	if re.match(pattern_for_ay, academic_yr_str):
		years = academic_yr_str.split("-")
		if int(years[1]) != int(years[0]) + 1:
				res_dict['valid'] = False
				res_dict['error_msg'] = "Academic year entered incorrectly"
	else:
		res_dict['valid'] = False
		res_dict['error_msg'] = "Academic year must be of the form like 2022-2023"
	
	return res_dict
			