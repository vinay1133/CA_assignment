# Copyright (c) 2023, byte_team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import re

pattern = re.compile(r'^\d{4}-\d{4}$')

class Course_Laboutcomeattainment(Document):
	def before_save(self):
		total = 0
		count = 0
		for item in self.enter_courselab_name:
			total += item.attainment
			count+=1
		self.average_attainment = (total)/count
		if self.average_attainment>2 and self.average_attainment<=3:
			self.self_appraisal_score=200
		elif self.average_attainment>1 and self.average_attainment<=2:
			self.self_appraisal_score=150
		elif self.average_attainment>0 and self.average_attainment<=1:
			self.self_appraisal_score=100
		else:
			self.self_appraisal_score=0
	
	"""method to autoname your document"""
	def autoname(self):
		base_name = f'AI5_{self.academic_year}_{self.professor}'
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
		
		"""Validation for attainments"""
		for item in self.enter_courselab_name:
			if item.attainment<0 or item.attainment>3:
				frappe.throw("Attainment should be between: 0 to 3")

def renameDoc(base_name, academic_year):
	dict = {'name_value': None}
	filters = {
		"name": ["like", base_name + "%"]
	}
	field = 'name'
	similar_docs = frappe.get_list("Course_Lab outcome attainment", filters= filters, pluck = field)
	dict['name_value'] = base_name
	return dict
