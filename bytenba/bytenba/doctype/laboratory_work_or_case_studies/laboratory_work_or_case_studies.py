# Copyright (c) 2023, byte_team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import bytenba.form_validation as validation
import re

pattern_for_wtg = r'\((\s*(?:\d+\.\d+|\d+)\s*)\)'
Doctype = "Laboratory Work Or Case Studies"

class LaboratoryWorkOrCaseStudies(Document):

	"""method to autoname your document"""
	def autoname(self):
		self.name = f'AI4_{self.owner}_{self.academic_year}_{self.semester}'
	
	def before_save(self):
		self.self_appraisal_score = compute_marks(self)

	def validate(self):
		validation.standard_validation(self)


def compute_marks(self):
	
	for item in self.lab_work_case_study_ct:
		return item.mms1
	# count = 0
	# appraisal_score = 0
	
	# for item in self.lab_work_case_study_ct:

	# 	count += 1

	# 	mms_category = False
	# 	engg_category = False

	# 	mms1 = item.mms_a
	# 	mms2 = item.mms_b
		
	# 	engg1 = item.engg_a
	# 	engg2 = item.engg_b
	# 	engg3 = item.engg_c

	# 	match = re.search(pattern_for_wtg, self.marks_obtained)
	# 	if match:
	# 		mappingval = float(match.group(1).strip())
	# 	else:
	# 		frappe.throw('Error Fetching Field Weightages')
		
	# 	if mms1 and mms2:
	# 		mms_category = True
	# 		if mms1 < 0 or mms2 < 0:
	# 			frappe.throw(f"MMS weights cannot be negative, error in row {count}")
	# 		if (mms1 > 1.5 or mms2 > 1):
	# 			frappe.throw(f"MMS weights cannot exceed specified ranges, error in row {count}")
	# 		mms = mms1*mms2
		
	# 	if engg1 and engg2 and engg3:
	# 		if engg1 < 0 or engg2 < 0 or engg3 < 0:
	# 			frappe.throw(f"Engg weights cannot be negative, error in row {count}")
	# 		if (engg1 > 1.5 or engg2 > 1.25 or engg3 > 1):
	# 			frappe.throw(f"Engg weights cannot exceed specified ranges, error in row {count}")
	# 		engg_category = True
	# 		engg = engg1*engg2*engg3
		
	# 	if mms_category and engg_category:
	# 		frappe.throw(f'Cannot fill both categories in the same row, error in row {count} ')
	# 	if mms_category:
	# 		item.marks_obtained = mms*mappingval
	# 	if engg_category:
	# 		item.marks_obtained = engg*mappingval
	# 	else:
	# 		frappe.throw(f'Values incorrectly entered in row {count}')
		
	# 	appraisal_score += item.marks_obtained
	
	# return appraisal_score / count






		

		

					