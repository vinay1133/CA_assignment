import frappe
from frappe.model.document import Document
import bytenba.custom_utilities as uf
import re
import math as m

Doctype = 'Expert for reputed committee'
pattern_for_wtg = r'\((\s*(?:\d+\.\d+|\d+)\s*)\)'

class Expertforreputedcommittee(Document):
	
	"""method to autoname your document"""
	def autoname(self):
		self.name = f'CB2_{self.professor}_{self.academic_year}_{self.semester}'
	
	def before_save(self):
		self.self_appraisal_score = compute_marks(self)

	def validate(self):
		uf.validateAY(self.academic_year)
		existing_record = frappe.db.exists(Doctype, {'name': self.name})
		if existing_record and existing_record != self.name:
			frappe.throw('There already exists such a record in the database')

		if self.num1 > 1:
			frappe.throw('Violation in first criterion: PA committe has set max number of appointments to not exceed 1')
		if self.num2 > 1:
			frappe.throw('Violation in second criterion: PA committe has set max number of appointments to not exceed 1')
		if self.num3 > 1:
			frappe.throw('Violation in third criterion: PA committe has set max number of appointments to not exceed 1')
		



def compute_marks(self):

	self.m1 = self.num1*50
	self.m2 = self.num2*40
	self.m3 = self.num3*30

	marks_obtained = self.m1 + self.m2 + self.m3
	
	return marks_obtained
