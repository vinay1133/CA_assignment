# Copyright (c) 2023, byte_team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import re

Doctype = 'Contribution In Learning Resources Development'
pattern_for_wtg = r'\((\s*(?:\d+\.\d+|\d+)\s*)\)'
pattern_for_ay = re.compile(r'^\d{4}-\d{4}$')


class Contributioninlearningresourcesdevelopment(Document):	

	def autoname(self):
		self.name = f'AI8Engg_{self.academic_year}_{self.semester}_{self.professor}'

	def before_save(self):
		self_appraisal_score = compute_marks(self)
		self.self_appraisal_score = self_appraisal_score

	def validate(self):
		#validate academic year str
		academic_yr_str = self.academic_year
		if re.match(pattern_for_ay, academic_yr_str):
			years = academic_yr_str.split("-")
			if int(years[1]) != int(years[0]) + 1:
				frappe.throw('Academic year entered incorrectly')
		else:
			frappe.throw('Academic year must be of the form like 2022-2023')

		#validate if same record exists in database
		existing_record = frappe.db.exists('BE Projects', {'name': self.name})
		#check if it is not the document currently begin worked upon
		if existing_record and existing_record != self.name:
			frappe.throw('There already exists such a record in the database')
			

def compute_marks(self):

	'''criteria 1'''
	match = re.search(pattern_for_wtg, self.criteria_1)
	if match:
		val1 = float(match.group(1).strip())
	else:
		frappe.throw('Error Fetching Field Weightages')

	'''criteria 1'''
	match = re.search(pattern_for_wtg, self.criteria_2)
	if match:
		val2 = float(match.group(1).strip())
	else:
		frappe.throw('Error Fetching Field Weightages')

	'''criteria 1'''
	match = re.search(pattern_for_wtg, self.criteria_3)
	if match:
		val3 = float(match.group(1).strip())
	else:
		frappe.throw('Error Fetching Field Weightages')

	'''criteria 1'''
	match = re.search(pattern_for_wtg, self.criteria_4)
	if match:
		val4 = float(match.group(1).strip())
	else:
		frappe.throw('Error Fetching Field Weightages')

	product_of_wts = val1*val2*val3*val4*val5
	return product_of_wts

