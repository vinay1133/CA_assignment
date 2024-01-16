# Copyright (c) 2023, byte_team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import re
import bytenba.form_validation as validation

Doctype = 'BSA guest lecture'
pattern = re.compile(r'^\d{4}-\d{4}$')
pattern_for_wtg = r'\((\s*(?:\d+\.\d+|\d+)\s*)\)'

class BSAguestlecture(Document):

	"""method to autoname your document"""
	def autoname(self):
		self.name = f'AI3a_{self.owner}_{self.academic_year}_{self.semester}'
	
	def before_save(self):
		self.self_appraisal_score = round(compute_marks(self))

	def validate(self):
		validation.standard_validation(self)


def compute_marks(self):

	counter = 0
	pas = []

	for item in self.criteria_table:
		if counter > 1:
			frappe.throw('Can only have two entries in the table')

		else:
			counter +=1

			if item.number_of_attendees > item.total_students:
				frappe.throw(f'Number of attendees cannot be greater than the number of students enrolled in row {counter}')

			if (item.number_of_attendees or item.total_students or item.feedback_received) < 0:
				frappe.throw('No field in this form can have a negative value')
			
			match = re.search(pattern_for_wtg, item.quality_of_speaker)
			if match:
				val1 = float(match.group(1).strip())
			else:
				frappe.throw('Error Fetching Field Weightages')
			
			match = re.search(pattern_for_wtg, item.mapping)
			if match:
				val2 = float(match.group(1).strip())
			else:
				frappe.throw('Error Fetching Field Weightages')			

			sub_val1 = item.feedback_received
			if sub_val1 >= 2.5:
				val3 = item.number_of_attendees // item.total_students
			else:
				val3 = 0
			
			item.quality_relevance = val3
			pow = val1*val2*val3*75

			item.marks_obtained = pow

			pas.append(round(pow))
	
	return sum(pas)