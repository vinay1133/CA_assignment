import frappe
from frappe.model.document import Document
import bytenba.custom_utilities as uf
import re

Doctype = 'Institute Level Academic Activities Organized'
pattern_for_wtg = r'\((\s*(?:\d+\.\d+|\d+)\s*)\)'

class InstituteLevelAcademicActivitiesOrganized(Document):
	
	"""method to autoname your document"""
	def autoname(self):
		self.name = f'AB1_{self.professor}_{self.academic_year}_{self.semester}'
	
	def before_save(self):
		self.self_appraisal_score = round(compute_marks(self))

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

			match = re.search(pattern_for_wtg, item.quality_of_conduct_of_activity)
			if match:
				val1 = float(match.group(1).strip())
			else:
				frappe.throw('Error Fetching Field Weightages')
			
			match = re.search(pattern_for_wtg, item.associations_in_the_activity)
			if match:
				val2 = float(match.group(1).strip())
			else:
				frappe.throw('Error Fetching Field Weightages')			

			match = re.search(pattern_for_wtg, item.paper_selection_ratio_after_review)
			if match:
				val3 = float(match.group(1).strip())
			else:
				frappe.throw('Error Fetching Field Weightages')

			match = re.search(pattern_for_wtg, item.designation)
			if match:
				val4 = float(match.group(1).strip())
			else:
				frappe.throw('Error Fetching Field Weightages')			
			
			pow = val1*val2*val3*val4*100
			pas.append(pow)
	
	return pas[0] + pas[1]