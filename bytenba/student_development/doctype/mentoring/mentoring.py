import frappe
from frappe.model.document import Document
import bytenba.custom_utilities as uf
import re

Doctype = 'Mentoring'
pattern_for_wtg = r'\((\s*(?:\d+\.\d+|\d+)\s*)\)'

class Mentoring(Document):
	
	"""method to autoname your document"""
	def autoname(self):
		self.name = f'SD5_{self.professor}_{self.academic_year}_{self.semester}'
	
	def before_save(self):
		self.self_appraisal_score = compute_marks(self)

	def validate(self):
		uf.validateAY(self.academic_year)
		existing_record = frappe.db.exists(Doctype, {'name': self.name})
		if existing_record and existing_record != self.name:
			frappe.throw('There already exists such a record in the database')  


def compute_marks(self):
	
	match = re.search(pattern_for_wtg, self.number_of_meetings)
	if match:
		val1 = float(match.group(1).strip())
	else:
		frappe.throw('Error Fetching Field Weightages')

	match = re.search(pattern_for_wtg, self.awards_won)
	if match:
		val2 = float(match.group(1).strip())
	else:
		frappe.throw('Error Fetching Field Weightages')

	match = re.search(pattern_for_wtg, self.prof_pers_dev)
	if match:
		val3 = float(match.group(1).strip())
	else:
		frappe.throw('Error Fetching Field Weightages')

	match = re.search(pattern_for_wtg, self.fys_feedback)
	if match:
		val4 = float(match.group(1).strip())
	else:
		frappe.throw('Error Fetching Field Weightages')
		
	product_of_wts = val1*val2*val3*val4
	
	return product_of_wts*200