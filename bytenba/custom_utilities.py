import frappe
import re

def validateAY(academic_yr_str):
	pattern_for_ay = re.compile(r'^\d{4}-\d{4}$')
	if re.match(pattern_for_ay, academic_yr_str):
		years = academic_yr_str.split("-")
		if int(years[1]) != int(years[0]) + 1:
				frappe.throw("Academic year entered incorrectly")
	else:
		frappe.throw("Academic year must be of the form like 2022-2023")
			