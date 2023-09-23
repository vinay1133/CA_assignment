# Copyright (c) 2023, byte_team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

doctype = 'Certification for courses allotted'

class Certificationforcoursesallotted(Document):
	
	def before_save(self):
		
		"""get platform type"""
		platform_type_str = self.platform_type
		platform_mapping = {'Professor/Industry Expert of National/International repute (1.5)': 1.5, 'Professor from State college (1)' :1, 'Any other (0.4)': 0.4}
		platform_param = platform_mapping.get(platform_type_str, 0)

		"""get values for number of hours"""
		no_hrs_str = self.number_of_hours
		hours_mapping = {'30+': 1, '20+': 0.5, 'Below 20': 0}
		hours_param = hours_mapping.get(no_hrs_str, 0)

		"""get assessment outcome"""
		assessment_outcome_str = self.assessment_outcome
		assessment_mapping = {'Grade B or Above (1)': 1, 'Pass (0.4)': 0.4, 'Audit (0.2)': 0.2, 'Fail (0)': 0}
		assessment_param = assessment_mapping.get(assessment_outcome_str, 0)

		"""get date of certification parameter"""
		doc_str = self.date_of_cerftification
		doc_mapping = {'2 years (1)': 1, '2 to 4 years (0.75)': 0.75, '4 to 6 years (0.4)': 0.4, 'More than 6 years (0)': 0}
		doc_param = doc_mapping.get(doc_str, 0)

		product_of_wts = platform_param*hours_param*assessment_param*doc_param
		marks = product_of_wts*100

		self.marks_obtained = marks

	def validate(self):
		pass


	# def validate(self):

	# 	date = getdate(self.reporting_date)
	# 	month_end = get_last_day(date)
	# 	if date!=month_end:
	# 		frappe.throw('Entered date is not the end of the month')

	# 	"""validate the team begin size"""
	# 	if self.period_begin_team_size < 0:
	# 		frappe.throw('Team size at the beginning cannot be less than 0')

	# 	"""validate the team end size"""
	# 	if self.period_end_team_size < 0:
	# 		frappe.throw('Team size at the end cannot be less than 0')

	# 	"""validate employee leaving"""
	# 	if self.employee_leaving < 0:
	# 		frappe.throw('Employee leaving number cannot be less than 0')

	# 	"""validate correction field"""
	# 	if self.correction < 0:
	# 		frappe.throw('Correction value cannot be less than 0')

	# 	if self.correction > self.employee_leaving:
	# 		frappe.throw('Correction value cannot be greater than the number of employees leaving')

	# 	"""validate that team begin and end size sum is not equal to 0"""
	# 	if self.period_begin_team_size == 0 and self.period_end_team_size == 0:
	# 		frappe.throw('Cannot calculate attrition percentage for this input')

	# 	"""validate if same record exists in database"""
	# 	existing_record = frappe.db.exists('Employee Attrition', {'name': self.name})
	# 	"""check if it is not the document currently begin worked upon"""
	# 	if existing_record and existing_record != self.name:
	# 		frappe.throw('There already exists such a record in the database')
