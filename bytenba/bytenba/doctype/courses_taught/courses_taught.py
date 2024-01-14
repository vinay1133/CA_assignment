# Copyright (c) 2023, byte_team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import bytenba.custom_utilities as uf
import re
import bytenba.form_validation as validation

Doctype = 'Courses taught'
pattern_for_wtg = r'\((\s*(?:\d+\.\d+|\d+)\s*)\)'

class Coursestaught(Document):
	
	def autoname(self):
		self.name = f'AI2_{self.owner}_{self.academic_year}_{self.semester}'

	def before_save(self):
		# no. of rows
		count=0 
		"""Average Target Obtained"""
		target_obt=0
		for item in self.course__lab_name:
			target_obt += item.no_sessions/item.number_of_sessions_as_per_syllabus*100
			count += 1
		avg_target_obt = target_obt/count
		self.average_target_obtained = avg_target_obt

		"""Average Completion of Syllabus"""
		comp_of_syllabus=0
		for item in self.course__lab_name:
			comp_of_syllabus += item.completion_of_syllabus
		avg_comp_of_syllabus = comp_of_syllabus/count
		self.average_syllabus_completed = avg_comp_of_syllabus

		"""Marks Obtained"""
		if avg_target_obt>=100:
			self.marks_obtained = 300
		elif avg_target_obt>90 and avg_target_obt<=99:
			self.marks_obtained = 225
		elif avg_target_obt>80 and avg_target_obt<=89:
			self.marks_obtained = 150
		elif avg_target_obt>70 and avg_target_obt<=79:
			self.marks_obtained = 100
		else:
			self.marks_obtained = 0
		
		"""Self-Appraisal Score"""
		self.self_appraisal_score = self.marks_obtained*self.average_syllabus_completed/100
	
	def validate(self):
		"""Validation for academic year"""
		validation.standard_validation(self)

