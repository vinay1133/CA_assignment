# Copyright (c) 2023, byte_team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import bytenba.custom_utilities as uf
import re

Doctype = 'Certification for courses allotted'
pattern_for_wtg = r'\((\s*(?:\d+\.\d+|\d+)\s*)\)'

class Certificationforcoursesallotted(Document):
	
	"""method to autoname your document"""
	def autoname(self):
		self.name = f'AI1_{self.professor}_{self.academic_year}_{self.semester}'
	
	def before_save(self):
		self_appraisal_score = compute_marks(self)
		self.self_appraisal_score = self_appraisal_score

	def validate(self):
		uf.validateAY(self.academic_year)
		existing_record = frappe.db.exists(Doctype, {'name': self.name})
		if existing_record and existing_record != self.name:
			frappe.throw('There already exists such a record in the database')  


def compute_marks(self):
	
	match = re.search(pattern_for_wtg, self.platform_type)
	if match:
		val1 = float(match.group(1).strip())
	else:
		frappe.throw('Error Fetching Field Weightages')

	match = re.search(pattern_for_wtg, self.assessment_outcome)
	if match:
		val2 = float(match.group(1).strip())
	else:
		frappe.throw('Error Fetching Field Weightages')

	match = re.search(pattern_for_wtg, self.date_of_cerftification)
	if match:
		val3 = float(match.group(1).strip())
	else:
		frappe.throw('Error Fetching Field Weightages')

	match = re.search(pattern_for_wtg, self.number_of_hours)
	if match:
		val4 = float(match.group(1).strip())
	else:
		frappe.throw('Error Fetching Field Weightages')
		
	product_of_wts = val1*val2*val3*val4
	return product_of_wts*100