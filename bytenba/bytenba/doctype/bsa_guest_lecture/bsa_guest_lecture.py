# Copyright (c) 2023, byte_team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import bytenba.custom_utilities as uf
import re

Doctype = 'BSA guest lecture'
pattern = re.compile(r'^\d{4}-\d{4}$')


class BSAguestlecture(Document):

	"""method to autoname your document"""
	def autoname(self):
		base_name = f'AI3a_{self.professor}_{self.academic_year}_{self.semester}'
		data = renameDoc(base_name, self.academic_year)
		if data['name_value']:
			self.name = data['name_value']
		else:
			frappe.throw("Failed to generate a unique name.")
	
	def before_save(self):
		
		marks_dict = compute_marks(self)
		self.quality_relevance = marks_dict['quality_relevance']
		self.marks_obtained = marks_dict['total_marks']

	def validate(self):
		"""Academic year validations"""
		uf.validateAY(self.academic_year)
		existing_record = frappe.db.exists(Doctype, {'name': self.name})
		if existing_record and existing_record != self.name:
			frappe.throw('There already exists such a record in the database') 

		if self.number_of_attendees > self.total_students:
			frappe.throw('Number of attendees cannot be greater than the number of students enrolled')		

		if (self.number_of_attendees or self.total_students or self.number_of_feedbacks) < 0:
			frappe.throw('No field in this form can have a negative value')
		
		if self.number_of_feedbacks > self.number_of_attendees:
			frappe.throw('Number of feedbacks cannot be greater than number of attendees')


def compute_marks(self):
	marksDict = {'quality_relevance': None,'total_marks': None}

	total_students = self.total_students
	number_of_attendees = self.number_of_attendees
	number_of_feedbacks = self.number_of_feedbacks
	quality_relevance = number_of_attendees / total_students  if number_of_feedbacks > 2.5 else 0
	marksDict['quality_relevance'] = quality_relevance

	quality_mapping = {
		'International / National VP and above / Unicorn Startup - CXO (1)': 1,
		'SME (0.5)': 0.5,
		'International / National Prof & Above (1)': 1,
		'State (0.5)': 0.5
	}
	quality_of_speaker_str = self.quality_of_speaker
	quality_param = quality_mapping.get(quality_of_speaker_str, 0)

	mapping_mapping_dict = {
		'Strongly to PO (1.5)': 1.5,
		'Strongly to CO (1)': 1,
		'Moderately to PO (1)': 1,
		'Moderately to CO (0.8)': 0.8,
		'Neither mapping to CO or PO (0)': 0
	}
	mapping_str = self.mapping
	mapping_param = mapping_mapping_dict.get(mapping_str, 0)

	product_of_wts = quality_relevance*quality_param*mapping_param
	marks = product_of_wts*75
	if marks > 113:
		marks = 113
	marksDict['total_marks'] = marks

	return marksDict

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
			frappe.throw(f'Maximum limit of 2 for AI13a forms for the academic year {academic_year} has been reached, kindly delete existing forms to create more')
	else:
			frappe.throw(f'Something went wrong')
	return dict
		
def addDocs(doc, method):
	filters = {
		"name": ["like", doc.name[:-2] + "%"]
	}
	field = 'name'
	similar_docs = frappe.get_list(Doctype, filters= filters, pluck = field)
	if len(similar_docs) == 2:
		for doc_name in similar_docs:
			if doc_name != doc.name:
				old_doc_name = doc_name
		e_doc = frappe.get_doc(Doctype, old_doc_name)
		e_marks = e_doc.marks_obtained		
		e_doc.db_set('self_appraisal_score', doc.marks_obtained + e_marks, commit = True)
		doc.db_set('self_appraisal_score', doc.marks_obtained + e_marks, commit = True)
	else:
		pass