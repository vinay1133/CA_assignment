import frappe
from frappe.model.document import Document
import bytenba.custom_utilities as uf
import re

Doctype = 'Special Accolades'
pattern_for_wtg = r'\((\s*(?:\d+\.\d+|\d+)\s*)\)'

class SpecialAccolades(Document):
	
	"""method to autoname your document"""
	def autoname(self):
		self.name = f'RB6_{self.professor}_{self.academic_year}_{self.semester}'
	
	def before_save(self):
		self.self_appraisal_score = compute_marks(self)

	def validate(self):
		uf.validateAY(self.academic_year)
		existing_record = frappe.db.exists(Doctype, {'name': self.name})
		if existing_record and existing_record != self.name:
			frappe.throw('There already exists such a record in the database')  


def compute_marks(self):
	
	counter = 0
	pas = []

	for item in self.criteria_table:
		if counter > 1:
			frappe.throw('Can only have two entries in the table')

		else:
			counter +=1

			match = re.search(pattern_for_wtg, item.col1)
			if match:
				val1 = float(match.group(1).strip())
			else:
				frappe.throw('Error Fetching Field Weightages')
			
			marks_obtained = round(val1*item.col2*50 , 2)
			item.col3 = marks_obtained

			pas.append(marks_obtained)
	
	return round(sum(pas))
