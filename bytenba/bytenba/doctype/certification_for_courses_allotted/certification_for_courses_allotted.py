# Copyright (c) 2023, byte_team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import re

Doctype = 'Certification for courses allotted'
pattern = re.compile(r'^\d{4}-\d{4}$')

platform_mapping = {'Professor/Industry Expert of National/International repute (1.5)': 1.5, 'Professor from State college (1)' :1, 'Any other (0.4)': 0.4}
hours_mapping = {'30+': 1, '20+': 0.5, 'Below 20': 0}
assessment_mapping = {'Grade B or Above (1)': 1, 'Pass (0.4)': 0.4, 'Audit (0.2)': 0.2, 'Fail (0)': 0}
doc_mapping = {'2 years (1)': 1, '2 to 4 years (0.75)': 0.75, '4 to 6 years (0.4)': 0.4, 'More than 6 years (0)': 0}

class Certificationforcoursesallotted(Document):
	
	"""method to autoname your document"""
	def autoname(self):
		base_name = f'AI1_{self.academic_year}_{self.professor}'
		data = renameDoc(base_name, self.academic_year)
		if data['name_value']:
			self.name = data['name_value']
		else:
			frappe.throw("Failed to generate a unique name.")
	
	def before_save(self):
		# frappe.msgprint('inside before save')
		marks = compute_marks(self)
		self.marks_obtained = marks

	def validate(self):
		academic_yr_str = self.academic_year
		if not re.match(pattern, academic_yr_str):
			frappe.throw('Academic year must be of the form like 2022-2023')
		else:
			yr_end_1 = academic_yr_str[3]
			yr_end_2 = academic_yr_str[-1]

			# if yr_end_1 == 

def compute_marks(self):
  
    """get platform type"""
    platform_type_str = self.platform_type
    platform_param = platform_mapping.get(platform_type_str, 0)

    """get values for number of hours"""
    no_hrs_str = self.number_of_hours
    hours_param = hours_mapping.get(no_hrs_str, 0)

    """get assessment outcome"""
    assessment_outcome_str = self.assessment_outcome
    assessment_param = assessment_mapping.get(assessment_outcome_str, 0)

    """get date of certification parameter"""
    doc_str = self.date_of_cerftification
    doc_param = doc_mapping.get(doc_str, 0)

    product_of_wts = platform_param*hours_param*assessment_param*doc_param
    marks = product_of_wts*100

    return marks

def renameDoc(base_name, academic_year):
	dict = {'name_value': None}
	filters = {
		"name": ["like", base_name + "%"]
	}
	field = 'name'
	similar_docs = frappe.get_list(Doctype, filters= filters, pluck = field)
	if len(similar_docs) == 0:
		dict['name_value'] = base_name + '_0'
		return dict
	if len(similar_docs) == 1:
		form_num = int(similar_docs[0][-1])
		new_num = form_num + 1
		dict['name_value'] = f"{base_name}_{new_num}"
	elif len(similar_docs) == 2:
			frappe.throw(f'Maximum limit of 2 for AI1 forms for the academic year {academic_year} has been reached, kindly delete existing forms to create more')
	else:
			frappe.throw(f'Something went wrong')
	return dict
		
def rankDocs(doc, method):
	filters = {
		"name": ["like", doc.name[:-2] + "%"]
	}
	field = 'name'
	similar_docs = frappe.get_list("Certification for courses allotted", filters= filters, pluck = field)
	if len(similar_docs) == 2:
		for doc_name in similar_docs:
			if doc_name != doc.name:
				old_doc_name = doc_name
		e_doc = frappe.get_doc(Doctype, old_doc_name)
		e_marks = e_doc.marks_obtained
		if e_marks > doc.marks_obtained:
			e_doc.db_set('max_val', 'True', commit = True)
			doc.db_set('max_val', 'False', commit = True)
		elif doc.marks_obtained > e_marks:
			e_doc.db_set('max_val', 'False', commit = True)
			doc.db_set('max_val', 'True', commit = True)
		else:
			e_doc.db_set('max_val', 'Equal Score', commit = True)
			doc.db_set('max_val', 'Equal Score', commit = True)
	else:
		pass