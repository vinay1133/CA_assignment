# Copyright (c) 2023, byte_team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import re

pattern = re.compile(r'^\d{4}-\d{4}$')

class Coursestaught(Document):
	def before_save(self):
		count=0 # no. of rows

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
	
	"""method to autoname your document"""
	def autoname(self):
		base_name = f'AI2_{self.academic_year}_{self.professor}'
		data = renameDoc(base_name, self.academic_year)
		if data['name_value']:
			self.name = data['name_value']
		else:
			frappe.throw("Failed to generate a unique name.")
	
	def validate(self):
		"""Validation for academic year"""
		academic_yr_str = self.academic_year
		if not re.match(pattern, academic_yr_str):
			frappe.throw('Academic year must be of the form like 2022-2023')
		else:
			yr_end_1 = int(academic_yr_str[2:4])
			yr_end_2 = int(academic_yr_str[7:9])
			if yr_end_2 != yr_end_1 + 1:
				frappe.throw('Academic Date entered improperly')

def renameDoc(base_name, academic_year):
	dict = {'name_value': None}
	filters = {
		"name": ["like", base_name + "%"]
	}
	field = 'name'
	similar_docs = frappe.get_list("Courses taught", filters= filters, pluck = field)
	dict['name_value'] = base_name
	return dict

