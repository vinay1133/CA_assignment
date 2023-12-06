import frappe
from frappe.model.document import Document
import bytenba.custom_utilities as uf
import re

Doctype = 'Institute Binding Activities'
pattern_for_wtg = r'\((\s*(?:\d+\.\d+|\d+)\s*)\)'


class InstituteBindingActivities(Document):
	
	"""method to autoname your document"""
	def autoname(self):
		self.name = f'AB9_{self.professor}_{self.academic_year}_{self.semester}'
	
	def before_save(self):
	
		match = re.search(pattern_for_wtg, self.c1)
		if match:
			val1 = float(match.group(1).strip())
		else:
			frappe.throw('Error Fetching Values From Field 1')
		
		self.m1 = val1*75
		self.m2 = self.c2*25
		self.m3 = self.c3*25
		self.m4 = self.c4*25
		self.m5 = self.c5*10
		self.m6 = self.c6*50
		self.m7 = self.c7*5

		sum_of_marks_obtained = self.m1 + self.m2 + self.m3 + self.m4 + self.m5 + self.m6 +self.m7

		if sum_of_marks_obtained > 200:
			sum_of_marks_obtained = 200
		
		self.self_appraisal_score = sum_of_marks_obtained


	def validate(self):
		uf.validateAY(self.academic_year)
		existing_record = frappe.db.exists(Doctype, {'name': self.name})
		if existing_record and existing_record != self.name:
			frappe.throw('There already exists such a record in the database')

	