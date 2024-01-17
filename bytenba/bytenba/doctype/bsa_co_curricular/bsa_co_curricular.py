# Copyright (c) 2023, byte_team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import bytenba.form_validation as validation
import re

Doctype = 'BSA-Co-curricular'
pattern_for_wtg = r'\((\s*(?:\d+\.\d+|\d+)\s*)\)'

class BSACocurricular(Document):
	def autoname(self):
		self.name = f'AI3c_{self.owner}_{self.academic_year}_{self.semester}'

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

			if item.number_of_attendees > item.total_number_of_students_of_roll_list:
				frappe.throw(f'Number of attendees cannot be greater than the number of students enrolled in row {counter}')
			
			match = re.search(pattern_for_wtg, item.type_of_event)
			if match:
				val1 = float(match.group(1).strip())
			else:
				frappe.throw('Error Fetching Field Weightages')
			
			match = re.search(pattern_for_wtg, item.awards_received)
			if match:
				val2 = float(match.group(1).strip())
			else:
				frappe.throw('Error Fetching Field Weightages')			
			
			match = re.search(pattern_for_wtg, item.mapping)
			if match:
				val3 = float(match.group(1).strip())
			else:
				frappe.throw('Error Fetching Field Weightages')

			
			if item.feedback_received>= 2.5:
				val4 = item.number_of_attendees / item.total_number_of_students_of_roll_list
			else:
				val4 = 0
			
			item.feedback_score = val4
			pow = val1*val2*val3*val4*75

			item.marks_obtained = pow

			pas.append(round(pow))
	
	return sum(pas)	