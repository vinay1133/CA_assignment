# Copyright (c) 2023, byte_team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import bytenba.custom_utilities as uf
pattern_for_wtg = r'\((\s*(?:\d+\.\d+|\d+)\s*)\)'

Doctype = "Laboratory Work Or Case Studies"

class LaboratoryWorkOrCaseStudies(Document):

	"""method to autoname your document"""
	def autoname(self):
		self.name = f'AI4_{self.professor}_{self.academic_year}_{self.semester}'
	
	def before_save(self):
		self_appraisal_score = compute_marks(self)
		self.self_appraisal_score = self_appraisal_score

	def validate(self):
		uf.validateAY(self.academic_year)
		existing_record = frappe.db.exists(Doctype, {'name': self.name})
		if existing_record and existing_record != self.name:
			frappe.throw('There already exists such a record in the database')  


def compute_marks(self):
	pass