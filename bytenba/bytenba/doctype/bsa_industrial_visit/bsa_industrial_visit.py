# Copyright (c) 2023, byte_team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import bytenba.form_validation as validation
import re

Doctype = 'BSA industrial visit'
pattern = re.compile(r'^\d{4}-\d{4}$')

class BSAindustrialvisit(Document):

	def autoname(self):
		self.name = f'AI3b_{self.professor}_{self.academic_year}_{self.semester}'
	
	def before_save(self):
		marks_dict = compute_marks(self)
		self.quality_relevance = marks_dict['quality_relevance']
		self.marks_obtained = marks_dict['total_marks']
		self.self_appraisal_score = marks_dict['total_marks']

	def validate(self):
		validation.standard_validation(self)

		if self.number_of_attendees > self.total_students:
			frappe.throw('Number of attendees cannot be greater than the number of students enrolled')		

		if (self.number_of_attendees or self.total_students or self.number_of_feedbacks) < 0:
			frappe.throw('feedback criterion cannot have negative values')
		
		if self.number_of_feedbacks > self.number_of_attendees:
			frappe.throw('Number of feedbacks cannot be greater than number of attendees')
		
		if (self.number_of_projects):
			if int(self.number_of_projects) < 0:
				frappe.throw('number of projects cannot be less than 0')

		if (self.number_of_internships):
			if int(self.number_of_internships) < 0:
				frappe.throw('number of projects cannot be less than 0')

		if (self.projects_status == 'None (1)'):
			if (self.number_of_projects and self.number_of_projects > 0):
				frappe.throw('If projects are not done then number of projects cannot be greater than 0')
		
		if (self.internships_status == 'None (1)'):
			if (self.number_of_internships and self.number_of_internships > 0):
				frappe.throw('If internships are not done then number of internships cannot be greater than 0')

def compute_marks(self):
	
	marksDict = {
		"quality_relevance": None,
		"total_marks" : None
	}

	mou_place_mapping = {
		"New MOU with industry / organization (1.5)": 1.5,
		"none (1)": 1
	}
	mou_place_str = self.mou_for_placement
	mou_place_param = mou_place_mapping.get(mou_place_str, 0)

	mou_intern_mapping = {
		'New MOU with industry / organization for internship including last 6 months (1.25)': 1.25,
		'none (1)': 1
	}
	mou_intern_str = self.mou_for_internship
	mou_intern_param = mou_intern_mapping.get(mou_intern_str, 0)

	faculty_presence_mapping = {
		'faculty present (1)': 1,
		'faculty absent (0.3)': 0.3
	}
	faculty_presence_str = self.faculty_presence
	faculty_presence_param = faculty_presence_mapping.get(faculty_presence_str, 0)

	internships_status_mapping = {
		'Equal to or more than 1 (1.2)' : 1.2,
		'None (1)': 1
	}
	internships_status_str = self.internships_status
	internships_status_param = internships_status_mapping.get(internships_status_str, 0)

	projects_status_mapping ={
		'Equal to or more than 1 (1.1)': 1.1,
		'None (1)': 1
	}
	projects_status_str = self.projects_status
	projects_status_param = projects_status_mapping.get(projects_status_str, 0)

	total_students = self.total_students
	number_of_attendees = self.number_of_attendees
	number_of_feedbacks = self.number_of_feedbacks
	quality_relevance = number_of_attendees / total_students  if number_of_feedbacks > 2.5 else 0
	marksDict['quality_relevance'] = quality_relevance


	mapping_mapping_dict = {
	'Strongly to PO (1.5)': 1.5,
	'Strongly to CO (1)': 1,
	'Moderately to PO (1)': 1,
	'Moderately to CO (0.8)': 0.8,
	'Neither mapping to CO or PO (0)': 0
	}
	mapping_str = self.mapping
	mapping_param = mapping_mapping_dict.get(mapping_str, 0)

	product_of_wts = mapping_param*quality_relevance*projects_status_param*internships_status_param*faculty_presence_param*mou_intern_param*mou_place_param
	marks = product_of_wts*75
	marksDict['total_marks'] = marks

	return marksDict