import frappe
from frappe.model.document import Document
import bytenba.custom_utilities as uf
import re

Doctype = 'Patents-designs-copyrights-technologies developed'
pattern_for_wtg = r'\((\s*(?:\d+\.\d+|\d+)\s*)\)'

class Patentsdesignscopyrightstechnologiesdeveloped(Document):
	
	"""method to autoname your document"""
	def autoname(self):
		self.name = f'RB4_{self.professor}_{self.academic_year}_{self.semester}'
	
	def before_save(self):
		self.self_appraisal_score = compute_marks(self)

	def validate(self):
		uf.validateAY(self.academic_year)
		existing_record = frappe.db.exists(Doctype, {'name': self.name})
		if existing_record and existing_record != self.name:
			frappe.throw('There already exists such a record in the database')  


def compute_marks(self):

	match = re.search(pattern_for_wtg, self.status_of_the_patent)
	if match:
		value = float(match.group(1).strip())*200
	else:
		frappe.throw('Error Fetching Field Weightages')
	
	return value
			